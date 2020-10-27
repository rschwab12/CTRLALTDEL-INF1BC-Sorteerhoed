$('.answer-box').click(function() {
    $("#user-answer").val($(this).data("answer"));

    setTimeout(function(){
        $("#answer-form").submit();
    }, 500);

    $("#question-body").toggleClass("animate__fadeIn");
    $("#question-body").toggleClass("animate__fadeOut");

});
