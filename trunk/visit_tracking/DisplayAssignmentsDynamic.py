#!/usr/bin/python

def PrintHtml(ht_or_vt, districts, month_diff):
  print ("Please click your companionship to see your assignment " +
      "or submit a report.")
  print "<table class='a'>"
  print "<tr>"
  for d in districts:
    print "<td class='d'>District " + str(d) + "</td>"
  print "</tr>"
  print "<tr>"
  for d in districts:
    print "<td class='l'>"
    print districts[d].supervisor.first_name + " "
    print districts[d].supervisor.last_name + " "
    print "</td>"
  print "</tr>"
  print "<tr>"
  for d in districts:
    print "<td valign='top'>"
    print "<table class='a' cellspacing=1 cellpadding=2>"
    comps = districts[d].companionships;
    for c in comps:
      print "<tr>"
      print ("<td><div class='c' onclick='window.location=" +
          "\"report_assignment?group=%s&d=%s&c=%d&chm=%d\"'>" % 
          (ht_or_vt, d, c, month_diff))
      print comps[c].senior_comp.first_name + " "
      print comps[c].senior_comp.last_name + "<br>"
      print comps[c].junior_comp.first_name + " "
      print comps[c].junior_comp.last_name + " "
      print "</div></td>"
      print "</tr>"
    print "</table>"
  print "</tr>"
  print "</table>"
