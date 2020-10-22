$('.linkButton').click(function(e) {
    $(document.body).toggleClass("animate__fadeIn");
    $(document.body).toggleClass("animate__fadeOut");
    e.preventDefault();
    if (this.href) {
        var target = this.href;
        setTimeout(function(){
            window.location = target;
        }, 500);
    }
});