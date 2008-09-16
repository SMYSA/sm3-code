#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import os
import HtmlReuse
import Common
import DisplayAssignmentsDynamic
import DataModule

def UpdateReportInfo(ht_or_vt, teachee, reporter, visited, comment,
    contact_type):
  reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)

  r = reports[teachee]
  r.visited = visited
  r.reported = True
  r.report_notes = comment
  r.reported_by  = reporter
  r.contact_type = contact_type

  DataModule.PutReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month, reports)


#print "Content-Type: text/html\n\n"
#print "<html>"
#print "<head>"
#print "<link rel='stylesheet' type='text/css' href='styles.css'></link>"
#print "</head>"
#print "<body>"

#
# This environment variable should be set when using BASIC HTTP Authentication
#
if os.environ.has_key("REMOTE_USER"):
  print "<h2>%s</h2>" % os.environ["REMOTE_USER"]

form = cgi.FieldStorage()

month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

ht_or_vt = None
if not form.has_key("group"):
  Common.PrintRedirect("302", "index.html")
  sys.exit(0)
else:
  ht_or_vt = form["group"].value 

#for key in form.keys():
#  print key + ": " + form[key].value
#  print "<br>"

t  = form["teachee"].value
r  = form["reporter"].value
v  = form["visited"].value == "Y"
rt = form["report"].value
d  = form["d"].value
c  = form["c"].value
ct = form["contact_type"].value
#print v
#print "<br>"

UpdateReportInfo(ht_or_vt, t, r, v, rt, ct)
#Redirect("report_assignment?group=%s&d=%s&c=%s" % (ht_or_vt, d, c))
Common.PrintRedirect("302", "report_assignment?group=%s&d=%s&c=%s&chm=%d"
    % (ht_or_vt, d, c, month_diff))
  
#print "</body>"
#print "</html>"


