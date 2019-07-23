import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'abcdefg'

DEBUG = True

DATABASE = {
    'postgre': {
        'id': 'postgres',
        'passwd': 'test123',
        'name': 'test',
        'host': 'localhost',
        'port': '5432',
        'isolation_level': 'READ UNCOMMITTED',
        
    }
}
