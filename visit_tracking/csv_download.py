#!/usr/bin/python

import cgi
import os
import sys
import HtmlReuse
import Sm3Ht
import Common
import DataModule

def PrintCsvReports(ht_or_vt):
  import csv
  districts = DataModule.GetAssignments(ht_or_vt,
                                       HtmlReuse.year,
                                       HtmlReuse.month)
  reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)
  writer = csv.writer(sys.stdout)
  writer.writerow(["Name",
		   "Visited",
		   "Reported",
		   "Reported By",
		   "Report Notes",
		   "Contact Type",
		   "Senior Companion",
		   "Junior Companion"])

  for d in districts:
    comps = districts[d].companionships
    for c in comps:
      as = comps[c].assignments
      for a in as:
        name = a.first_name + " " + a.last_name
        if reports.has_key(name):
          report = reports[name]
        else:
          report = Sm3Ht.ReportInfo()
        
        writer.writerow([name,
			 report.visited,
			 report.reported,
			 report.reported_by,
			 report.report_notes,
			 report.contact_types,
			 comps[c].senior_comp.first_name + " " +
			 comps[c].senior_comp.last_name,
			 comps[c].junior_comp.first_name + " " +
			 comps[c].junior_comp.last_name])
                     


form = cgi.FieldStorage()

#
# Perform Authorization
#
Common.AuthorizePage(["htadmin", "vtadmin", "admin"])
ht_or_vt = Common.GetPageType(form)


if ht_or_vt == None:
  print "Content-Type: text/html"
  print
  print "<html>"
  print "<body>"
  print "Don't know what type of page this is!"
  sys.exit(0)


month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

if form.has_key("action") and form["action"].value == "download":
  print "Content-Type: application/csv"
  print ("Content-Disposition: \"attachment; "
      "filename=sm3_home_teaching_%s-%s.csv\"" % (HtmlReuse.month,
	                                          HtmlReuse.year))
#  print "Content-Type: text/html"
  print
  PrintCsvReports(ht_or_vt)
  sys.exit(0)
elif form.has_key("action"):
  print form["action"].value


#
#  Start HTML page
#
print "Content-Type: text/html"
print
print "<html>"
print "<body>"

#
#
#
HtmlReuse.PrintCal("csv_download?group=%s" % ht_or_vt, month_diff)
print "<br/><br/>"

print "<a href='csv_download?group%s&chm=%s&action=download'>download</a>" % (
    ht_or_vt,
    month_diff)

print "</body>"
print "</html>"
