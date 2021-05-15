from models.base_model import BaseModel
import peewee as pw
from models.gsc import Gsc

class Reference(BaseModel):
    gsc = pw.ForeignKeyField(Gsc, backref="references", on_delete="CASCADE")
    referral_name = pw.CharField()
    reasons_gscf_makes_a_good_partner = pw.TextField()
    good_match_for_gscf = pw.TextField()