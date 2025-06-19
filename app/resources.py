
# app/resources.py
from flask_restful import Resource
from flask import request
from app.models import Power, Hero, HeroPower
from app.extensions import db

class PowerList(Resource):
    def get(self):
        return [power.to_dict() for power in Power.query.all()]

class PowerDetail(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if power:
            return power.to_dict()
        return {"error": "Power not found"}, 404

    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404

        data = request.get_json()
        description = data.get("description")

        if not description or len(description) < 20:
            return {"errors": ["validation errors"]}, 400

        power.description = description
        db.session.commit()
        return power.to_dict()

class HeroPowerCreate(Resource):
    def post(self):
        data = request.get_json()
        strength = data.get("strength")
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")

        if strength not in ["Strong", "Weak", "Average"]:
            return {"errors": ["validation errors"]}, 400

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return {"errors": ["validation errors"]}, 400

        hero_power = HeroPower(
            strength=strength,
            hero_id=hero_id,
            power_id=power_id
        )
        db.session.add(hero_power)
        db.session.commit()

        return hero_power.to_dict(), 201
def register_resources(api):
      api.add_resource(PowerList, "/api/powers")
      api.add_resource(PowerDetail, "/api/powers/<int:id>")
      api.add_resource(HeroPowerCreate, "/api/hero_powers")

