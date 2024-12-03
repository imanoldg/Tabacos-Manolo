document.addEventListener("DOMContentLoaded", function (){

    const currentPath = window.location.pathname;

    const menuLinks = document.querySelectorAll("#menu li a");

    menuLinks.forEach(link => {
        if(link.getAttribute("href") === currentPath){
            link.parentElement.classList.add("selected");
        }
    })
})