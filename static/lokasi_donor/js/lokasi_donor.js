$(document).ready(function () {
   $("#clickHelp").click(function () {
     if ($("#divHelp").html() == "") {
       $("#divHelp").load("include");
     } else {
       $("#divHelp").html("");
     }
   });
 });