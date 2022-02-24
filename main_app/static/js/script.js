// Variables

const dateEl = document.getElementById("id_date");
const selectEl = document.getElementById("id_fill");

// Date Picker Animation

M.Datepicker.init(dateEl, {
  format: "yyyy-mm-dd",
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true,
});

// Select Widget Animation

M.FormSelect.init(selectEl);
