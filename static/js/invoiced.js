const packages = document.getElementsByClassName("packages");

for (let i = 0; i < packages.length; i++) {
    packages[i].addEventListener("click", _ => {
        console.log(packages[i].parentElement.parentElement.id)
    })
}
