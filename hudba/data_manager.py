import re
import requests
import sqlite3
from bs4 import BeautifulSoup
from hudba.models import Genre, Band


def genrescsv():
    genres = Genre.objects.order_by('id')
    url = 'hudba/static/csv/genres.csv'
    f = open(url, 'r')
    lines = f.readlines()
    f.close()
    f = open(url, 'w')
    for number, line in enumerate(lines):
        split = line.split(';')
        correct = 0
        for genre in genres:
            if split[0] == genre.name:
                correct = 1
                break
        if correct == 1:
            f.write(line)
    f.close()

    for genre in genres:
        f = open(url, 'r')
        lines = f.readlines()
        i = 0
        found = 0
        while i < len(lines):
            splitline = lines[i].split(';')
            name = splitline[0]
            if name == genre.name:
                found = 1
                break
            else:
                i += 1
        if found == 0:
            link = "https://cs.wikipedia.org/wiki/" + genre.name
            response = requests.get(url=link)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.select('p')[0]
            para = item.text
            edit = para.replace('\'', ' ')
            finaledit = edit.replace('\"', ' ')
            modify = re.sub(r"\[[^()]*]", "", finaledit)
            csvinput = genre.name + ';' + modify
            f = open(url, 'a', encoding='windows-1250')
            f.write(csvinput)
        f.close()


def bandscsv():
    bands = Band.objects.order_by('id')
    url = 'hudba/static/csv/bands.csv'
    f = open(url, 'r')
    lines = f.readlines()
    f.close()
    f = open(url, 'w')
    for number, line in enumerate(lines):
        split = line.split(';')
        correct = 0
        for band in bands:
            if split[0] == band.title:
                correct = 1
                break
        if correct == 1:
            f.write(line)
    f.close()

    for band in bands:
        f = open(url, 'r')
        lines = f.readlines()
        i = 0
        found = 0
        while i < len(lines):
            splitline = lines[i].split(';')
            name = splitline[0]
            if name == band.title:
                found = 1
                break
            else:
                i += 1
        if found == 0:
            link = "https://cs.wikipedia.org/wiki/" + band.title
            response = requests.get(url=link)
            soup = BeautifulSoup(response.content, 'html.parser')
            csvinput = band.title
            items = [soup.select('p')[0], soup.select('p')[1], soup.select('p')[2]]
            for item in items:
                item = item.text
                item = item.replace('\'', ' ')
                item = item.replace('\"', ' ')
                item = item.replace('¡', ' ')
                modified_item = re.sub(r"\[[^()]*]", "", item)
                csvinput = csvinput + ';' + modified_item
            f = open(url, 'a', encoding='windows-1250')
            f.write(csvinput)
        f.close()


def genressql():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    f = open('hudba/static/csv/genres.csv', 'r')
    i = 0
    lines = f.readlines()
    while i < len(lines):
        split = lines[i].split(';')
        article = split[1]
        name = split[0]

        cur.execute("UPDATE hudba_genre SET article = '" + article + "' WHERE name = '" + name + "'")
        i += 1
    con.commit()
    con.close()


def bandssql():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    f = open('hudba/static/csv/bands.csv', 'r')
    i = 0
    lines = f.readlines()
    while i < len(lines):
        split = lines[i].split(';')
        article = split[1]
        name = split[0]

        cur.execute("UPDATE hudba_band SET article = '" + article + "' WHERE title = '" + name + "'")
        i += 1

    con.commit()
    con.close()
