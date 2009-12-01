#!/usr/bin/python

class ReportInfo:
  def __init__(self):
    self.visited = False
    self.reported = False
    self.report_notes = ""
    self.reported_by = ""
    self.contact_types = []


class HTDistrict:
  def __init__(self, d_id, supervisor):
    self.district_id    = d_id
    self.supervisor     = supervisor
    self.companionships = {}

  def AddCompanionship(self, comp):
    self.companionships[comp.comp_id] = comp

  def GetCompanionship(self, comp_id):
    if comp_id in self.companionships:
      return self.companionships[comp_id]
    else:
      return None

  def GetCompanionships(self):
    return self.companionships

  def GetSupervisor(self):
    return self.supervisor

  def RenderHtml(self):
    pass


class HTCompanionship:
  def __init__(self, id, super, senior_comp, junior_comp):
    self.comp_id     = id
    self.supervisor  = super
    self.senior_comp = senior_comp
    self.junior_comp = junior_comp
    self.assignments = []

  def AddAssignment(self, assignment):
    self.assignments.append(assignment)

  def RenderHtml(self):
    pass


class HomeTeacher:
  def __init__(self, first_name, last_name, phone):
    self.first_name = first_name
    self.last_name  = last_name
    self.phone      = phone
    
  def RenderHtml(self):
    pass


class HTAssignment:
  def __init__(self, id, first_name, last_name, phone, email, street,
               city, zip):
    self.comp_id    = id
    self.first_name = first_name
    self.last_name  = last_name
    self.phone      = phone
    self.email      = email
    self.street     = street
    self.city       = city
    self.zip        = zip

  def RenderHtml(self):
    pass


class SM3HomeTeaching:
  #
  # The fields of a line in the csv file are as follows:
  #
  #  0  - Quroum
  #  1  - HT District ID
  #  2  - HT Supervisor Name
  #  3  - HT Supervisor Phone
  #  4  - Companionship ID
  #  5  - Senior Companion
  #  6  - Senior Companion Phone
  #  7  - Junior Companion
  #  8  - Junior Companion Phone
  #  9  - HT Assignment Name
  #  10 - HT Assignment Phone 1
  #  11 - HT Assignment Phone 2
  #  12 - HT Assignment Email
  #  13 - HT Assignment Street 1
  #  14 - HT Assignment Street 2
  #  15 - HT Assignment D/P ????
  #  16 - HT Assignment City
  #  17 - HT Assignment Zip
  #  18 - HT Assignment State
  #  19 - HT Assignment Country
  #
  def __init__(self, ht_file_lines):
    self.districts       = {}
    self.district_offset = {}
    self.district_offset[0] = 0

    for line in ht_file_lines:
      fields = self._SplitLine(line.strip())
      if fields[0] == "Quorum" or fields[0] == "":
        continue
      district_id = int(fields[1])
      quorum = int(fields[0].split()[-1])
      if not self.district_offset.has_key(quorum):
        self.district_offset[quorum] = 0
      if self.district_offset[quorum] < district_id:
        self.district_offset[quorum] = district_id

    for line in ht_file_lines:
      fields        = self._SplitLine(line.strip())
      if fields[0] == "Quorum" or fields[0] == "":
        continue

      district      = self._GetDistrictFromCsv(fields)
      companionship = self._GetCompanionshipFromCsv(district, fields)
      assignment    = self._GetAssignmentFromCsv(fields)

      companionship.AddAssignment(assignment)

  def GetHTDistricts(self):
    return self.districts

  def _GetDistrictFromCsv(self, fields):
    quorum = int(fields[0].split()[-1])
    district_id = int(fields[1]) + self.district_offset[quorum - 1]
    district = None
    if district_id in self.districts:
      district = self.districts[district_id]
    else:
      supervisor = self._GetHTCompanionFromCsv(fields, 2)
      district   = HTDistrict(district_id, supervisor)
      self.districts[district_id] = district
    return district

  def _GetCompanionshipFromCsv(self, district, fields):
    comp_id = int(fields[5])
    comp = district.GetCompanionship(comp_id)
    if comp:
      return comp
    else:
      supervisor  = district.GetSupervisor()
      senior_comp = self._GetHTCompanionFromCsv(fields, 6)
      junior_comp = self._GetHTCompanionFromCsv(fields, 8)
      comp = HTCompanionship(comp_id, supervisor, senior_comp, junior_comp)
      district.AddCompanionship(comp)
    return comp

  def _GetHTCompanionFromCsv(self, fields, index):
    name = fields[index]
    first_name = ""
    last_name = ""
    if name != "":
      first_name = name.split(",")[1].strip()   
      last_name  = name.split(",")[0].strip()   
    return HomeTeacher(first_name, last_name, fields[index + 1])

  def _GetAssignmentFromCsv(self, fields):
    first_name = fields[9].split(",")[1].strip()
    last_name  = fields[9].split(",")[0].strip()
    street     = fields[13]
    if fields[14] != "":
      street = street + " " + fields[14]
    assignment = HTAssignment(fields[4], first_name, last_name, fields[10],
      fields[12], street, fields[16], fields[17])
    return assignment

  def _SplitLine(self, line):
    fields = line.split("\",\"")
    fields[0]  = fields[0][1:]
    fields[-1] = fields[-1][:-2]
    return fields

if __name__ == "__main__":
  ht_file_name = "HomeTeaching.csv"
  sm3_ht = SM3HomeTeaching(ht_file_name)
  districts = sm3_ht.GetHTDistricts()
  for d in districts:
    print str(d) + " ",
    print districts[d]
