#!/usr/bin/python


__AUTHORIZED_USERS = {
  "hteacher": "teach",
  "vteacher": "visit",
  "htadmin":  "Jacob",
  "vtadmin":  "Abish",
  "admin":    "CanViewAllPages"
}

authorized_user = None

def Authorize():
  global authorized_user
  import os
  import base64
  if not os.environ.has_key("HTTP_AUTHORIZATION"):
    return False

  auth_str = os.environ["HTTP_AUTHORIZATION"].strip().split(" ")[1]
  decode_str = base64.decodestring(auth_str)
  fields = decode_str.split(":")
  (user, password) = (fields[0], fields[1])
  if __AUTHORIZED_USERS.has_key(user) and __AUTHORIZED_USERS[user] == password:
    authorized_user = user
    return True
  return False

def PrintBasicAuthHeader():
  print "Status: 401 UNAUTHORIZED"
  print "WWW-Authenticate: Basic realm=\"SM3 Home/Visiting Teaching\""
  print

def CheckUserAuthorization(users):
  if not authorized_user in users:
    import sys
    PrintNotAuthorized()
    sys.exit(0)

def PrintNotAuthorized():
  print "Content-Type: text/html"
  print
  print "<html><body>"
  print "<h1>%s is not authorized to view this page." % authorized_user
  print "</body></html>"
