#!/usr/bin/python

import cgi
import os
import sys
import HtmlReuse
import Sm3Ht
import Common
import DataModule

def StubReportInfo(ht_or_vt, districts):
  reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)

  for d in districts:
    comps = districts[d].companionships
    for c in comps:
      as = comps[c].assignments
      for a in as:
        name = a.first_name + " " + a.last_name
        if not reports.has_key(name):
          reports[name] = Sm3Ht.ReportInfo()

  DataModule.PutReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month, reports)

def ReplaceHtAssignments(ht_or_vt):
  sm3_ht = Sm3Ht.SM3HomeTeaching(form["membership_file"].value.split("\n"))
  districts = sm3_ht.GetHTDistricts()
  DataModule.PutAssignments(ht_or_vt, HtmlReuse.year, HtmlReuse.month,
                            districts)
  return districts


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
print

if ht_or_vt == None:
  print "Don't know what type of page this is!"
  sys.exit(0)


print "<html>"
print "<body>"

month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

if form.has_key("action") and form["action"].value == "process_file":
  districts = ReplaceHtAssignments(ht_or_vt)
  StubReportInfo(ht_or_vt, districts)
  print "<h3>Upload Successful</h3>" 
elif form.has_key("action"):
  print form["action"].value

#
#
#
print "<a href=display_reports?group=%s>Click here </a>" % ht_or_vt
print "if you want to see the report page"
print "<br/><br/>"
HtmlReuse.PrintCal("upload?group=%s" % ht_or_vt, month_diff)
print "<br/><br/>"

print ("<form action='upload' method='post'" +
   " enctype='multipart/form-data'>")
print "file: <input type='file' name='membership_file'/> <br/>" 
print "<input type='submit' value='upload'/>"
print "<input type='hidden' name='action' value='process_file'/>"
print "<input type='hidden' name='chm' value='%d'/>" % month_diff
print "<input type='hidden' name='group' value='%s'/>" % ht_or_vt
print "</form>"

print "</body>"
print "</html>"
