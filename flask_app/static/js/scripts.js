
function getQuote() {
    fetch("http://api.quotable.io/random")
        .then(res => res.json())
        .then(data => {
            document.querySelector(".description side").innerHTML = `"${data.content}"`;
        })
}
getQuote()


window.onload = choosePic;

var myPix = new Array("static/images/harmony.png", "static/images/meditation.png", "static/images/MJDesign.png");

function choosePic() {
    var randomNum = Math.floor(Math.random() * myPix.length);
    document.getElementById("myPicture").src = myPix[randomNum];
}

choosePic()