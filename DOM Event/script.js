var userinput = document.getElementById("userinput");
var add = document.getElementById("add");
var ul = document.querySelector("ul");

function inputLength() {
  return userinput.value.length
}

function createListElement() {
  var div = document.createElement("div");
  var li = document.createElement("li");
  var but = document.createElement("button");
  div.classList.add("wrapper")
  li.appendChild(document.createTextNode(userinput.value))
  but.appendChild(document.createTextNode("Delete"))
  div.appendChild(li)
  div.appendChild(but)
  ul.appendChild(div)
  userinput.value = ""
}

function addListAfterClick() {
  if (inputLength() > 0) {
    createListElement();
  }
}

function addListAfterEnter(event) {
  if (inputLength() > 0 && event.which === 13) {
    createListElement()
  }
}

function lineThroughTodo(element) {
  if (element.target.tagName === "LI") {
    element.target.classList.toggle("done")
  }
}

function deleteTodo(element) {
  if (element.target.tagName === "BUTTON") {
    element.target.parentElement.remove()
  }
}

function handleUIChange(element) {
  lineThroughTodo(element)
  deleteTodo(element)
}

add.addEventListener("click", addListAfterClick);
userinput.addEventListener("keypress", addListAfterEnter);
ul.addEventListener("click", handleUIChange);
