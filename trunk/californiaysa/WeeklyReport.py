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

class WeeklyReport(db.Model):
  unit = db.StringProperty()
  stake = db.StringProperty()
  name = db.StringProperty()
  email = db.StringProperty()
  phone = db.StringProperty()
  less_active_visits = db.IntegerProperty()
  stake_ysa_visits = db.IntegerProperty()
  renewed_temple_recommends = db.IntegerProperty()
  reissued_temple_recommends = db.IntegerProperty()
  first_time_temple_recommends = db.IntegerProperty()
  temple_ordinances = db.IntegerProperty()
  registered_voters = db.IntegerProperty()
  submit_date = db.DateTimeProperty(auto_now_add=True)

  # These fields are no longer used.  They have been replaced by
  # the "temple_ordinances field.
  endowments = db.IntegerProperty()
  sealings = db.IntegerProperty()
  initiatories = db.IntegerProperty()
  baptisms_confirmations = db.IntegerProperty()
  family_file_names = db.IntegerProperty()
  # End deprecated fields

  DB_NAME = "Tbl_Weekly_Submission"

  def __init__(self, *args, **kw):
    db.Model.__init__(self, *args, **kw)
    self.questions = []
    self.questions.append({
        "id": "unit_select",
        "type": "select",
        "text": "Unit",
        "help_text": "",
        "validation": "onchange='SetStakeFromUnit();'"
        })
    self.questions.append({
        "id": "stake_select",
        "type": "select",
        "text": "Stake",
        "help_text": "",
        "validation": ""
        })
    self.questions.append({
        "id": "name",
        "type": "text",
        "text": "Name",
        "help_text": "",
        "validation": ""
        })
    self.questions.append({
        "id": "email",
        "type": "text",
        "text": "Email",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    self.questions.append({
        "id": "phone",
        "type": "text",
        "text": "Phone",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    self.questions.append({
        "id": "less_active_visits",
        "type": "text",
        "text": "Less Active YSA Visits",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    self.questions.append({
        "id": "stake_ysa_visits",
        "type": "hidden",
        "text": "Stake YSA Visits",
        "help_text": "",
        "validation": "",
        "value": "0",
        })
    self.questions.append({
        "id": "renewed_temple_recommends",
        "type": "text",
        "text": "Renewed YSA Temple Recommends",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    self.questions.append({
        "id": "reissued_temple_recommends",
        "type": "text",
        "text": "Reissued YSA Temple Recommends",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    self.questions.append({
        "id": "first_time_temple_recommends",
        "type": "text",
        "text": "First Time YSA Temple Recommends",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })

    self.questions.append({
        "id": "temple_ordinances",
        "type": "text",
        "text": "Temple Ordinances (YSA)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })
    # These fields are no longer used.  They have been replaced by
    # the "temple_ordinances field.
    self.questions.append({
        "id": "endowments",
        "type": "hidden",
        "text": "Endowments (YSA)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'",
        "value": "0",
        })
    self.questions.append({
        "id": "sealings",
        "type": "hidden",
        "text": "Sealings (YSA)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'",
        "value": "0",
        })
    self.questions.append({
        "id": "initiatories",
        "type": "hidden",
        "text": "Initiatories (YSA)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'",
        "value": "0",
        })
    self.questions.append({
        "id": "baptisms_confirmations",
        "type": "hidden",
        "text": "Baptisms/Confirmations (YSA)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'",
        "value": "0",
        })
    self.questions.append({
        "id": "family_file_names",
        "type": "hidden",
        "text": "Ordinances from Family File Names",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'",
        "value": "0",
        })
    # End deprecated fields

    self.questions.append({
        "id": "registered_voters",
        "type": "text",
        "text": "Total Registered YSA Voters (Running Total)",
        "help_text": "",
        "validation": "onkeyup='MaybeValidate();'"
        })


  def GetQuestionList(self):
    return self.questions

  def PrintInsertStatement(self, writer):
    writer.write("INSERT INTO %s " % self.DB_NAME)
    writer.write(("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " +
        "%s, %s, %s, %s) ") % (
          "Unit",
          "Stake",
          "Name",
          "Email",
          "Phone",
          "Less_Active_Visits",
          "Stake_YSA_Visits",
          "Renewed_Temple_Recommends",
          "Reissued_temple_recommends",
          "First_Time_recommends",
          "Endowments",
          "Sealings",
          "Initiatories",
          "Baptisms_Confirmations",
          "Family_File_Name",
          "Registered_Voters",
          "Submit_Date",
          ))
    writer.write("VALUES('%s', '%s', '%s', '%s', '%s'," % (
            self.unit, self.stake, self.name, self.email, self.phone))
    writer.write("%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s');\n" % (
        self.less_active_visits,
        self.stake_ysa_visits,
        self.renewed_temple_recommends,
        self.reissued_temple_recommends,
        self.first_time_temple_recommends,
        self.endowments,
        self.sealings,
        self.initiatories,
        self.baptisms_confirmations,
        self.family_file_names,
        self.registered_voters,
        self.submit_date.ctime(),
        ))

