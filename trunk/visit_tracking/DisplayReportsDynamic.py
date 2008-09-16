#!/usr/bin/python

import Common
import HtmlReuse
import Sm3Ht
import DataModule

def FillEmptyMonths(ht_or_vt, assignment_reports):
  keys = assignment_reports.keys()
  for key in keys:
    l = len(assignment_reports[key])
    if l < 12:
      for i in xrange(12):
        if not assignment_reports[key].has_key(i):
          assignment_reports[key][i] = Sm3Ht.ReportInfo() 
    
def GetDictByAssignment(ht_or_vt, month_diff):
  assignment_reports = {}
  offset = month_diff
  reports = {}
  while offset > month_diff - 12:
    HtmlReuse.CalcDateOffset(offset)
    reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)
    for key in reports:
      if not assignment_reports.has_key(key):
        assignment_reports[key] = {}
      assignment_reports[key][11 - (month_diff - offset)] = reports[key]
    offset -= 1
  FillEmptyMonths(ht_or_vt, assignment_reports)
  return assignment_reports


def FillTeacherEmptyMonths(ht_or_vt, teachers):
  keys = teachers.keys()
  for key in keys:
    l = len(teachers[key])
    if l < 12:
      for i in xrange(12):
        if not teachers[key].has_key(i):
          teachers[key][i] = "not_reported"
    
def FillTeacherDictForMonth(ht_or_vt, offset, index, teachers):
  HtmlReuse.CalcDateOffset(offset)
  year = HtmlReuse.year
  month = HtmlReuse.month
  reports = DataModule.GetReports(ht_or_vt, year, month)
  assignments = DataModule.GetAssignments(ht_or_vt, year, month)
  for d in assignments:
    district = assignments[d]
    for c in district.companionships:
      comp = district.companionships[c]
      s = comp.senior_comp.first_name + " " + comp.senior_comp.last_name
      j = comp.junior_comp.first_name + " " + comp.junior_comp.last_name
      if not teachers.has_key(s):
        teachers[s] = {}
        teachers[j] = {}
      for teachee in comp.assignments:
        if reports[teachee.first_name + " " + teachee.last_name].visited:
          teachers[s][index] = "visited"
          teachers[j][index] = "visited"
 	  break
        elif reports[teachee.first_name + " " + teachee.last_name].reported:
          teachers[s][index] = "not_visited"
          teachers[j][index] = "not_visited"
      if not teachers[s].has_key(index):
        teachers[s][index] = "not_reported"
        teachers[j][index] = "not_reported"

def GetDictByTeacher(ht_or_vt, month_diff):
  teachers = {}
  for i in xrange(12):
    FillTeacherDictForMonth(ht_or_vt, month_diff - i, 11 - i, teachers)
  FillTeacherEmptyMonths(ht_or_vt, teachers)
  return teachers

def PrintTotalVisits(ht_or_vt, month_diff):
  HtmlReuse.CalcDateOffset(month_diff)
  reports = DataModule.GetReports(ht_or_vt, HtmlReuse.year, HtmlReuse.month)
  total_visits = 0
  for key in reports:
    if reports[key].visited:
      total_visits += 1

  print "Total visits for this month: %d" % total_visits

def PrintTableStyle():
  print (" table.r tr.rh td.le "
      "{border:1px red;border-style: solid none solid solid}")
  print (" table.r tr.rh td.re "
      "{border:1px red;border-style: solid solid solid none}")
  print (" table.r tr.rh td.not_reported "
      "{border:1px solid red}")
  print (" table.r tr.rh td.not_visited  "
      "{border:1px solid red}")
  print (" table.r tr.rh td.in_home "
      "{border:1px solid red}")
  print (" table.r tr.rh td.phone_call "
      "{border:1px solid red}")
  print (" table.r tr.rh td.letter "
      "{border:1px solid red}")



def PrintReport(ht_or_vt, report_type, month_diff):
  if report_type == "assignment":
    PrintReportByAssignment(ht_or_vt, month_diff)
  elif report_type == "teacher":
    PrintReportByTeacher(ht_or_vt, month_diff)

def PrintReportByAssignment(ht_or_vt, month_diff):
  rows = GetDictByAssignment(ht_or_vt, month_diff)
  print "<style type='text/css'>"
  print " table.r td.not_reported {background-color:#04f;padding:10px}"
  print " table.r td.not_visited  {background-color:#1aa;padding:10px}"
  print " table.r td.in_home      {background-color:#aaa;padding:10px}"
  print " table.r td.phone_call   {background-color:#333;padding:10px}"
  print " table.r td.letter       {background-color:#eee;padding:10px}"
  print " table.r td.other        {background-color:#fe0;padding:10px}"
  PrintTableStyle()
  print "</style>"
  print "<table class='r'>"
  print "<tr><td class='not_reported'></td><td>not reported</td>"
  print "<td class='not_visited'></td> <td>not visited</td>"
  print "<td class='in_home'></td>     <td>in home visit</td>"
  print "<td class='phone_call'></td>  <td>phone call</td>"
  print "<td class='letter'></td>      <td>letter</td>"
  print "<td class='other'></td>       <td>other</td></tr>"
  print "</table>"
  print "<br>"
  print "<table class='r'>"
  keys = rows.keys()
  keys.sort(lambda a,b: cmp(a.split(' ')[-1], b.split(' ')[-1]))
  for r in keys:
#    print "<tr onmouseover='this.className = \"rh\";' onmouseout='this.className = \"\";'>"
    print "<tr>" 
    print "<td class='le'>%s</td>" % r
    for m in rows[r]:
      col_class = "not_reported"
      report = rows[r][m]
      if report.visited:
        col_class = report.contact_type
      elif report.reported:
        col_class = "not_visited"
      print "<td class='%s'></td>" % (col_class)
    print "<td class='re'>%s</td>" % rows[r][rows[r].keys()[-1]].report_notes
    print "</tr>"
  print "</table>"

def PrintReportByTeacher(ht_or_vt, month_diff):
  rows = GetDictByTeacher(ht_or_vt, month_diff)
  print "<style type='text/css'>"
  print " table.r td.not_reported {background-color:#04f;padding:10px}"
  print " table.r td.not_visited  {background-color:#1aa;padding:10px}"
  print " table.r td.visited      {background-color:#aaa;padding:10px}"
  PrintTableStyle()
  print "</style>"
  print "<table class='r'>"
  print "<tr><td class='not_reported'></td><td>not reported</td>"
  print "<td class='not_visited'></td> <td>no visits</td>"
  print "<td class='visited'></td>     <td>made at least visit</td>"
  print "</table>"
  print "<br>"
  print "<table class='r'>"
  keys = rows.keys()
  keys.sort(lambda a,b: cmp(a.split(' ')[-1], b.split(' ')[-1]))
  for r in keys:
    print "<tr>"
    print "<td class='le'>%s</td>" % r
    for m in rows[r]:
      print "<td class='%s'></td>" % (rows[r][m])
    print "</tr>"
  print "</table>"
