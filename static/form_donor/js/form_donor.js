$(document).ready(function() {
	$("#warning_alert").hide();
	$("#alert_close").click(function(e){
		e.preventDefault();
		$("#warning_alert").hide();
	});
			
	$("#id_nomor_induk").keyup(function(){
		if($(this).val().length != 16){
			$("#p1").html("NIK harus terdiri dari 16 angka");
		}
		else{
			$("#p1").html("");
		}
	});
			
	$("#form_donor").on("submit", function(e) {
		e.preventDefault();
		var formData = new FormData($("#form_donor")[0]);
		$.ajax({
			type: "POST",
			url: "",
			data: formData,
			processData: false,
           	contentType: false,
			success: function (data) {
				if(data["status"] == "error"){
					var msg = "";
					for(const k in data["msg"]){
						msg += "<li>"+data["msg"][k][0]+"</li>";
					}
					$("#alert_msg").html(msg);
					$("#warning_alert").show();
					window.scrollTo(0,0);
				}
				else{
					var modal =  new bootstrap.Modal(document.getElementById("modal_success"),{keyboard:false, backdrop:"static"});
					modal.show();
					$("#btn-success-modal").click(function(e){
						window.location = "/dashboard-donor/";
					});
				}
			}
		});
	});
});