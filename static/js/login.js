function login(){

  var username = document.getElementById("username");
  var pass = document.getElementById("password");

  if (username.value == ""){
    alert("Please enter user name");
  }

  else if (pass.value == ""){
    alert("Please enter password");
  }
}
function init2(){
  var login1 = document.getElementById("loginform");
  login1.onsubmit = login;
}
window.addEventListener("load",init2);
