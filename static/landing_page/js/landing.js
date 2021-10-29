function getPercentage(a, totalUser) {
  if (totalUser < 1) {
    return 0;
  }
  var percentage = 100 * a / totalUser;
  return String(percentage);
}


function refreshCounter() {
  $.ajax({
    type: 'GET',
    url: 'get_count',
    dataType: 'json',
    success: function(data) {
      var donorPercentage = getPercentage(data.donor_count, data.user_count);
      $("#donor-bar").css("width", donorPercentage+"%");
      $("#donor-bar").attr("aria-valuenow", donorPercentage);
    
      var recipientPercentage = getPercentage(data.recipient_count, data.user_count);
      $("#recipient-bar").css("width", recipientPercentage+"%");
      $("#recipient-bar").attr("aria-valuenow", recipientPercentage);

      $(".users-count").text(data.user_count);
      $("#donor-count").text(data.donor_count);
      $("#recipient-count").text(data.recipient_count);
    },
    error: function() {
      console.log("Error");
    },
    complete: function() {
      setTimeout(refreshCounter, 60000);
    }
  });
}



$(document).ready(function() {
  $(".carousel-inner").children(":first").addClass("active");
  
  refreshCounter();
});