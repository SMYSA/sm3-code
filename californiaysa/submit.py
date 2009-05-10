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


class InitialAssessmentHandler(webapp.RequestHandler):

  def get(self):
    a = InitialAssessment()
    a.unit = self.request.get("unit")
    a.stake = self.request.get("stake")
    a.name = self.request.get("name")
    a.email = self.request.get("email")
    a.phone = self.request.get("phone")
    a.total_members = int(self.request.get("member_count"))
    a.active_members = int(self.request.get("active_count"))
    a.less_active_members = int(self.request.get("less_active_count"))
    a.stake_ysa_members = int(self.request.get("stake_ysas"))
    a.active_temple_recommends = int(self.request.get("current_temple"))
    a.expired_temple_recommends = int(self.request.get("expired_temple"))
    a.potential_temple_recommends = int(self.request.get("potential_temple"))
    a.avg_temple_distance = int(self.request.get("temple_distance"))
    a.may17_est = int(self.request.get("may17"))
    a.aug8_est = int(self.request.get("august8"))
    a.registered_voters = int(self.request.get("voters"))
    a.submit_date = datetime.now()
    a.put()

    self.redirect("/thanks.html")


def main():
  application = webapp.WSGIApplication([
      ('/submit/initial_assessment', InitialAssessmentHandler),
      ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
