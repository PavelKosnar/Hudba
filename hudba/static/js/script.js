$(document).ready(function (){
    $(".bands").hide()
    $(".toggle_bands").click(function (){
        $(".change").attr({
            "class" : "col change_back"
        });
        $(".bands").show()
    });
    $("h1").click(function (){
        $(".change_back").attr({
            "class" : "row change"
        });
        $(".bands").hide()
    });
});
