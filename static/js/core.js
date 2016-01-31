var checkAvailabilityDates, from, to;

from = null;

to = null;

$(function() {
  var picker;
  if ($('#id_available_date').length > 0) {
    picker = new Pikaday({
      field: document.getElementById('id_available_date')
    });
  }
  if ($('#availability_from').length > 0) {
    from = new Pikaday({
      field: document.getElementById('availability_from'),
      defaultDate: moment().toDate(),
      minDate: moment().toDate()
    });
    $('#availability_from').change(checkAvailabilityDates);
  }
  if ($('#availability_to').length > 0) {
    to = new Pikaday({
      field: document.getElementById('availability_to'),
      defaultDate: moment().toDate(),
      minDate: moment().toDate()
    });
    $('#availability_to').change(checkAvailabilityDates);
  }
  if ($('.js-advanced-toggle').length > 0) {
    $('.js-advanced-toggle').click(function() {
      $('.js-advanced-search').slideToggle();
    });
  }
});

checkAvailabilityDates = function() {
  var fromDate, toDate;
  to.minDate = from.toString();
  fromDate = moment(from.toString());
  toDate = moment(to.toString());
  if (toDate < fromDate) {
    to.setDate(fromDate.toString());
  }
};
