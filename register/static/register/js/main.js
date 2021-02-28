function myFunction(x, y) {
    x.classList.toggle("change");
    document.getElementById("btn1").classList.toggle("button_change");
    document.getElementById("btn2").classList.toggle("button_change");
    document.getElementById("btn3").classList.toggle("button_change");
    document.getElementById("btn4").classList.toggle("button_change");
    document.getElementById("header_for_top").classList.toggle("header_for_top_on");
}

var modal = document.getElementById('id01');

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
