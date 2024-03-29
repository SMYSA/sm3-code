#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from datetime import datetime

import wsgiref.handlers

from google.appengine.ext import webapp

from InitialAssessment import InitialAssessment


class MainHandler(webapp.RequestHandler):

  def get(self):
    a = InitialAssessment()
    a.unit = "a"
    a.stake = "b"
    a.name = "c"
    a.email = "d"
    a.subit_date = datetime.now()
    a.put()
    assesments = InitialAssessment.gql("ORDER BY submit_date")
    for a in assesments:
      self.response.out.write("%s<br>" % a.unit)
      self.response.out.write("%s<br>" % a.stake)
      self.response.out.write("%s<br>" % a.name)
      self.response.out.write("%s<br>" % a.email)
#      self.response.out.write("%s<br>" % a.submit_date.ctime())
      self.response.out.write("%s<br>" % a.actual_submit_date.ctime())
      self.response.out.write("<br><br><br>")
#      self.response.headers["WWW-Authenticate"] = "Basic realm=\"California YSA\""
#      self.response.out.write('Hello world!')


def main():
  application = webapp.WSGIApplication([
      ('/', MainHandler),
#      ('/i', MainHandler)
      ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
