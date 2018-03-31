jQuery(document).ready(function() {

	jQuery(".sidebar").on("click", "li", function() {
	  var patientID = jQuery(this).attr("data-patient-id");

	  fetchPatientInfo(patientID);
	});

	jQuery("form").on("submit", function(e) {
		e.preventDefault();
		var patientNumber = jQuery("#id_pat_number").val();
		var firstName = jQuery("#id_first_name").val();
		var surName = jQuery("#id_sur_name").val();

		// console.log(patientNumber + " | " + firstName + " | " + surName);

		if(patientNumber) {
			console.log("Perform Search with patient Number");
			fetchPatientInfo(patientNumber);
		}
	});


	//Full names : 
	jQuery("#id_first_name").on("keyup", function() {
	  var value = jQuery(this).val(); 
	  jQuery(".patient-card").each(function(i,el){
		var name = jQuery(el).find(".patient-name").text();
	    if(name.toLowerCase().indexOf(value.toLowerCase()) != -1) {
	      jQuery(el).parent().removeClass("hidden");
	    } else {
		  jQuery(el).parent().addClass("hidden");
	    }
	  });
	});

});

var genderMapper = {
	'M':'<i class="icon-male"></i>',
	'F':'<i class="icon-female"></i>',
}

function fetchPatientInfo(patientID) {
	$.ajax({
		type:'GET', 
		dataType:'json',
		url:"/patient/"+patientID+"/fetch/",
		beforeSend:function() {
			console.log("Fetching Info of Patient#"+patientID);
		}, success:function(response) {
			var response = JSON.parse(response);

			console.log(response[0]);

			if(typeof response[0] == 'object') {
				jQuery(".patient-info-container").removeClass("hidden");
				var infoContainer = jQuery(".patient-info-container");
				var response = response[0]['fields'];
				infoContainer.find(".patient-name").html(response['first_name'] + " " + response['sur_name']);
				infoContainer.find(".patient-sex").html(genderMapper[response['sex']]);
				infoContainer.find(".patient-number").html(response['pat_number']);
				// infoContainer.find(".patient-age").html(response['dob']);

				var dob = moment(response['dob']);
				var now = moment();

				var diff = moment.preciseDiff(dob, now, true); 

				infoContainer.find(".patient-age").html(diff['years'] + " yrs, " + diff['months']+" m" );
				// .html(JSON.stringify(response[0]['fields']));
			}

			
		}
	})
}