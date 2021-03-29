from flask import Blueprint, jsonify, request
from models.gsc import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

gscs_api_blueprint = Blueprint('gscs_api',
                             __name__)

@gscs_api_blueprint.route('/', methods=['GET'])
def index():
    gscs = Gsc.select()
    return jsonify([{
        "id": gsc.id,
        "name": gsc.name,
        "email": gsc.email,
        "contact_method": gsc.contact_method,
        "contact_info": gsc.contact_info,
        "gender": gsc.gender,
        "year_of_birth": gsc.year_of_birth,
        "height": gsc.height,
        "languages": gsc.languages,
        "nationality": gsc.nationality,
        "city": gsc.city,
        "country": gsc.country,
        "descriptive_words": gsc.descriptive_words,
        "mbti": gsc.mbti,
        "enneagram":  gsc.enneagram,
        "disc": gsc.disc,
        "strengths_finder": gsc.strengths_finder,
        "favorite_topics": gsc.favorite_topics,
        "chill_activities": gsc.chill_activities,
        "do": gsc.do,
        "skills_and_talents":  gsc.skills_and_talents,
        "favorite_cuisine": gsc.favorite_cuisine,
        "growth_and_development": gsc.growth_and_development,
        "spiritual_gifts": gsc.spiritual_gifts,
        "duration_of_being_a_christian": gsc.duration_of_being_a_christian,
        "church_background": gsc.church_background,
        "reasons_sf_makes_a_good_partner": gsc.reasons_sf_makes_a_good_partner,
        "good_match_for_sf": gsc.good_match_for_sf,
        "moving_to_a_different_town": gsc.moving_to_a_different_town,
        "moving_to_a_different_country": gsc.moving_to_a_different_country,
        "has_been_married_or_has_kids": gsc.has_been_married_or_has_kids,
        "desire_to_have_kids": gsc.desire_to_have_kids,
        "important_info_to_know": gsc.important_info_to_know,
        "first_referral_name": gsc.first_referral_name,
        "first_referral_email": gsc.first_referral_email,
        "second_referral_name": gsc.second_referral_name,
        "second_referral_email": gsc.second_referral_email,
        "ff_email": gsc.ff_email,
        }
        for gsc in gscs
    ])

@gscs_api_blueprint.route('/', methods=['POST'])
def create():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    contact_method = data.get('contact_method')
    contact_info = data.get('contact_info')
    gender = data.get('gender')
    year_of_birth = data.get('year_of_birth')
    height = data.get('height')
    languages = data.get('languages')
    nationality = data.get('nationality')
    city = data.get('city')
    country = data.get('country')
    descriptive_words = data.get('descriptive_words')
    mbti = data.get('mbti')
    enneagram = data.get('enneagram')
    disc = data.get('disc')
    strengths_finder = data.get('strengths_finder')
    favorite_topics = data.get('favorite_topics')
    chill_activities = data.get('chill_activities')
    do = data.get('do')
    skills_and_talents = data.get('skills_and_talents')
    favorite_cuisine = data.get('favorite_cuisine')
    growth_and_development = data.get('growth_and_development')
    spiritual_gifts = data.get('spiritual_gifts')
    duration_of_being_a_christian = data.get('duration_of_being_a_christian')
    church_background = data.get('church_background')
    reasons_sf_makes_a_good_partner = data.get('reasons_sf_makes_a_good_partner')
    good_match_for_sf = data.get('good_match_for_sf')
    moving_to_a_different_town = data.get('moving_to_a_different_town')
    moving_to_a_different_country = data.get('moving_to_a_different_country')
    has_been_married_or_has_kids = data.get('has_been_married_or_has_kids')
    desire_to_have_kids = data.get('desire_to_have_kids')
    important_info_to_know = data.get('important_info_to_know')
    first_referral_name = data.get('first_referral_name')
    first_referral_email = data.get('first_referral_email')
    second_referral_name = data.get('second_referral_name')
    second_referral_email = data.get('second_referral_email')
    ff_email = data.get('ff_email')

    if name and email:
        gsc = Gsc(
            name = name,
            email = email,
            contact_method = contact_method,
            contact_info = contact_info,
            gender = gender,
            year_of_birth = year_of_birth,
            height = height,
            languages = languages,
            nationality = nationality,
            city = city,
            country = country,
            descriptive_words = descriptive_words,
            mbti = mbti,
            enneagram = enneagram,
            disc = disc,
            strengths_finder = strengths_finder,
            favorite_topics = favorite_topics,
            chill_activities = chill_activities,
            do = do,
            skills_and_talents = skills_and_talents,
            favorite_cuisine = favorite_cuisine,
            growth_and_development = growth_and_development,
            spiritual_gifts = spiritual_gifts,
            duration_of_being_a_christian = duration_of_being_a_christian,
            church_background = church_background,
            reasons_sf_makes_a_good_partner = reasons_sf_makes_a_good_partner,
            good_match_for_sf = good_match_for_sf,
            moving_to_a_different_town = moving_to_a_different_town,
            moving_to_a_different_country = moving_to_a_different_country,
            has_been_married_or_has_kids = has_been_married_or_has_kids,
            desire_to_have_kids = desire_to_have_kids,
            important_info_to_know = important_info_to_know,
            first_referral_name = first_referral_name,
            first_referral_email = first_referral_email,
            second_referral_name = second_referral_name,
            second_referral_email = second_referral_email,
            ff_email = ff_email
        )
        if gsc.save():
            token = create_access_token(identity=gsc.id)
            return jsonify({
                "auth_token": token,
                "message": "Successfully added a new gsc",
                "status": "success",
                "gsc": {
                    "id": gsc.id,
                    "name": gsc.name,
                    "email": gsc.email
                }
            })
        elif gsc.errors != 0:
            return jsonify({
                "message": [error for error in gsc.errors],
                "status": "failed"
            })
    else:
        return jsonify({
            "message": "All fields are required!",
            "status": "failed"
        })