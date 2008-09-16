
import cgi
import AuthModule
import Common

form = cgi.FieldStorage()

#
# Perform Authorization
#
Common.AuthorizePage(["hteacher", "vteacher", "htadmin", "vtadmin", "admin"])
ht_or_vt = Common.GetPageType(form)

user = AuthModule.authorized_user
if user in ["hteacher", "vteacher"]:
  Common.PrintRedirect("302", "display_assignments")
elif user in ["htadmin", "vtadmin"]:
  Common.PrintRedirect("302", "upload")
elif user == "admin":
  Common.PrintRedirect("302", "upload?group=%s" % ht_or_vt)
