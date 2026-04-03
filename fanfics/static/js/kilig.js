src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"
src="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700,700italic,400italic"


/*OPEN FANFICS BY CLICKING ON THE CARD*/
    function openFanfic(id){
    window.location.href = "/fanfic/" + id
}

/*FILTER FUNCTION*/
const btn = document.getElementById("filter-btn")
const dropdown = document.getElementById("filter-dropdown")

btn.addEventListener("click", () => {
    dropdown.classList.toggle("hidden")
})

function removeFilter(name){
    const url = new URL(window.location.href)
    url.searchParams.delete(name)
    window.location.href = url.toString()
}
    
/*FUNCTION TO OPEN DROPDOWN MENU UNDER USER AVATAR WHEN THEY ARE LOGGED IN*/
function toggleMenu() {
  const menu = document.getElementById("dropdown-profile");
  menu.style.display = menu.style.display === "block" ? "none" : "block";
}

document.addEventListener("click", function(event) {
  const menu = document.getElementById("dropdown-profile");
  const avatar = document.querySelector(".avatar");

  if (!avatar.contains(event.target) && !menu.contains(event.target)) {
    menu.style.display = "none";
  }
});

            /*BUTTERFLY*/
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";

  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }

  return color;
}

function changeColor() {
  const color = getRandomColor();

  const moth = document.getElementById("shape-moth");
  const main = moth.querySelector("#main");

  if (main) {
    main.style.fill = color;
  }
}
