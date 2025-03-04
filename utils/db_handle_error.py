from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from utils.json_response import render_json

def handle_db_commit(db):
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return render_json("Database Integrity error", 400, "error", str(e))
    except SQLAlchemyError as e:
        db.session.rollback()
        return render_json("Database error occurred", 500, "error", str(e))
    return None
