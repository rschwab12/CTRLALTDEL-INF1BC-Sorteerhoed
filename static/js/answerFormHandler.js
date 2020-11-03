$('.answer-box').click(function() {
    $("#user-answer").val($(this).data("answer"));

    setTimeout(function(){
        $("#answer-form").submit();
    }, 500);

    $("#question-text").toggleClass("animate__fadeIn");
    $("#answer-buttons").toggleClass("animate__fadeIn");

    $("#question-text").toggleClass("animate__fadeOut");
    $("#answer-buttons").toggleClass("animate__fadeOut");
});
