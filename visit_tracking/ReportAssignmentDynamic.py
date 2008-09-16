#!/usr/bin/python

def PrintValidateFuncs():
  print "<script type='text/javascript'>"
  print "function el(id) {"
  print "  return document.getElementById(id);"
  print "}"
  print "function empty(s) {"
  print "  return s.replace(/Spiritual:|Temporal:|\s/g, '').length == 0;"
  print "}"
  print "function clear(id) {"
  print "  el(id).innerHTML = '';"
  print "}"
  print "var form_submitted = false;"
  print "function validate(form) {"
  print "  try {"
  print "  if (!form_submitted) {"
  print "    var e = el('error');"
  print "    var teachee;"
  print "    var reporter;"
  print "    var contact_type;"
  print "    for (var i = 0; i < form.teachee.length; ++i) {"
  print "      if (form.teachee[i].checked) teachee = 1;"
  print "    }"
  print "    for (var i = 0; i < form.reporter.length; ++i) {"
  print "      if (form.reporter[i].checked) reporter = 1;"
  print "    }"
  print "    for (var i = 0; i < form.contact_type.length; ++i) {"
  print "      if (form.contact_type[i].checked) contact_type = 1;"
  print "    }"
  print "    if (!teachee) {"
  print "      e.innerHTML = 'Please select a teachee.';"
  print "    }"
  print "    else if (!form.visited[0].checked && !form.visited[1].checked) {"
  print "      e.innerHTML = 'Please select Yes or No.';"
  print "      form.visited[0].focus();"
  print "    }"
  print "    else if (!contact_type) {"
  print "      e.innerHTML = 'Please choose a type of contact.';"
  print "      form.contact_type[0].focus();"
  print "    }"
  print "    else if (empty(form.report.value)) {"
  print "      e.innerHTML = 'Please enter a brief report.';"
  print "      form.report.select();"
  print "    }"
  print "    else if (!reporter) {"
  print "      e.innerHTML = 'Please select a reporter.';"
  print "      form.reporter[0].focus();"
  print "    } else {"
  print "      e.innerHTML = '';"
  print "      form.method = 'POST';"
  print "      form.action = 'record_report';"
  print "      form.submit();"
  print "      return (form_submitted = true);"
  print "    }"
  print "  }"
  print "  setTimeout('clear(\"error\")', 2000);"
  print "  return false;"
  print "  } catch (err) {"
  print "    e.innerHTML = err.description;"
  print "  }"
  print "  return false;"
  print "}"
  print "</script>"

def PrintHtml(d, c, ht_or_vt, districts, reports, month_diff):
  PrintValidateFuncs()
  print "<div id='f'>"
  print "<form onsubmit='return validate(this);'>"
  print "<input type='hidden' name='group' value='%s'>" % ht_or_vt
  print "<input type='hidden' name='d' value='%d'>" % d
  print "<input type='hidden' name='c' value='%d'>" % c
  print "<input type='hidden' name='chm' value='%d'>" % month_diff
  print "<div>Who is this report for?</div>"
  print "<div class='rg'>"
  print "<table cellpadding=0 cellspacing=0>"
  comp = districts[d].companionships[c];
  for i in xrange(len(comp.assignments)):
    a = comp.assignments[i];
    name = a.first_name + " " + a.last_name
    print "<tr " + ((i&1) and " " or "class='o'") + ">"
    print ("<td><input type=radio id='ee" + str(i) + "' name='teachee' value='"
        + name + "'</td>")
    print "<td>" + name + "</td>"
    print ("<td class='t" + (reports[name].reported and " u'>report received" or
          "'>not yet reported") + "</td>")
    print "</tr>"
  print "</table>"
  print "</div>"
  print "<div>Did you visit this person this month?</div>"
  print "<div class='rg'>"
  print "<input type='radio' id='ry' name='visited' value='Y'>Yes<br>"
  print "<input type='radio' id='rn' name='visited' value='N'>No<br>"
  print "</div>"
  print "<div>What type of contact did you have with this person?</div>"
  print "<div>"
  print ("<input type='radio' id='none' name='contact_type' "
      "value='none'>None<br>")
  print ("<input type='radio' id='ih' name='contact_type' "
      "value='in_home'>In Home<br>")
  print ("<input type='radio' id='pc' name='contact_type' "
      "value='phone_call'>Phone Call<br>")
  print ("<input type='radio' id='lt' name='contact_type' "
      "value='letter'>Letter<br>")
  print ("<input type='radio' id='ot' name='contact_type' "
      "value='other'>Other<br>")
  print "</div>"
  print "<div style='width:80%'>"
  print ("Please enter a few sentences about this person, their current " +
      "circumstances and any needs they may have.  These comments are " +
      "confidential and will be viewed only by your supervisor, the EQ " +
      "presidency, and the bishopric.  They are critical in helping these " +
      "leaders meet the needs of those they lead.  If you were unable to " +
      "visit this person, please explain why.  For pressing needs or " +
      "emergencies, please contact your leaders directly.<br>")
  print "</div>"
  print "<textarea rows=7 style='width:80%' name='report'>"
  print "Spiritual:\n\n"
  print "Temporal:\n\n"
  print "Social:"
  print "</textarea>"
  print "<div style='padding:6 0 0'>Reported by:</div>"
  print "<div class='rg'>"
  name = comp.senior_comp.first_name + " " + comp.senior_comp.last_name
  print ("<input type='radio' name='reporter' value='" + name + "'>" +
      name + "<br>")
  name = comp.junior_comp.first_name + " " + comp.junior_comp.last_name
  print ("<input type='radio' name='reporter' value='" + name + "'>" +
      name + "<br>")
  print ("<input type='radio' name='reporter' value='supervisor'>supervisor" +
      "<br>")
  print "</div>"
  print "<input type='submit' value='Submit'>"
  print "<span id='error'></span>"
  print "</form>"
  print "<p><a href='contact?group=%s&d=%d&c=%d&chm=%d'>This Assignment " % (
    ht_or_vt, d, c, month_diff)
  print "with Contact Info</a></p>"
  print "<p><a href='display_assignments?group=%s&chm=%d'>" % (
    ht_or_vt, month_diff)
  print "Back to All Assignments</a></p>"
  print "</div>"
