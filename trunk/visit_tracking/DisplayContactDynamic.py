#!/usr/bin/python

def PrintHtml(d, c, ht_or_vt, districts, reports, month_diff):
  cell_style = "style='font:9pt arial, sans-serif;padding:0 3 0 3'"
  try:
    comp = districts[d].companionships[c]
  except:
    print "<div style='horizontal-align:center'>"
    print "This companionship did not exist this month"
    print "</div>"
    return

  print "<div id='f'>"
  print "<table style='margin: 0 auto'>"
  print "<tr><td style='font-weight:bold'>Teachers</td></tr>"
  print "<tr><td %s>%s</td><td %s>%s</td></tr>" % (
    cell_style, comp.senior_comp.first_name + " " + comp.senior_comp.last_name,
    cell_style, comp.senior_comp.phone)
  print "<tr><td %s>%s</td><td %s>%s</td></tr>" % (
    cell_style, comp.junior_comp.first_name + " " + comp.junior_comp.last_name,
    cell_style, comp.junior_comp.phone)
  print "<tr><td style='font-weight:bold'>Teachees</td></tr>"
  for i in xrange(len(comp.assignments)):
    a = comp.assignments[i];
    name = a.first_name + " " + a.last_name
    print "<tr><td %s>%s</td><td %s>%s</td><td %s>%s</td></tr>" % (
      cell_style, name, cell_style, comp.assignments[i].phone,
      cell_style, comp.assignments[i].email)
  print "</table>"
  print "</div>"
