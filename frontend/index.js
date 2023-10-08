const header= document.querySelector("header");
window.addEventListener("scroll", function(){
    header.classList.toggle("sticky",window.scrollY>0);
})

document.addEventListener("DOMContentLoaded", function() {
const scrollList = document.querySelectorAll(".scroll-list li a");

 scrollList.forEach(function(link) {
link.addEventListener("click", function(e) {
e.preventDefault();
 const targetId = this.getAttribute("href").substring(1); // Remove the "#" from the href
 const targetSection = document.getElementById(targetId);
if (targetSection) {
targetSection.scrollIntoView({ behavior: "smooth" });
 }
});
 });
});





