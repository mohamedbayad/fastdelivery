// services
let topHeader = document.querySelector('.top-header');
let scoter = document.getElementById("scoter");
let boxOne = document.getElementById('box-one');
let boxtwo = document.getElementById('box-two');
let boxThree = document.getElementById('box-three');

// button up 
const up = document.querySelector(".up")


window.onscroll = function() {
    const value = scrollY
    try {
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
    } catch (e) {
        
    }

    if (window.scrollY >= '500') {
        up.style.cssText = "transform: translateY(-80px);"
    } else {
        up.style.cssText = "transform: translateY(40px);"
    }

}

// action btn up 
up.addEventListener('click', _ => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});

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
};
