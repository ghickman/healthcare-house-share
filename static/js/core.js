$(function() {
  var picker;
  if ($('#id_available_date').length > 0) {
    return picker = new Pikaday({
      field: document.getElementById('id_available_date')
    });
  }
});
