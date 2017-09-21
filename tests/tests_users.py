"""
Module contains user tests
"""
import flask
import tests.tests_base
from app.models import Users

class UserTests(tests.tests_base.BaseDrinksTestCase):
    def login(self, email, password):
        return self.app.post('/user/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)
 
    def logout(self):
        return self.app.get('/user/logout', follow_redirects=True)
 
    def create(self, first_name, second_name, email, password, phonenumber):
        return self.app.post('user/create', data=dict(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password=password,
            phonenumber=phonenumber
        ), follow_redirects=True)
 
    def test_page_not_found(self):
        """Pages which dont exist should be directed to a 404 page"""
        response = self.app.get('/a-page-which-doesnt-exist')
        self.assertTrue(b'404 Page not found!' in response.data)
 
    def test_sign_in_page_loads(self):
        """Sign in page loads successfully"""
        response = self.app.get('user/login')
        self.assertTrue(b'Sign in' in response.data)
 
    def test_login_success_message(self):
        """Should display successfully logged in message"""
        response = self.login('admin@admin.local', 'default')
        self.assertTrue(b'You have successfully logged in' in response.data)
 
    def test_login_success_session(self):
        """Successfull login should put user_name in session"""
        with self.app as c:
            rv = self.login('admin@admin.local', 'default')
            self.assertTrue('user_name' in flask.session)
 
    def test_logout_success(self):
        """Successfull logout should remove user-name from session"""
        with self.app as c:
            self.login('admin@admin.local', 'default')
            rv = self.logout()
            self.assertTrue('user_name' not in flask.session)
 
    def test_login_failed_bad_password(self):
        """Failed Logins with bad password should display failure message"""
        rv = self.login('admin@admin.local', 'defaultx')
        self.assertTrue(b'Invalid Username or Password!' in rv.data)
 
    def test_login_failed_bad_username(self):
        """Failed Logins with bad username should display failure message"""
        rv = self.login('adminx@admin.loc', 'default')
        self.assertTrue(b'Invalid Username or Password!' in rv.data)
 
    def test_user_creation_success(self):
        """User should be found in the database after creation"""
        with self.app as c:
            self.create('test',
                        'subject',
                        'test@admin.local',
                        'secret',
                        '0724820290')
            user = Users.query.filter_by(email='test@admin.local').count()
            self.assertTrue(user == 1)
    def test_user_creation_wrongemail(self):
        """failed to create user with bad email should display failure message"""
        with self.app as c:
            response = self.create('test',
                                   'test name',
                                   'email.only',
                                   'default',
                                   '0724820290')
            self.assertTrue(b'Invalid email, enter a valid email' in response.data)
    def test_user_creation_failed_wrongphonrnumber(self):
        """Failed to create user with bad phone number should display failure message"""
        with self.app as c:
            response = self.create('test',
                                   'test name',
                                   'email.only',
                                   'default',
                                   '123456')
            self.assertTrue(b'Invalid phonenumber, enter a valid phonenumber' in response.data)
    def test_user_creation_failed_duplicate_email(self):
        """failed to create user with duplicate email should display failure message"""
        with self.app as c:
            self.create('test',
                        'test name',
                        'email@drinks.com',
                        'default',
                        '0724820290')
            response = self.create('test2',
                                   'test name2',
                                   'email@drinks.com',
                                   'default2',
                                   '0724820291')
            self.assertTrue(b'Email already taken' in response.data)
            
    def test_user_creation_failed_duplicate_phonenumber(self):
        """failed to create user with duplicate phonenumber"""
        with self.app as c:
            self.create('test',
                        'test name',
                        'email2@drinks.com',
                        'default',
                        '0724820290')
            response = self.create('test2',
                                   'test name2',
                                   'email@drinks.com',
                                   'default2',
                                   '0724820290')
            self.assertTrue(b'Phonenumber already in use' in response.data)
if __name__ == '__main__':
    unittest.main()
    