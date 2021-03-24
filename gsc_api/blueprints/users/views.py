from flask import Blueprint, jsonify, request
from models.user import *
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

users_api_blueprint = Blueprint('users_api',
                             __name__)

@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.select()
    return jsonify([{
        "id": user.id,
        "gender": user.gender,
        "year_of_birth": user.year_of_birth,
        "height": user.height,
        "languages": user.languages,
        "nationality": user.nationality,
        "city": user.city,
        "country": user.country,
        "descriptive_words": user.descriptive_words,
        "mbti": user.mbti,
        "enneagram":  user.enneagram,
        "disc": user.disc,
        "strengths_finder": user.strengths_finder,
        "favorite_topics": user.favorite_topics,
        "chill_activities": user.chill_activities,
        "do": user.do,
        "skills_and_talents":  user.skills_and_talents,
        "favorite_cuisine": user.favorite_cuisine,
        "growth_and_development": user.growth_and_development,
        "spiritual_gifts": user.spiritual_gifts,
        "duration_of_being_a_christian": user.duration_of_being_a_christian,
        "church_background": user.church_background,
        "reasons_sf_makes_a_good_partner": user.reasons_sf_makes_a_good_partner,
        "good_match_for_sf": user.good_match_for_sf,
        "moving_to_a_different_town": user.moving_to_a_different_town,
        "moving_to_a_different_country": user.moving_to_a_different_country,
        "has_been_married_or_has_kids": user.has_been_married_or_has_kids,
        "desire_to_have_kids": user.desire_to_have_kids,
        "important_info_to_know": user.important_info_to_know,
        "first_referral_name": user.first_referral_name,
        "first_referral_email": user.first_referral_email,
        "second_referral_name": user.second_referral_name,
        "second_referral_email": user.second_referral_email,
        "ff_email": user.ff_email,
        }
        for user in users
    ])

@users_api_blueprint.route('/', methods=['POST'])
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
        user = User(
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
        if user.save():
            token = create_access_token(identity=user.id)
            return jsonify({
                "auth_token": token,
                "message": "Successfully created a user and signed in",
                "status": "success",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                }
            })
        elif user.errors != 0:
            return jsonify({
                "message": [error for error in user.errors],
                "status": "failed"
            })
    else:
        return jsonify({
            "message": "All fields are required!",
            "status": "failed"
        })