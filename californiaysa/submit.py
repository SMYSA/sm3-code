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
from WeeklyReport import WeeklyReport
from FinalReport import FinalReport


class InitialAssessmentHandler(webapp.RequestHandler):

  def get(self):
    a = InitialAssessment()
#    a.unit = self.request.get("unit_select")
    a.unit = self.request.get("unit")
    a.stake = self.request.get("stake_select")
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

#    self.response.out.write(str(self.request))
    self.redirect("/thanks.html")

class WeeklyReportHandler(webapp.RequestHandler):

  def get(self):
    r = WeeklyReport()
    r._entity = None
#    r.unit = self.request.get("unit_select")
    r.unit = self.request.get("unit")
    r.stake = self.request.get("stake_select")
    r.name = self.request.get("name")
    r.email = self.request.get("email")
    r.phone = self.request.get("phone")
    r.less_active_visits = int(self.request.get("less_active_visits"))
    r.stake_ysa_visits = int(self.request.get("stake_ysa_visits"))
    r.renewed_temple_recommends = (
      int(self.request.get("renewed_temple_recommends")))
    r.reissued_temple_recommends = (
      int(self.request.get("reissued_temple_recommends")))
    r.first_time_temple_recommends = (
      int(self.request.get("first_time_temple_recommends")))

    r.temple_ordinances = int(self.request.get("temple_ordinances"))

    # These values should be 0.  We keep them to maintain backward compatability
    r.endowments = int(self.request.get("endowments"))
    r.sealings = int(self.request.get("sealings"))
    r.initiatories = int(self.request.get("initiatories"))
    r.baptisms_confirmations = int(self.request.get("baptisms_confirmations"))
    # End deprecated fields

    r.family_file_names = int(self.request.get("family_file_names"))
    r.registered_voters = int(self.request.get("registered_voters"))
    r.submit_date = datetime.now()
    r.put()

#    self.response.out.write(str(self.request))
    self.redirect("/thanks.html")

class FinalReportHandler(webapp.RequestHandler):

  def get(self):
    r = FinalReport()
    r._entity = None
    r.unit = self.request.get("unit")
    r.stake = self.request.get("stake_select")
    r.name = self.request.get("name")
    r.email = self.request.get("email")
    r.phone = self.request.get("phone")
    r.aug8_active_members = int(self.request.get("aug8_active_members"))
    r.aug8_less_active_members = int(
        self.request.get("aug8_less_active_members"))
    r.aug8_non_members = int(self.request.get("aug8_non_members"))
    r.submit_date = datetime.now()
    r.put()

#    self.response.out.write(str(self.request))
    self.redirect("/thanks.html")


def main():
  application = webapp.WSGIApplication([
      ('/submit/initial_assessment', InitialAssessmentHandler),
      ('/submit/weekly_report', WeeklyReportHandler),
      ('/submit/final_report', FinalReportHandler),
      ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
