
from flask import Blueprint, jsonify, request
from app.models import Hero, Power, HeroPower
from app.extensions import db

from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()])

@api.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify({
            **hero.to_dict(),
            "hero_powers": [
                {
                    **hp.to_dict(),
                    "power": hp.power.to_dict()
                } for hp in hero.hero_powers
            ]
        })
    return jsonify({"error": "Hero not found"}), 404

@api.route("/powers", methods=["GET"])
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()])

@api.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    return jsonify({"error": "Power not found"}), 404

@api.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["validation errors"]}), 400

    power.description = description
    db.session.commit()
    return jsonify(power.to_dict())

@api.route("/hero_powers", methods=["POST"])
def create_hero_power():
    data = request.json
    strength = data.get("strength")
    power_id = data.get("power_id")
    hero_id = data.get("hero_id")

    if strength not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["validation errors"]}), 400

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"errors": ["validation errors"]}), 400

    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(hero_power)
    db.session.commit()

    return jsonify(hero_power.to_dict()), 201
