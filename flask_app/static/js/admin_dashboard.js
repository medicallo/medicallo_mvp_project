(function () {
'use strict'
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
})
})()

function over(element) {
    element.style.backgroundColor = "blue"; 
    element.style.borderRadius = "5px"; 
}
    
function out(element) {
    element.style.backgroundColor = "rgb(33, 36, 41)";   
}


function openForm() {
        document.querySelector("#popupForm").style.display = "block";
}
function closeForm() {
        document.querySelector("#popupForm").style.display = "none";
    
}
function openForm1() {
    document.querySelector("#popupForm1").style.display = "block";
}
function closeForm1() {
    document.querySelector("#popupForm1").style.display = "none";

}
function openForm2() {
    document.querySelector("#popupForm2").style.display = "block";
}
function closeForm2() {
    document.querySelector("#popupForm2").style.display = "none";

}
function openForm3() {
    document.querySelector("#popupForm3").style.display = "block";
}
function closeForm3() {
    document.querySelector("#popupForm3").style.display = "none";

}
function openForm4() {
    document.querySelector("#popupForm4").style.display = "block";
}
function closeForm4() {
    document.querySelector("#popupForm4").style.display = "none";

}
