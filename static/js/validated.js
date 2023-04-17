"use strict";
function validate(){

	var errMsg = "";								/* stores the error message */
	var result = true;								/* assumes no errors */

  var firstname = document.getElementById("fname").value;
  var lastname = document.getElementById("lname").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var comfimpw = document.getElementById("comfirmpw").value;


  if (document.getElementById("position").value == "") {
      errMsg = "Please select at least one position.\n";
      result = false;
  }

  if (firstname == "") {
		errMsg += "Employee ID cannot be empty.\n";
    }

  if (lastname =="") {
      errMsg += "Last Name cannot be empty.\n";
  }
  if (!lastname.match(/^[a-zA-Z]+$/)){
    errMsg = errMsg + "Please enter a valid last name.\n"
    result = false;
  }
  if (!email.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)){
    errMsg = errMsg + "Please enter a valid email address.\n"
    result = false;
  }
  if (!password.match(/^.{8,20}$/)){
    errMsg = errMsg + "Please enter a valid password between 8 to 20 characters.\n"
    result = false;
  }
  else if (password != comfimpw){
    errMsg = errMsg + "Please match your password.\n"
    result = false;
  }
	if (errMsg !=""){
    alert(errMsg);
    return result; }   //if false the information will not be sent to the server

  if (result) {
    storeRegister(firstname, lastname, email, password, comfimpw)
    return result;
  }
}

function storeRegister(firstname, lastname, email, password, comfimpw){
  sessionStorage.firstname = firstname;
  sessionStorage.lastname = lastname;
  sessionStorage.email = email;
  sessionStorage.password = password;
  sessionStorage.comfimpw = comfimpw;
}

function init1() {
  var regForm = document.getElementById("regform");
  regForm.onsubmit = validate;

}
window.addEventListener("load",init1);
