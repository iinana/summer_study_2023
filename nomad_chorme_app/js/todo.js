const todoForm = document.querySelector("#todo-form");
const todoInput = todoForm.querySelector("input");
const todoList = document.querySelector("#todo-list");

function paintTodo(newTodo) {
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newTodo;

  const button = document.createElement("button")
  button.innerText = ❌"

  li.appendChild(span);
  li.appendChild(button)
  todoList.appendChild(li);

  button.addEventListener("click", deleteTodo);
}


function handleTodoSubmit(event) {
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = "";
  paintTodo(newTodo);
}
todoForm.addEventListener("submit", handleTodoSubmit);
