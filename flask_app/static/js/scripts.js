
function getQuote(){
    fetch("http://api.quotable.io/random")
    .then(res=>res.json())
    .then(data=>{
        document.querySelector(".description side").innerHTML=`"${data.content}"`;
    })
}
getQuote()


