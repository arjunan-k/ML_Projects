var col1 = prompt("What is the first color?")
var col2 = prompt("What is the second color?")

var body = document.getElementById("gradient")
var but = document.getElementById("but")
body.style.background = "linear-gradient(to right, " + col1 + ", " + col2 + ")";

var color1 = document.querySelector(".color1")
var color2 = document.querySelector(".color2")
color1.setAttribute("value", col1)
color2.setAttribute("value", col2)
var css = document.querySelector("h3");

css.textContent = body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ");";

function setGradient() {
  body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ")";
  css.textContent = body.style.background + ";";
}

var hexlist = [0, 1, 2, 3, 4 ,5 ,6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
var newList = []

function random_item(items) {
  return items[Math.floor(Math.random()*items.length)];
}

function randomGenerator(event) {
  for (j=0; j<2; j++) {
    text = "#"
    for (i=0; i<6; i++) {
      var item = hexlist[Math.floor(Math.random()*hexlist.length)];
      text = text + item
    } newList.push(text)
  }
  code1 = newList[0]
  code2 = newList[1]
  newList = []
  color1.setAttribute("value", code1)
  color2.setAttribute("value", code2)
  body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ")";
  css.textContent = body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ")";
}

color1.addEventListener("input", setGradient);
color2.addEventListener("input", setGradient);
but.addEventListener("click", randomGenerator)
