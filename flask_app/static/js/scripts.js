
function getQuote() {
    fetch("http://api.quotable.io/random")
        .then(res => res.json())
        .then(data => {
            document.querySelector(".description side").innerHTML = `"${data.content}"`;
        })
}
getQuote()


window.onload = choosePic;

var myPix = new Array("/static/images/ali.png", "/static/images/sailor.jpg", "/static/images/bigjourney.jpg", "/static/images/inspiration.jpg", "/static/images/proud.png");

function choosePic() {
    var randomNum = Math.floor(Math.random() * myPix.length);
    console.log(randomNum)
    document.getElementById("myPicture").src = myPix[randomNum];
}

