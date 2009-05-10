var __stake_names = {
  "Santa Monica Stake": 1,
  "Los Angeles Stake": 1,
  "Glendale Stake": 1
};
var __unit_names = {
  "Santa Monica 3rd": 1,
  "Los Angeles 1st": 1,
  "Glendale 7th": 1
};
function check_regex(reg, str) {
  return reg.test(str);
}
function is_valid_phone(phone) {
  var phone_regex = /^(\+\d)*\s*(\(?\d{3}\)?\s*)*\d{3}(-{0,1}|\s{0,1})\d{2}(-{0,1}|\s{0,1})\d{2}$/; 
  return check_regex(phone_regex, phone);
}
function is_valid_email(email) {
  var email_regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return check_regex(email_regex, email);
}
function is_valid_int(val) {
  return Math.floor(parseFloat(val)).toString() == val;
}
function SetError(error, error_id, error_text) {
  var error_node = document.getElementById(error_id);
  if (error) {
    error_node.innerHTML = error_text;
  } else {
    error_node.innerHTML = "";
  }
  return error;
}
