from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="charity_db",
        user="postgres",
        password="yourpassword"  # Replace with your actual password
    )
    return conn

# Handle donations
@app.route('/api/donations', methods=['POST'])
def add_donation():
    data = request.json
    name = data['name']
    email = data['email']
    amount = data['amount']
    message = data.get('message', '')
    donation_type = data['donation_type']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO donations (name, email, amount, message, donation_type) VALUES (%s, %s, %s, %s, %s)',
        (name, email, amount, message, donation_type)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"status": "success", "message": "Donation added!"})

# Fetch donations to display
@app.route('/api/data', methods=['GET'])
def get_donations():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM donations ORDER BY created_at DESC')
    donations = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(donations)

if __name__ == '__main__':
    app.run(debug=True)
