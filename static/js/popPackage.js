const invoice = document.querySelectorAll(".invoice")
const packages = document.querySelectorAll(".packages")

packages.forEach((e) => {
    console.log(e.parentElement.id)
})
