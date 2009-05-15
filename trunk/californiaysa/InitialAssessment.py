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


from google.appengine.ext import db 
class InitialAssessment(db.Model):
  unit = db.StringProperty()
  stake = db.StringProperty()
  name = db.StringProperty()
  email = db.StringProperty()
  phone = db.StringProperty()
  total_members = db.IntegerProperty()
  active_members = db.IntegerProperty()
  less_active_members = db.IntegerProperty()
  stake_ysa_members = db.IntegerProperty()
  active_temple_recommends = db.IntegerProperty()
  expired_temple_recommends = db.IntegerProperty()
  potential_temple_recommends = db.IntegerProperty()
  avg_temple_distance = db.IntegerProperty()
  may17_est = db.IntegerProperty()
  aug8_est = db.IntegerProperty()
  registered_voters = db.IntegerProperty()
  submit_date = db.DateTimeProperty(auto_now_add=True)

  DB_NAME = "Tbl_Initial_Assessment"

  def PrintInsertStatement(self, writer):
    writer.write("INSERT INTO %s " % self.DB_NAME)
    writer.write(("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " +
        "%s, %s, %s, %s) ") % (
          "Unit",
          "Stake",
          "Name",
          "Email",
          "Phone",
          "Total_Membership",
          "Active_Membership",
          "Less_Active_members",
          "Stake_YSA",
          "Current_temple_recommend_holders",
          "Expired_temple_recommends",
          "Potential_temple_recommends",
          "Avg_temple_distance",
          "May17_Estimate",
          "August8_Estimate",
          "Registered_Voters",
          "Submit_Date",
          ))
    writer.write("VALUES('%s', '%s', '%s', '%s', '%s'," % (
            self.unit, self.stake, self.name, self.email, self.phone))
    writer.write("%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s');\n" % (
        self.total_members,
        self.active_members,
        self.less_active_members,
        self.stake_ysa_members,
        self.active_temple_recommends,
        self.expired_temple_recommends,
        self.potential_temple_recommends,
        self.avg_temple_distance,
        self.may17_est,
        self.aug8_est,
        self.registered_voters,
        self.submit_date.ctime(),
        ))

