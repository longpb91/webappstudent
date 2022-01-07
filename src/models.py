# from enum import unique


class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    clas = db.Column(db.String(200))
    subject = db.Column(db.Text())

    def __init__(self, id, name, clas, subject):
        self.id = id
        self.name = name
        self.clas = clas
        self.subject = subject

        