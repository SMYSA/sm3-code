#!/usr/bin/python

import time

(year, month) = time.localtime(time.time())[:2]

def CalcDateOffset(month_diff):
  global year, month
  (year, month) = time.localtime(time.time())[:2]
  if month_diff + month < 0:
    year  = year - abs((month_diff + month) / 12)
    month = (month_diff + month) % 12
  else:
    year  = year + abs((month_diff + month) / 12)
    month = (month + month_diff) % 12
  if month == 0:
    month = 12
    year = year - 1

def DisplayDate():
  return time.strftime("%b %Y", (year, month, 0,0,0,0,0,0,0))

def PrintCal(address, month_diff):
  CalcDateOffset(month_diff)
  if address.find("?") == -1:
    address = address + "?"
  else:
    address = address + "&"
  display_date = DisplayDate()
  print (
    "<table border='1'  bordercolor='#FFFF00' cellspacing='1' " +
    "cellpadding='0' align='center'>" +
    "<tr><td align='center'>" +
    "<table cellspacing='0' cellpadding='0' align=center width='100' " +
    "border='1'>" +
#    "<tr><td  align=center bgcolor='#ff0000'>" +
    "<tr><td  align=center>" +
    "<font size='3' face='Tahoma'>" +
    "<a href='%schm=%d'>&lt;&lt;</a>" +
    "</font></td>" +
#    "<td colspan=5 align=center bgcolor='#ff0000'>" +
    "<td colspan=5 align=center>" +
    "<font size='3' face='Tahoma'>%s</font></td>" +
#    "<td  align=center bgcolor='#ffff00'>" +
    "<td  align=center>" +
    "<font size='3' face='Tahoma'>" +
    "<a href='%schm=%d'>&gt;&gt;</a></font></td>" +
    "</tr></table></td></tr></table>") % (
      address, (month_diff - 1), display_date, address, (month_diff + 1))
