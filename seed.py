
from app import create_app
from app.models import  Hero, Power, HeroPower
from app.extensions import db


app = create_app()

with app.app_context():
    
    db.drop_all()
    db.create_all()


    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Bruce Wayne", super_name="Batman")
    hero3 = Hero(name="Diana Prince", super_name="Wonder Woman")


    power1 = Power(name="Super Strength", description="Gives the wielder super-human strength.")
    power2 = Power(name="Flight", description="Allows the hero to fly through the air at great speeds.")
    power3 = Power(name="Invisibility", description="Allows the hero to become invisible to the naked eye.")


    db.session.add_all([hero1, hero2, hero3, power1, power2, power3])
    db.session.commit()


    hp1 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)
    hp2 = HeroPower(strength="Average", hero_id=hero1.id, power_id=power2.id)
    hp3 = HeroPower(strength="Weak", hero_id=hero2.id, power_id=power3.id)

    db.session.add_all([hp1, hp2, hp3])
    db.session.commit()

    print(" Database seeded successfully!")
