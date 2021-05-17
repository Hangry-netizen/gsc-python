from models.base_model import BaseModel
import peewee as pw
from models.gsc import Gsc

class Report(BaseModel):
    reported_by = pw.ForeignKeyField(Gsc, backref="reports", on_delete="CASCADE")
    got_reported = pw.ForeignKeyField(Gsc, backref="reports", on_delete="CASCADE")
    concerns = pw.TextField()
    actions = pw.CharField()
  