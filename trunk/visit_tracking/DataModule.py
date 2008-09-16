#!/usr/bin/python

#import cPickle
import pickle

from google.appengine.ext import db

class Sm3HtVtReports(db.Model):
  year    = db.IntegerProperty()
  month   = db.IntegerProperty()
  type    = db.StringProperty()
  reports = db.BlobProperty()

class Sm3HtVtAssignments(db.Model):
  year        = db.IntegerProperty()
  month       = db.IntegerProperty()
  type        = db.StringProperty()
  assignments = db.BlobProperty()


def GetReports(ht_or_vt, year, month):
  q = Sm3HtVtReports.all()
  q.filter("year = ", year)
  q.filter("month = ", month)
  q.filter("type = ", ht_or_vt)
  result = q.fetch(2)
  assert(len(result) <= 1)
  if len(result) == 1:
    return pickle.loads(result[0].reports)
  else:
    return {}

def PutReports(ht_or_vt, year, month, reports):
  q = Sm3HtVtReports.all()
  q.filter("year = ", year)
  q.filter("month = ", month)
  q.filter("type = ", ht_or_vt)
  result = q.fetch(2)
  r = None
  if (len(result) == 0):
    r = Sm3HtVtReports()
    r.year = year
    r.month = month
    r.type = ht_or_vt
  else:
   r = result[0]
  r.reports = pickle.dumps(reports)
  r.put()

def GetAssignments(ht_or_vt, year, month):
  q = Sm3HtVtAssignments.all()
  q.filter("year = ", year)
  q.filter("month = ", month)
  q.filter("type = ", ht_or_vt)
  result = q.fetch(2)
  assert(len(result) <= 1)
  if len(result) == 1:
    return pickle.loads(result[0].assignments)
  else:
    return {}

def PutAssignments(ht_or_vt, year, month, assignments):
  q = Sm3HtVtAssignments.all()
  q.filter("year = ", year)
  q.filter("month = ", month)
  q.filter("type = ", ht_or_vt)
  result = q.fetch(2)
  r = None
  if (len(result) == 0):
    r = Sm3HtVtAssignments()
    r.year = year
    r.month = month
    r.type = ht_or_vt
  else:
   r = result[0]
  r.assignments = pickle.dumps(assignments)
  r.put()

