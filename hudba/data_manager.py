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
            csvinput = genre.name + ';' + finaledit + '...' + '\n'
            f = open(url, 'a')
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
            item = soup.select('p')[0]
            para = item.text
            edit = para.replace('\'', ' ')
            finaledit = edit.replace('\"', ' ')
            csvinput = band.title + ';' + finaledit + '...' + '\n'
            f = open(url, 'a')
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
        id = i + 1
        print(i)

        cur.execute("UPDATE hudba_genre SET article = '" + article + "' WHERE id = " + str(id) + "")
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
        id = i + 1
        print(i)

        cur.execute("UPDATE hudba_band SET article = '" + article + "' WHERE id = " + str(id) + "")
        i += 1

    con.commit()
    con.close()
