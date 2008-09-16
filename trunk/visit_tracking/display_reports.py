#!/usr/bin/python

import sys
import cgi
import cgitb; cgitb.enable()
import os
import HtmlReuse
import Common
import DisplayReportsDynamic

form = cgi.FieldStorage()

#
# Perform Authorization
#
Common.AuthorizePage(["htadmin", "vtadmin", "admin"])
ht_or_vt = Common.GetPageType(form)

#
#  Start HTML page
#
print "Content-Type: text/html"
print "Cache-Control: no-cache"
print

if ht_or_vt == None:
  print "Don't know what type of page this is!"
  sys.exit(0)


month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

report_type = "assignment"
if form.has_key("report_type"):
  report_type = form["report_type"].value


print "<html>"
print "<head>"
#print "<link rel='stylesheet' type='text/css' href='styles.css'></link>"
print "</head>"
print "<body>"
HtmlReuse.PrintCal("display_reports?group=%s&report_type=%s" % (ht_or_vt,
    report_type), month_diff)
print "<br>"
print "<div style='text-align:center'>"
DisplayReportsDynamic.PrintTotalVisits(ht_or_vt, month_diff)
print "<br>"
DisplayReportsDynamic.PrintTotalReported(ht_or_vt, month_diff)
print "</div>"
print ("<a href='display_reports?group=%s&chm=%d&report_type=assignment" %
    (ht_or_vt, month_diff) + "'>By Assignment</a>")
print ("<a href='display_reports?group=%s&chm=%d&report_type=teacher" %
    (ht_or_vt, month_diff) + "'>By Teacher</a>")
print "<br><br>"
DisplayReportsDynamic.PrintReport(ht_or_vt, report_type, month_diff)
print "</body>"
print "</html>"


