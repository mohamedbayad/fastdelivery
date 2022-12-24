const inputCheckAll = document.querySelector("input[name='pickup-check-all']")
const AllInputCheck = document.querySelectorAll("input[name='pickup-check']")

inputCheckAll.addEventListener("click", () => {
    AllInputCheck.forEach(e => {
        if (e.checked == true) {
            e.checked = false
        } else {
            e.checked = true
        }
    })
})