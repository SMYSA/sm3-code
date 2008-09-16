#!/usr/bin/python


def PrintHtml(ht_or_vt, districts, reports, month_diff):
  print "<table class='a'>"
  print "<tr>"
  for d in districts:
    print "<td class='dd'>District " + str(d) + "</td>"
  print "</tr>"
  print "<tr>"
  for d in districts:
    print "<td class='ll'>"
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
      print "<td><div class='f'>"
      print comps[c].senior_comp.first_name + " "
      print comps[c].senior_comp.last_name + "<br>"
      print comps[c].junior_comp.first_name + " "
      print comps[c].junior_comp.last_name + " "
      print "</div><div class='e'>"
      comp = comps[c].assignments
      for a in comp:
        name = a.first_name + " " + a.last_name
        print reports[name].visited and "&#x25cf;" or "&#x25cb;"
        print name
        print "<br>"
      print "</div></td>"
      print "</tr>"
    print "</table>"
  print "</tr>"
  print "</table>"
