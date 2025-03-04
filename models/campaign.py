from models import db

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    short_description = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    goal_amount = db.Column(db.Integer, nullable=False)
    current_amount = db.Column(db.Integer, default=0)
    perks = db.Column(db.Text, nullable=True)
    backer_count = db.Column(db.Integer, default=0)
    slug = db.Column(db.String(255), unique=True, nullable=False)

    user = db.relationship('User', backref=db.backref('campaigns', lazy=True))