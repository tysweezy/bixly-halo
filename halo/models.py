from halo import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Team {}>'.format(self.name)    

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.String(250), index=True)
    gamer_tag = db.Column(db.String(250), index=True)
    exp_points = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'),
        nullable=False)

    def __repr__(self):
        return '<Player {}>'.format(self.real_name)