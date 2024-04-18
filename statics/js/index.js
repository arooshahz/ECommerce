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

let data = 0;
let data1 = 1;

//printing default value of data that is 0 in h2 tag
var counter = document.getElementById("counting");


if (counter){
counter.innerText = data;
}


//creation of increment function
function increment() {
    data = data + 1;
    document.getElementById("counting").innerText = data;
}
//creation of decrement function
function decrement() {
    data = data - 1;
    if (data<0){
        data=0;
    }
    document.getElementById("counting").innerText = data;
}



//var slider = document.getElementById("price-slider");
//var output = document.getElementById("filtered-price");
//output.innerHTML = slider.value;
//console.log(slider.value)
//
//// Update the current slider value (each time you drag the slider han
//const priceSlider = () => {
//  output.innerHTML = slider.value;
//}



function controlFromInput(fromSlider, fromInput, toInput, controlSlider) {
    const [from, to] = getParsed(fromInput, toInput);
    fillSlider(fromInput, toInput, '#C6C6C6', '#25daa5', controlSlider);
    if (from > to) {
        fromSlider.value = to;
        fromInput.innerText = to;
    } else {
        fromSlider.value = from;
    }
}

function controlToInput(toSlider, fromInput, toInput, controlSlider) {
    const [from, to] = getParsed(fromInput, toInput);
    fillSlider(fromInput, toInput, '#C6C6C6', '#008384', controlSlider);
    setToggleAccessible(toInput);
    if (from <= to) {
        toSlider.value = to;
        toInput.innerText = to;
    } else {
        toInput.innerText = from;
    }
}

function controlFromSlider(fromSlider, toSlider, fromInput) {
  const [from, to] = getParsed(fromSlider, toSlider);
  fillSlider(fromSlider, toSlider, '#C6C6C6', '#008384', toSlider);
  if (from > to) {
    fromSlider.value = to;
    fromInput.innerText = to;
  } else {
    fromInput.innerText = from;
  }
}

function controlToSlider(fromSlider, toSlider, toInput) {
  const [from, to] = getParsed(fromSlider, toSlider);
  fillSlider(fromSlider, toSlider, '#C6C6C6', '#008384', toSlider);
  setToggleAccessible(toSlider);
  if (from <= to) {
    toSlider.value = to;
    toInput.innerText = to;
  } else {
    toInput.innerText = from;
    toSlider.value = from;
  }
}

function getParsed(currentFrom, currentTo) {
  const from = parseInt(currentFrom.value, 10);
  const to = parseInt(currentTo.value, 10);
  return [from, to];
}

//function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
//    const rangeDistance = to.max-to.min;
//    const fromPosition = from.value - to.min;
//    const toPosition = to.value - to.min;
//    controlSlider.style.background = `linear-gradient(
//      to right,
//      ${sliderColor} 0%,
//      ${sliderColor} ${(fromPosition)/(rangeDistance)*100}%,
//      ${rangeColor} ${((fromPosition)/(rangeDistance))*100}%,
//      ${rangeColor} ${(toPosition)/(rangeDistance)*100}%,
//      ${sliderColor} ${(toPosition)/(rangeDistance)*100}%,
//      ${sliderColor} 100%)`;
//}

function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
    const rangeDistance = to.max - to.min;
    const fromPosition = from.value - to.min;
    const toPosition = to.value - to.min;

    // Calculate the percentage positions of the slider handles
    const fromPercentage = (fromPosition / rangeDistance) * 100;
    const toPercentage = (toPosition / rangeDistance) * 100;

    // Set gradient direction based on page direction
    const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
    let direction = 'to right';
    if (isRTL) {
        direction = 'to left';
    }

    // Set gradient stops based on direction
    let gradientStops = `${sliderColor} 0%, ${sliderColor} ${fromPercentage}%, ${rangeColor} ${fromPercentage}%, ${rangeColor} ${toPercentage}%, ${sliderColor} ${toPercentage}%, ${sliderColor} 100%`;

    // Apply gradient background to controlSlider
    controlSlider.style.background = `linear-gradient(${direction}, ${gradientStops})`;
}

function setToggleAccessible(currentTarget) {
  const toSlider = document.querySelector('#toSlider');
  if (Number(currentTarget.value) <= 0 ) {
    toSlider.style.zIndex = 2;
  } else {
    toSlider.style.zIndex = 0;
  }
}

const fromSlider = document.querySelector('#fromSlider');
const toSlider = document.querySelector('#toSlider');
const fromInput = document.querySelector('#fromInput');
const toInput = document.querySelector('#toInput');


fillSlider(fromSlider, toSlider, '#C6C6C6', '#008384', toSlider);

setToggleAccessible(toSlider);

fromSlider.oninput = () => controlFromSlider(fromSlider, toSlider, fromInput);
toSlider.oninput = () => controlToSlider(fromSlider, toSlider, toInput);
fromInput.oninput = () => controlFromInput(fromSlider, fromInput, toInput, toSlider);
toInput.oninput = () => controlToInput(toSlider, fromInput, toInput, toSlider);
