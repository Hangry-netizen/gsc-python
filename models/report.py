from models.base_model import BaseModel
import peewee as pw
from models.gsc import Gsc

class Report(BaseModel):
    gsc = pw.ForeignKeyField(Gsc, backref="reports", on_delete="CASCADE")
    concerns = pw.TextField()
    actions = pw.CharField()
  