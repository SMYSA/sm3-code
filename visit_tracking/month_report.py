#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import os
import sys
import HtmlReuse
import Common
import MonthReportDynamic
import DataModule


form = cgi.FieldStorage()

#
# Perform Authorization
#
Common.AuthorizePage(["hteacher", "vteacher", "htadmin", "vtadmin", "admin"])
ht_or_vt = Common.GetPageType(form)

#
#  Start HTML page
#
print "Content-Type: text/html"
print

if ht_or_vt == None:
  print "Don't know what type of page this is!"
  sys.exit(0)


print "<html>"
print "<head>"
print "<link rel='stylesheet' type='text/css' href='static/styles.css'></link>"
print "</head>"
print "<body>"

month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

assignments = DataModule.GetAssignments(ht_or_vt, HtmlReuse.year,
    HtmlReuse.month)
reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year,
    HtmlReuse.month)

#
#
#
print "<p align='center'><div align='center' style='text-align:center'>"
print "<h1>Santa Monica 3rd Ward<br>Home Teaching</h2>"
#print "<h2>%s</h2>" % HtmlReuse.DisplayDate()

HtmlReuse.PrintCal("month_report?group=%s" % ht_or_vt, month_diff)
if len(assignments) > 0:
  MonthReportDynamic.PrintHtml(ht_or_vt, assignments, reports,
      month_diff)
else:
  print "<h2>Assignments for this month have not been uploaded yet.</h2>"


print "</div></p></body>"
print "</html>"
