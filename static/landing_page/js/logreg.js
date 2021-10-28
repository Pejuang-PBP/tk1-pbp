$(document).ready(function(){		
  $('.show-hide').click(function(){
      var input = $(this).parent().children("input");
      if (input.attr("type") == "password") {
          input.attr("type", "text");
          $(this).removeClass("bi-eye-slash").addClass("bi-eye");
      } else {
        input.attr("type", "password");
        $(this).removeClass("bi-eye").addClass("bi-eye-slash");
      }
  });
});