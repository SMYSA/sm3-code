#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import os
import HtmlReuse
import Common
import ReportAssignmentDynamic
import DataModule

form = cgi.FieldStorage()

#
# Perform Authorization
#
Common.AuthorizePage(["hteacher", "vteacher", "htadmin", "vtadmin", "admin"])
ht_or_vt = Common.GetPageType(form)

#
#
#
print "Content-Type: text/html"
print "Cache-Control: no-cache"
print

if ht_or_vt == None:
  print "Don't know what type of page this is!"
  sys.exit(0)

print " ".join(open("shtml/template_header.shtml","r").readlines())

month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

d = -1
c = -1
if form.has_key("d"):
  d = int(form["d"].value)
if form.has_key("c"):
  c = int(form["c"].value)

assignments = DataModule.GetAssignments(ht_or_vt, HtmlReuse.year,
                                        HtmlReuse.month)
reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)

#
#
#
print " ".join(open("shtml/template1.shtml","r").readlines())
HtmlReuse.PrintCal(
    "report_assignment?group=%s&d=%d&c=%d" % (ht_or_vt, d, c), month_diff)
print " ".join(open("shtml/template2.shtml","r").readlines())
if len(assignments) > 0 and d != -1 and c != -1:
  ReportAssignmentDynamic.PrintHtml(d, c, ht_or_vt, assignments,
      reports, month_diff)
else:
  print "<h2>Assignments for this month have not been uploaded yet.</h2>"
print " ".join(open("shtml/template4.shtml","r").readlines())


print " ".join(open("shtml/template_footer.shtml","r").readlines())
