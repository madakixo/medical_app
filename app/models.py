from app import db

class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    body_part = db.Column(db.String(50))
    severity = db.Column(db.Integer)

class Disease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))

class SymptomDisease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptom.id'), nullable=False)
    disease_id = db.Column(db.Integer, db.ForeignKey('disease.id'), nullable=False)
    probability = db.Column(db.Float)
    symptom = db.relationship('Symptom', backref='disease_associations')
    disease = db.relationship('Disease', backref='symptom_associations')

# Add models for Medications, Patients, etc., if needed
