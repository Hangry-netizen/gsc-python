from models.base_model import BaseModel
import peewee as pw
import uuid

class Gsc(BaseModel):
    uuid = pw.UUIDField()
    name = pw.CharField()
    email = pw.CharField(unique=True)
    gender = pw.CharField()
    year_of_birth = pw.IntegerField()
    height = pw.CharField(null=True)
    languages = pw.TextField()
    nationality = pw.CharField()
    city = pw.CharField()
    country = pw.CharField()
    descriptive_words = pw.TextField()
    mbti = pw.CharField(null=True)
    enneagram = pw.CharField(null=True)
    disc = pw.CharField(null=True)
    strengths_finder = pw.CharField(null=True)
    favorite_topics = pw.TextField(null=True)
    chill_activities = pw.TextField(null=True)
    do = pw.TextField()
    skills_and_talents = pw.TextField()
    growth_and_development = pw.TextField()
    spiritual_gifts = pw.TextField()
    spiritual_maturity = pw.TextField()
    church_background = pw.TextField()
    reasons_gscf_makes_a_good_partner = pw.TextField()
    good_match_for_gscf = pw.TextField()
    moving_to_a_different_town = pw.CharField(null=True)
    moving_to_a_different_country = pw.CharField(null=True)
    has_been_married_or_has_kids = pw.CharField()
    want_to_have_kids = pw.CharField()
    important_info_to_know = pw.TextField(null=True)
    alias = pw.CharField()
    consent = pw.BooleanField(default=False)
    social_media_profile_link= pw.CharField(null=True)
    preferred_contact_method = pw.CharField(null=True)
    contact_info = pw.CharField(null=True)
    notification_frequency = pw.CharField(null=True)
    what_is_important_to_me = pw.TextField(null=True)
    first_referral_name = pw.CharField(null=True)
    first_referral_email = pw.CharField(null=True)
    second_referral_name = pw.CharField(null=True)
    second_referral_email = pw.CharField(null=True)
    ff_email = pw.CharField()
    is_approved = pw.BooleanField(default=False)
    is_active = pw.BooleanField(default=False)
    last_signed_in = pw.DateField(null=True)

    def validate(self):
        duplicate_email = Gsc.get_or_none(Gsc.email == self.email)

        if duplicate_email and self.id != duplicate_email.id:
            self.errors.append("There is an existing account with this email address")

        else:
            self.uuid = uuid.uuid4()