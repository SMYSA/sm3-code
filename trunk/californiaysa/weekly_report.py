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

import os
from datetime import datetime

import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from WeeklyReport import WeeklyReport


class WeeklyReportHandler(webapp.RequestHandler):

  title = "Weekly Report"
  description = "Please fill out the form for your Ward or Branch"
  custom_validators = "<script src='weekly_validators.js'></script>"
  onload = "onload='AddStakeUnits();'"
  form_action = "/submit/weekly_report"

  def get(self):
    report = WeeklyReport()
    template_values = {
      "title_text": self.title,
      "description": self.description,
      "custom_validators": self.custom_validators,
      "onload_event": self.onload,
      "form_action": self.form_action,
      "questions": report.GetQuestionList(),
    }
    path = os.path.join(os.path.dirname(__file__), "entry_form.html")
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication([
      ('/weekly_report', WeeklyReportHandler),
      ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
