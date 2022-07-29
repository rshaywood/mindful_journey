
var getQuote=async()=>{
    var request=await fetch("http://api.quotable.io/random")
    var response= await request.json();
    console.log(response);document.querySelector(".quote").innerHTML=`"${response.content}"`;
    console.log(response);document.querySelector(".author").innerHTML=`By:${response.author}`;

}
getQuote();


window.onload = choosePic;

var myPix = new Array("/static/images/ali.png", "/static/images/sailor.jpg", "/static/images/bigjourney.jpg", "/static/images/inspiration.jpg", "/static/images/proud.png");

function choosePic() {
    var randomNum = Math.floor(Math.random() * myPix.length);
    console.log(randomNum)
    document.getElementById("myPicture").src = myPix[randomNum];
}

// script for dropdown box in add and edit forms
$(document).ready(function(e) {
    try {
    $("body select").msDropDown();
    } catch(e) {
    alert(e.message);
    }
    });




