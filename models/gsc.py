from models.base_model import BaseModel
import peewee as pw


class Gsc(BaseModel):
    name = pw.CharField()
    email = pw.CharField(unique=True)
    contact_method = pw.CharField()
    contact_info = pw.CharField()
    gender = pw.CharField()
    year_of_birth = pw.CharField()
    height = pw.CharField()
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
    favorite_cuisine = pw.TextField()
    growth_and_development = pw.TextField()
    spiritual_gifts = pw.CharField()
    duration_of_being_a_christian = pw.CharField()
    church_background = pw.TextField()
    reasons_sf_makes_a_good_partner = pw.TextField()
    good_match_for_sf = pw.TextField()
    moving_to_a_different_town = pw.IntegerField()
    moving_to_a_different_country = pw.IntegerField()
    has_been_married_or_has_kids = pw.CharField()
    desire_to_have_kids = pw.CharField()
    important_info_to_know = pw.TextField(null=True)
    first_referral_name = pw.CharField(null=True)
    first_referral_email = pw.CharField(null=True)
    second_referral_name = pw.CharField(null=True)
    second_referral_email = pw.CharField(null=True)
    ff_email = pw.CharField()

    def validate(self):
        duplicate_email = Gsc.get_or_none(Gsc.email == self.email)
        print("GSC validation in process")

        if duplicate_email and self.id != duplicate_email.id:
            self.errors.append("There is an existing account with this email address")
