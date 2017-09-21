"""
Modoule provides the module tests of the database
"""
import os
import unittest
import sys

TOPDIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(TOPDIR)

from werkzeug.security import generate_password_hash
from app import APP, DB
from app.models import Users
from config import BASE_DIR

class BaseDrinksTestCase(unittest.TestCase):
    """
    Class handles all the basic tests
    """
    def setUp(self):
        APP.config['TESTING'] = True
        APP.config['CSRF_ENABLED'] = False
        APP.config['WTF_CSRF_ENABLED'] = False
        APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR, 'drinksdb')
        self.app = APP.test_client()
        self.db = DB
        self.db.create_all()

        if Users.query.filter_by(first_name='admin').count() == 0:
            self.user = Users(first_name='admin',
                              second_name='istrator',
                              phonenumber='0712345678',
                              email='admin@drinksapi.local',
                              password=generate_password_hash('default'))
            self.db.session.add(self.user)
            self.db.session.commit()
    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    if __name__ == '__main__':
        unittest.main()
