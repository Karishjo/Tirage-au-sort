from apps import db
from models import main, jeune, enfant

def populate():
    # MAIN: 100-175
    for n in range(100, 176):
        db.session.add(main(num=n, status=False))

    # JEUNE: 20-50
    for n in range(20, 51):
        db.session.add(jeune(num=n, status=False))

    # ENFANT: 1–13
    for n in range(1, 15):
        db.session.add(enfant(num=n, status=False))

    db.session.commit()

if __name__ == "__main__":
    populate()

