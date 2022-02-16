// EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
// SoftDev pd0
// K31 -- animation with JS
// 2022-02-15

var c = document.getElementById("playground");
var dotButton = document.getElementById("dotButton");
var stopButton = document.getElementById("stopButton");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue";


var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}


var radius = 0;
var growing = true;
var requestID = -1;

var drawDot = (e) => {

    if(requestID >= 0) return;
    else requestID = window.requestAnimationFrame(drawFrame);

}

var drawFrame = (e) => {
    clear(e);

    ctx.beginPath(); // this thingy resets the drawing so the circles aren't connected
    ctx.fillStyle = "red";
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();

    if(radius > 250) growing = false;
    else if(radius < 1) growing = true;

    if(growing) radius++;
    else radius--;

    requestID = window.requestAnimationFrame(drawFrame);
}

var stopIt = (e) => {
    console.log("stopIt invoked...")
    console.log(requestID );

    window.cancelAnimationFrame(requestID);
    requestID = -1;
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
