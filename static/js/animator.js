function fadeOutBody(){
    let body = document.getElementsByTagName("body")[0];
    body.classList.remove("animated__fadeIn");
    body.classList.add("animate__fadeOut");
}