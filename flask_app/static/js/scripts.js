
function getQuote() {
    fetch("http://api.quotable.io/random")
        .then(res => res.json())
        .then(data => {
            document.querySelector(".description side").innerHTML = `"${data.content}"`;
        })
}
getQuote()


window.onload = choosePic;

var myPix = new Array("/static/images/ali.png", "/static/images/sailor.webp", "/static/images/bigjourney.jpg", "/static/images/inspiration.jpg", "/static/images/proud.png");

function choosePic() {
    var randomNum = Math.floor(Math.random() * myPix.length);
    document.getElementById("myPicture").src = myPix[randomNum];
}

