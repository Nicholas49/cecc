function teamedit(emt) {

    if (emt.value == ''){
        emt.value = '0';
    }
    emt.parentElement.submit();
}


function disableb() {
    var buttons = document.getElementsByTagName("button");
    var b;
    for (b of buttons){
        b.disabled = true;
    }
}


function showform(evt) {
    evt.nextElementSibling.classList.toggle('opened');
    evt.classList.toggle('down');
    if(evt.classList == 'drop down'){
        evt.children[1].innerHTML = '&#9660;';
    }
    else{
        evt.children[1].innerHTML = '&#9650;';
    }
}


function reveal() {
    var aa = document.getElementById("aa");
    var dd = document.getElementById('dd');
    var bb = document.getElementById('bb');
    aa.classList.toggle("hidden");
    dd.classList.toggle("hidden");
    bb.classList.toggle("hidden");
}


function revealResponse(){
    var rr = document.getElementById('rr');
    rr.classList.toggle("hidden");
}


function expandgame(evt){
    evt.nextElementSibling.classList.toggle("hidden2");
}


function deletegame(gname) {
/*    if (confirm("Are you sure you want to delete " + gname + "? You can't undo this!")) {
        window.location.assign("https://01as.pythonanywhere.com/jeopardy/delete_game/" + gname);
    }*/

    alert("Sorry, this function is disabled for now.");
}


function creategame() {
    var gname = document.getElementById('newname').value;
    window.location.assign("https://01as.pythonanywhere.com/jeopardy/create_game/" + gname);
}


function updatescore(evt, points, dollar) {
    if(evt.checked == true) {
        b = points + dollar;
        evt.nextElementSibling.firstElementChild.innerHTML = b;
    }
    if(evt.checked == false) {
        evt.nextElementSibling.firstElementChild.innerHTML = points;
    }
}

