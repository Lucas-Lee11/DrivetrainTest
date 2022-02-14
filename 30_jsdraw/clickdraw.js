// EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
// SoftDev pd0
// K30 -- canvas with JS
// 2022-02-014

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
    console.log("toggle");
    if(mode === "rect") mode = "circ";
    else mode = "rect";
}

var drawRect = (e) => {
    console.log("draw rect");
    mouseX = e.offsetX;
    mouseY = e.offsetY;
    ctx.strokeStyle = "red";
    ctx.strokeRect(mouseX, mouseY, 50, 10);
}

var drawCircle = (e) => {
    console.log("draw circ");
    mouseX = e.offsetX;
    mouseY = e.offsetY;
    ctx.strokeStyle = "red";
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI);
}

var draw = (e) => {
    console.log("drawing");
    mode === "rect" ? drawRect(e) : drawCircle(e);
}

var wipe = (e) => {
    console.log("wipe");
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipe);
