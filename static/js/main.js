let linkButtons = document.getElementsByClassName("linkButton");

for (var i = 0; i < linkButtons.length; i++) {
    linkButtons[0].addEventListener("click", function() {
        fadeOutBody();
    });
}