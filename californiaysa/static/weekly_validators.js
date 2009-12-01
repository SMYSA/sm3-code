__custom_ids = [
  "stake",
  "unit",
  "name",
  "email",
  "phone",
  "stake_ysa_visits"
];
__int_ids = [
  "less_active_visits",
  "renewed_temple_recommends",
  "reissued_temple_recommends",
  "first_time_temple_recommends",
  "temple_ordinances",
//  "endowments",
//  "sealings",
//  "initiatories",
//  "baptisms_confirmations",
  "family_file_names",
  "registered_voters"
];
function Validate() {
  document.report_form["submit_attempt"] = true;
  var has_error = false;
  var unit = document.getElementById('unit');
  var name = document.getElementById('name');
  var email = document.getElementById('email');
  var phone = document.getElementById('phone');

  has_error = SetError(unit.value == "",
    "unit_error",
    "Please enter a unit name");

  has_error = SetError(name.value == "",
    "name_error",
    "Please enter a name") || has_error;

  has_error = SetError(!is_valid_email(email.value),
    "email_error",
    "Please enter a valid email address") || has_error;
        
  has_error = SetError(!is_valid_phone(phone.value),
    "phone_error",
    "Please use this format: (xxx) xxx-xxxx") || has_error;

  for (var i = 0; i < __int_ids.length; i++) {
    var int_val = document.getElementById(__int_ids[i]);
    has_error = SetError(!is_valid_int(int_val.value),
                         int_val.id + "_error",
                         "Please enter a number (no decimals)") || has_error;
  }
  var submit_error = document.getElementById('submit_error');
  if (has_error) {
    submit_error.innerHTML = "There are errors above.";
  } else {
    submit_error.innerHTML = "";
  }
  return !has_error;
}
function MaybeValidate() {
  if (document.report_form["submit_attempt"]) {
    Validate();
  }
}
function AddStakeUnits() {
  var stakes = document.getElementById("stake_select");
//  var units = document.getElementById("unit_select");
  var units = null;
  AddSelectOptions(stakes, units);
}
function SetStakeFromUnit() {
  var stakes = document.getElementById("stake_select");
  var units = document.getElementById("unit_select");
  var stake_name = __units_to_stakes[units.options[units.selectedIndex].value];
  for (var i in stakes.options) {
    if (stake_name == stakes.options[i].value) {
      stakes.selectedIndex = i;
      return;
    }
  }
}
