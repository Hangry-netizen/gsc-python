from models.base_model import BaseModel
import peewee as pw


class Approval(BaseModel):
    gsc_name = pw.CharField()
    ff_email = pw.CharField()