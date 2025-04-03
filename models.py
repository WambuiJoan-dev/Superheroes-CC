from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from app import db


class Hero(db.Model, SerializerMixin):
    __tablename__='heroes'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan")

class Power(db.Model, SerializerMixin):
    __tablename__='powers'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan")
    serialize_rules = ('-hero_powers.power',)

class HeroPower(db.Model, SerializerMixin):
    __tablename__='hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey(heroes.id), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey(powers.id), nullable=False)

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers')