let listsParent = document.querySelectorAll(".parent");
let childOl = document.querySelectorAll(".parent .child_ul");
let iconDrop = document.querySelectorAll(".drop");

let dropList = listsParent.forEach((e) => {
  e.addEventListener("click", () => {
    for (let i = 0; i < childOl.length; i++) {
      if (childOl[i].parentElement === e) {
        if (childOl[i].style.display != "block") {
          childOl[i].style.display = "block";
          iconDrop[i].classList.replace("fa-caret-right", "fa-caret-down");
        } else {
          iconDrop[i].classList.replace("fa-caret-down", "fa-caret-right");
          childOl[i].style.display = "none";
        }
      } else {
        iconDrop[i].classList.replace("fa-caret-down", "fa-caret-right");
        childOl[i].style.display = "none";
      }
    }
  });
});

// actions nav bar 
let btnNav = document.querySelector(".btn-nav");
let navBar = document.querySelector(".nav-bar");
let btnCloseNavBar = document.querySelector(".nav-close .bx");
btnNav.addEventListener("click", _ => {
  navBar.classList.add("active")
})
btnCloseNavBar.addEventListener("click", _ => {
  navBar.classList.remove("active")
})



// action settings and profile 
const profile = document.querySelector(".profile");
const ulProfile = document.querySelector(".ul-profile");

profile.addEventListener("click", () => {
  ulProfile.classList.toggle("active")
})


function settingTap() {
  let ulSetting = document.querySelector(".ul-setting");
  ulSetting.classList.toggle("active");

}

