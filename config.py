"""
Defining application directory
"""
import os
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
"""
Define database configuration
"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'drinksdb')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True
"""
Application threads
"""
THREADS_PER_PAGE = 2
"""
Security configurations
"""
CSRF_ENABLED = True
CSRF_SESSION_KEY = "s3ss10n_K3y"
SECRET_KEY = "s3CR3t_k3y"
