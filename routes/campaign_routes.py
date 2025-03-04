from flask import Blueprint, request, jsonify
from app import db
from models.campaign import Campaign
from utils.json_response import render_json
from utils.db_handle_error import handle_db_commit

campaign_bp = Blueprint('campaign_bp', __name__)

@campaign_bp.route('/', methods=['POST'])
def create_campaign():
    data = request.get_json()
    new_campaign = Campaign(
        user_id = data['user_id'],
        name = data['name'],
        short_description = data['short_description'],
        description = data['description'],
        goal_amount = data['goal_amount'],
        current_amount = data.get('current_amount', 0),
        perks = data.get('perks', ''),
        backer_count = data.get('backer_count', 0),
        slug = data['slug']
    )
    db.session.add(new_campaign)
    
    error_response = handle_db_commit(db)
    if error_response:
        return error_response

    campaign_data = {
        "id": new_campaign.id,
        "name": new_campaign.name,
        "user_id": new_campaign.user_id,
        "short_description": new_campaign.short_description,
        "description": new_campaign.description,
        "goal_amount": new_campaign.goal_amount,
        "current_amount": new_campaign.current_amount,
        "perks": new_campaign.perks,
        "backer_count": new_campaign.backer_count,
        "slug": new_campaign.slug,
        }
    
    return render_json("Campaign created successfully", 201, "success", campaign_data)

@campaign_bp.route('/', methods=['GET'])
def get_campaigns():
    campaigns = Campaign.query.all()
    if campaigns is None:
        return render_json("Campaign not found", 404, "error", None)
    
    campaign_datas = [{
        "id": c.id,
        "user_id": c.user_id,
        "short_description": c.short_description,
        "description": c.description,
        "goal_amount": c.goal_amount,
        "current_amount": c.current_amount,
        "perks": c.perks,
        "backer_count": c.backer_count,
        "slug": c.slug,
        } for c in campaigns]

    return render_json("Retrieved Campaigns is successfully", 200, "success", campaign_datas)


@campaign_bp.route('/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return render_json("Campaign not found", 404, "error", None)
    
    campaign_data = {
        'id': campaign.id, 
        'user_id': campaign.user_id, 
        'short_description': campaign.short_description, 
        'description': campaign.description, 
        'goal_amount': campaign.goal_amount, 
        'current_amount': campaign.current_amount, 
        'perks': campaign.perks,
        'backer_count': campaign.backer_count, 
        'slug': campaign.slug
    }

    return render_json("Retrieved one campaign", 200, "success", campaign_data)

@campaign_bp.route('/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return render_json("Campaign not found", 404, "error", None)
    
    data = request.get_json()
    campaign.short_description = data.get('short_description', campaign.short_description)
    campaign.description = data.get('description', campaign.description)
    campaign.goal_amount = data.get('goal_amount', campaign.goal_amount)
    campaign.current_amount = data.get('current_amount', campaign.current_amount)
    campaign.perks = data.get('perks', campaign.perks)
    campaign.backer_count = data.get('backer_count', campaign.backer_count)
    campaign.slug = data.get('slug', campaign.slug)
    
    # db.session.commit()
    error_response = handle_db_commit(db)
    if error_response:
        return error_response
    
    campaign_data = {
        'id': campaign.id, 
        'user_id': campaign.user_id, 
        'short_description': campaign.short_description, 
        'description': campaign.description, 
        'goal_amount': campaign.goal_amount, 
        'current_amount': campaign.current_amount, 
        'perks': campaign.perks,
        'backer_count': campaign.backer_count, 
        'slug': campaign.slug
    }
    
    return render_json("Updated one campaign", 200, "success", campaign_data)

@campaign_bp.route('/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if campaign is None:
        return render_json("Campaign not found", 404, "error", None)

    db.session.delete(campaign)
    db.session.commit()
    return render_json("Delete one campaign", 200, "success", None)