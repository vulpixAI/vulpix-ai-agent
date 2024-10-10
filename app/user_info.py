# user_info.py
from db_connection import get_db_connection

def get_user_info(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user_info = cursor.fetchone()
    cursor.close()
    conn.close()
    return user_info
