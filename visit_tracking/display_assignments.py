#!/usr/bin/python

import cgi
import os
import sys

import Common
import DisplayAssignmentsDynamic
import DataModule
import HtmlReuse

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

print " ".join(open("shtml/template_header.shtml","r").readlines())

month_diff = 0
if form.has_key("chm"):
  month_diff = int(form["chm"].value)
  HtmlReuse.CalcDateOffset(month_diff)

assignments = DataModule.GetAssignments(ht_or_vt, HtmlReuse.year,
                                        HtmlReuse.month)

#
#
#
print " ".join(open("shtml/template1.shtml","r").readlines())
HtmlReuse.PrintCal("display_assignments?group=%s" % ht_or_vt, month_diff)
print " ".join(open("shtml/template2.shtml","r").readlines())
if len(assignments) > 0:
  pass
  DisplayAssignmentsDynamic.PrintHtml(ht_or_vt, assignments, month_diff)
else:
  print "<h2>Assignments for this month have not been uploaded yet.</h2>"
print " ".join(open("shtml/template4.shtml","r").readlines())


print " ".join(open("shtml/template_footer.shtml","r").readlines())
