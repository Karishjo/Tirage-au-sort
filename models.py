from apps import db

class main(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)

    def __init__(self, num, status=False):
        self.num = num
        self.status = status

class jeune(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)

    def __init__(self, num, status=False):
        self.num = num
        self.status = status

class enfant(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    num = db.Column("Number", db.Integer)
    status = db.Column("Status", db.Boolean)

    def __init__(self, num, status=False):
        self.num = num
        self.status = status
