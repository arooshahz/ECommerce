let stars = document.getElementsByClassName("star");

// Funtion to update rating
function gfg(n) {
  remove();
  for (let i = 0; i < n; i++) {
    if (n == 1) cls = "one";
    else if (n == 2) cls = "two";
    else if (n == 3) cls = "three";
    else if (n == 4) cls = "four";
    else if (n == 5) cls = "five";
    stars[i].className = "star " + cls;
  }
}

// To remove the pre-applied styling
function remove() {
  let i = 0;
  while (i < 5) {
    stars[i].className = "star";
    i++;
  }
}

// function changeLang(language) {
//   document.getElementById("lang").children[2].value = language.code;
//   document.getElementById("lang").submit();
//   if (language.code === "fa") {
//     document.getRootNode().children[0].dir = "rtl";
//   } else {
//     document.getRootNode().children[0].dir = "ltr";
//   }
// }