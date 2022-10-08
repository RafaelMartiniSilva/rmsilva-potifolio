
/* Code section ****.menu-nav-active**** - This peace of code open and close the side menu on mobile screen */
const menuMobile = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

menuMobile.addEventListener('click', () => {
    menuMobile.classList.contains("bi-list")
        ? menuMobile.classList.replace("bi-list", "bi-x")
        : menuMobile.classList.replace("bi-x", "bi-list");

    body.classList.toggle("menu-nav-active");
});


/* Close the menu side bar when clicking in any item and automatic change icon to bi-list */
const naveItem = document.querySelectorAll(".nav-item")

naveItem.forEach((item) => {
    item.addEventListener('click', () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active")
            menuMobile.classList.replace("bi-x", "bi-list");
        }
    })
})


// Animate all the data-anime attributes
const item = document.querySelectorAll("[data-anime]");
console.log(item);

const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;
    console.log("windowTop=" + windowTop);

    item.forEach((element) => {
        if (windowTop > element.offsetTop) {
            console.log("element[" + element.localName + "].offsetTop=" + element.offsetTop + " ///// windowTop=" + windowTop);
            element.classList.add("animate");
        } else {
            element.classList.remove("animate");
        }
    });
};
animeScroll()

window.addEventListener("scroll", () => {
    animeScroll();
});


// Change the send e-mail button
const btnEnviar = document.querySelector('#btn-enviar')
const btnEnviarLoader = document.querySelector('#btn-enviar-loader')
btnEnviar.addEventListener("click", ()=>{
  btnEnviarLoader.style.display = "block";
  btnEnviar.style.display = "none"
})

// Erase flash messages after 5 seconds
setTimeout(()=>{
    document.querySelector('#alerta').style.display = "none";
}, 5000)
