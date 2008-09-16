#!/usr/bin/python

import os

def GetAssignmentFile(ht_or_vt, year, month):
  path = os.path.join("assignments", str(year))
  if not os.path.exists(path):
    os.mkdir(path, 0777)
  os.chmod(path, 0777)
  path = os.path.join(path, str(month))
  if not os.path.exists(path):
    os.mkdir(path, 0777)
  os.chmod(path, 0777)
  path = os.path.join(path, ht_or_vt + "_assignments.dat")
  return path

def GetReportFile(ht_or_vt, year, month):
  path = os.path.join("assignments", str(year))
  if not os.path.exists(path):
    os.mkdir(path, 0777)
  os.chmod(path, 0777)
  path = os.path.join(path, str(month))
  if not os.path.exists(path):
    os.mkdir(path, 0777)
  os.chmod(path, 0777)
  path = os.path.join(path, ht_or_vt + "_reports.dat")
  return path

def PrintRedirect(status, location):
  print "Status: %s" % status
  print "Location: %s" % location
  print
  print "<html><body>Redirecting</body></html>"


def PrintDetermineGroup(page):
  print "<a href='%s?group=ht'>Home Teaching</a> or " % page
  print "<a href='%s?group=vt'>Visiting Teaching</a>" % page


def AuthorizePage(user_list):
  import AuthModule
  if not AuthModule.Authorize():
    import sys
    AuthModule.PrintBasicAuthHeader()
    sys.exit(0)

  # This will exit if the user is not authorized
  AuthModule.CheckUserAuthorization(user_list)

def GetPageType(form):
  import AuthModule
  user = AuthModule.authorized_user
  if user in ["hteacher", "htadmin"]:
    return "ht"
  elif user in ["vteacher", "vtadmin"]:
    return "vt"
  elif (user == "admin" and form.has_key("group") and
        form["group"].value in ["ht", "vt"]):
    return form["group"].value
  return None

