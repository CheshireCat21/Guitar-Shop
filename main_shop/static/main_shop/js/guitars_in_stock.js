function filterSelectionAll() {
    var x, i, a;
    x = document.getElementsByClassName("column");
    for (i = 0; i < x.length; i++) {
        if (x[i].className.slice(-9,) == 'show_none'){
            x[i].className = x[i].className.slice(0,-10);
        }
    }
}


function filterSelection(c) {
    var x, i, a;
    x = document.getElementsByClassName("column");
    for (i = 0; i < x.length; i++) {
        if (x[i].className != c && x[i].className.slice(-9,) != 'show_none') {
            x[i].className += " " + "show_none";
        }
        if (x[i].className.slice(0,-10) == c) {
            x[i].className = x[i].className.slice(0,-10);
        }
    }
}


function MakeOrder(text, img, guitar) {
    order_form.style.display = 'block';
    console.log(text, guitar);

    let photo = document.getElementById('photo-block');
    photo.src = img;
}

window.onclick = function(event) {
  if (event.target == order_form) {
    order_form.style.display = "none";
  }
}












/*    document.getElementById('1').innerHTML = guitar;*/