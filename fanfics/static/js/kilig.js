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

/* QUILL EDITOR FUNCTION */
document.addEventListener("DOMContentLoaded", function () {
  const editor = document.querySelector('#editor');
  const form = document.querySelector('#chapter-form');
  const hiddenInput = document.querySelector('#hidden-input');

  if (editor && form && hiddenInput) {
    const quill = new Quill('#editor', {
      theme: 'snow',
      modules: {
        toolbar: [['bold', 'italic', 'underline']]
      }
    });

    form.addEventListener("submit", function (e) {
      const content = quill.root.innerHTML;

      console.log("ENVIANDO:", content); // 🔥 DEBUG

      hiddenInput.value = content;

      // 🔥 força atualização antes de enviar
      if (!content || content === "<p><br></p>") {
        e.preventDefault();
        alert("Escreva algo antes de enviar!");
      }
    });
  } else {
    console.log("ERRO: editor ou form ou input não encontrado");
  }
});