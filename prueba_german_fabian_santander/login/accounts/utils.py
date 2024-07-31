from django.db import connections
from django.db.utils import OperationalError

def check_database_connection():
    db_conn = connections['default']
    try:
        db_conn.cursor()
        return True
    except OperationalError:
        return False