
let draggabletodo = null;
function dragStart(){
    draggabletodo = this;
    console.log("dragStart");
}
function dragEnd(){
    draggabletodo = null;
    console.log("dragEnd");
}

function dragOver(e){//for drag target
    e.preventDefault();
    console.log("dragOver");
    //when the draggable element is over the targer
    //we see this action
}

function dragEnter(){
    console.log("dragEnter");
}
function dragLeave(){
    console.log("dragLeave");
}

function dragDrop(){
    this.appendChild(draggabletodo);
    console.log("dropped");
}

function createTodo() {
  //get input value and store them
    // const inner_div = document.createElement("div");
    const input_val1 = document.getElementById("todo_input1").value;
    // const txt1 = document.createTextNode(input_val1);
    const input_val2 = document.getElementById("todo_input2").value;
    // const txt2 = document.createTextNode(input_val2);

   
    //creating div1 for task name and div2 for task description in cards
    const inner_inner_div1 = document.createElement("div");
    const inner_inner_div2 = document.createElement("div");
    // inner_div.appendChild(inner_inner_div1);
    // inner_div.appendChild(inner_inner_div2);
    // inner_inner_div1.appendChild(txt1);
    // inner_inner_div2.appendChild(txt2);
    
    //create div for new card
    // inner_div.classList.add("inner");
    inner_div.setAttribute("draggable", "true");
    //create span for "x" button
    const span = document.createElement("span");
    const span_txt1 = document.createTextNode("\u00D7");
    const span_txt2 = document.createTextNode("\u00D7");

    span.classList.add("close");
    span.appendChild(span_txt1,span_txt2);

    inner_div.appendChild(span);
    //add eventlistener for "x" button
    no_status.appendChild(inner_div);
  
    span.addEventListener("click", () => {
      span.parentElement.style.display = "none";
    });
    //add eventlistener for drag and drop of new card
    inner_div.addEventListener("dragstart", dragStart);
    inner_div.addEventListener("dragend", dragEnd);
  
    document.getElementById("todo_input1").value = "";
    document.getElementById("todo_input2").value = "";
    todo_form.classList.remove("active");
    overlay.classList.remove("active");


  }
  

  
  
function init3(){
    const todos = document.querySelectorAll(".inner");
    todos.forEach((todo) =>{
    todo.addEventListener("dragstart",dragStart);
    todo.addEventListener("dragend",dragEnd);
})
    const all_innerbox = document.querySelectorAll(".innerbox")
    all_innerbox.forEach((innerbox)=>{
        innerbox.addEventListener("dragover",dragOver);
        innerbox.addEventListener("dragenter",dragEnter);
        innerbox.addEventListener("dragleave",dragLeave);
        innerbox.addEventListener("drop",dragDrop);
    })

    const btns = document.querySelectorAll("[data-target-modal]");
    const close_modals = document.querySelectorAll(".close-modal");
    const overlay = document.getElementById("overlay");

    btns.forEach((btn) => {
        btn.addEventListener("click", () => {
          document.querySelector(btn.dataset.targetModal).classList.add("active");
          overlay.classList.add("active");
        });
      });
      
      close_modals.forEach((btn) => {
        btn.addEventListener("click", () => {
          const modal = btn.closest(".modal");
          modal.classList.remove("active");
          overlay.classList.remove("active");
        });
      });

      window.onclick = (event) => {
        if (event.target == overlay) {
          const modals = document.querySelectorAll(".modal");
          modals.forEach((modal) => modal.classList.remove("active"));
          overlay.classList.remove("active");
        }
      };

  const todo_submit = document.getElementById("todo_submit");
  todo_submit.addEventListener("click", createTodo);


  const close_btns = document.querySelectorAll(".close");

  close_btns.forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.parentElement.style.display = "none";
    });
  });
}

window.addEventListener("load",init3);