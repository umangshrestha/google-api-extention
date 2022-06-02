let htmlFile = "index.html"
let settings = "toolbar=0,location=1,menubar=0,width=800,height=800,top=100,left=100"
document.getElementById("open")
    .addEventListener("click", () => window.open(htmlFile, '_blank', settings).focus())
window.open(htmlFile, '_blank', settings).focus();
