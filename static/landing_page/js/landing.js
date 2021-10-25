var allSlide = document.getElementsByClassName("carousel-inner")[0].childNodes

for (var i = 0; i < allSlide.length; i++) {
    if (allSlide[i].nodeType == 1) {
      allSlide[i].classList.add("active");
      break;
    }        
}