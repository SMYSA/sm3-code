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
    assesments = InitialAssessment.gql("ORDER BY submit_date")
    self.response.headers["Content-Type"] = "text/plain"
    for a in assesments:
      a.PrintInsertStatement(self.response.out)

class WeeklyReportHandler(webapp.RequestHandler):
  def get(self):
    reports = WeeklyReport.gql("ORDER BY submit_date")
    self.response.headers["Content-Type"] = "text/plain"
    for r in reports:
      r.PrintInsertStatement(self.response.out)

class FinalReportHandler(webapp.RequestHandler):
  def get(self):
    reports = FinalReport.gql("ORDER BY submit_date")
    self.response.headers["Content-Type"] = "text/plain"
    for r in reports:
      r.PrintInsertStatement(self.response.out)


def main():
  application = webapp.WSGIApplication([
      ('/sql/initial_assessment', InitialAssessmentHandler),
      ('/sql/weekly_report', WeeklyReportHandler),
      ('/sql/final_report', FinalReportHandler),
      ],
      debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
