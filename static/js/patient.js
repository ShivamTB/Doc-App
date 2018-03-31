$(function () {

  $(".js-create-patient").click(function () {
    var btn = $(this);  // <-- HERE
    $.ajax({
      url: btn.attr("data-url"),
      url: '/patient/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patient").modal("show");
      },
      success: function (data) {
        $("#modal-patient .modal-content").html(data.html_form);
      }
    });
  });

});

$("#modal-patient").on("submit", ".js-patient-create-form", function () {
  var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      if (data.form_is_valid) {
        alert("Patient created!");
        $("#patient-table tbody").html(data.html_patient_list);  // <-- Replace the table body
        $("#modal-patient").modal("hide");  // <-- Close the modal  // <-- This is just a placeholder for now for testing
      }
      else {
        $("#modal-patient .modal-content").html(data.html_form);
      }
    }
  });
  return false;
});

$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-patient").modal("show");
      },
      success: function (data) {
        $("#modal-patient .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#patient-table tbody").html(data.html_patient_list);
          $("#modal-patient").modal("hide");
        }
        else {
          $("#modal-patient .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create patient
  $(".js-create-patient").click(loadForm);
  $("#modal-patient").on("submit", ".js-patient-create-form", saveForm);

  // Update patient
  $("#patient-table").on("click", ".js-update-patient", loadForm);
  $("#modal-patient").on("submit", ".js-patient-update-form", saveForm);

  // Delete Patient
  $("#patient-table").on("click", ".js-delete-patient", loadForm);
 $("#modal-patient").on("submit", ".js-patient-delete-form", saveForm);

});
