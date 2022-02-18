// ELs :: Ella Krechmer, Lucas Lee
// SoftDev pd0
// K32 -- screen saver
// 2022-02-17

var c = document.getElementById("playground");
var dotButton = document.getElementById("dotButton");
var dvdButton = document.getElementById("dvdButton");
var stopButton = document.getElementById("stopButton");

var ctx = c.getContext("2d");
ctx.fillStyle = "red";


var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}


var radius = 0;
var growing = true;
var requestID = -1;

var img = new Image();
img.src = "logo_dvd.jpg";


var imgWidth = 60;
var imgHeight = 40;
var x = c.width/2;
var y = c.height/2;
var dx = 5;
var dy = 5;

var drawDot = (e) => {

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);

    clear(e);

    ctx.beginPath(); // this thingy resets the drawing so the circles aren't connected
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();

    if(radius > 250) growing = false;
    else if(radius < 1) growing = true;

    if(growing) radius++;
    else radius--;


}

var stopIt = (e) => {
    console.log("stopIt invoked...")
    console.log(requestID );

    window.cancelAnimationFrame(requestID);
    requestID = -1;
}

var startDvd = (e) =>{
    x = Math.floor(Math.random() * (c.width - imgWidth));
    y = Math.floor(Math.random() * (c.height - imgHeight));

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDvd);
}


var drawDvd = (e) => {

    console.log(x, y);

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDvd);

    clear(e);
    ctx.drawImage(img, x, y, imgWidth, imgHeight);



    if(x + imgWidth >= c.width || x <= 0){
        if(x + imgWidth > c.width) x = c.width - imgWidth;
        if(x < 0) x = 0;
        dx = -dx;
    }
    if(y + imgHeight >= c.height || y <= 0){
        if(y + imgHeight > c.height) y = c.height - imgHeight;
        if(y < 0) y = 0;
        dy = -dy;
    }

    x += dx;
    y += dy;
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", startDvd);
stopButton.addEventListener("click", stopIt);
