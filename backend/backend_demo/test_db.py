from backend.backend_wg.backend_first_test import db


def test_create_db():
    db.create_all()

