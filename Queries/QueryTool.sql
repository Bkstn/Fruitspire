from sqlalchemy import text
from db.models import db

with app.app_context():
    db.session.execute(text("""
        INSERT INTO food_items (name, date_expire)
        VALUES ('Banfaaaaaaaaaaana', '2026-06-25')
    """))
    db.session.commit()