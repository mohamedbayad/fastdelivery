let topHeader = document.querySelector('.top-header');
let scoter = document.getElementById("scoter");
let boxOne = document.getElementById('box-one');
let boxtwo = document.getElementById('box-two');
let boxThree = document.getElementById('box-three');

window.onscroll = function() {
    const value = scrollY
    if (scrollY >= 100) {
        topHeader.style.backgroundColor = "white";
        topHeader.style.boxShadow = "0 0 11px 0 #00000024";
        topHeader.style.zIndex = "999";
        
    } else {
        topHeader.style.backgroundColor = "transparent";
        topHeader.style.boxShadow = "none";
    }

    if (scrollY >= 180) {
        boxOne.style.cssText = 'transform: translateX(0px); opacity: 1;'
        boxtwo.style.cssText = 'opacity: 1;'
        boxThree.style.cssText = 'transform: translateX(0px); opacity: 1;'
    } else {
        boxOne.style.cssText = 'transform: translateX(-500px); opacity: 0;'
        boxtwo.style.cssText = 'opacity: 0;'
        boxThree.style.cssText = 'transform: translateX(500px); opacity: 0;'
    }

    scoter.style.left = value * .5 + "px"
}

let search = document.getElementById("search");
let pricingThumb = document.querySelectorAll(".pricing-thumb .title");
let listWord = []
search.oninput = function() {
    pricingThumb.forEach(t => {
        if (search.value !== "") {
            t.parentElement.style.display = "none"
            listWord.push(t)
            if (t.textContent.trim().toLowerCase().includes(search.value.trim().toLowerCase())) {
                t.parentElement.style.display = "block"
                // console.log(Array.apply(t.textContent.trim().toLowerCase()))
            } else {
                t.parentElement.style.display = "none"
            }
        } else {
            search.value = "";
            t.parentElement.style.display = "block"
        }
    })
}

let navTop = document.querySelector(".nav-top")
let navMobileClose = document.createElement("i");

navMobileClose.setAttribute("class", "fa-solid fa-xmark");
navMobileClose.classList.add('close')
navTop.appendChild(navMobileClose)

let navMobile = document.querySelector(".nav-mobile");
let register = document.querySelector(".register");

navMobile.addEventListener("click", function () {
    navMobile.style.display = "none";
    navTop.classList.add("active")
    navTop.style.display = 'block'
    navMobileClose.style.display = "block"
    register.classList.add('active')
    register.style.display = "flex"
})

navMobileClose.addEventListener("click", () => {
    navMobile.style.display = "flex";
    navTop.classList.remove("active")
    navTop.style.display = 'none'
    navMobileClose.style.display = "none"
    register.classList.remove('active')
    register.style.display = "none"
})