from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import bcrypt
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# MYSQL CONFIG
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'smart_college'

mysql = MySQL(app)

# ------------------ STUDENT REGISTER ------------------
@app.route('/register_student', methods=['POST'])
def register_student():
    data = request.json
    print("Received Data:", data)  # 🔥 ADD THIS


    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO students 
        (name, reg_no, roll_no, email, class, degree, department, hod_name, advisor_name, phone, username, password)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['name'], data['reg_no'], data['roll_no'], data['email'],
        data['class'], data['degree'], data['department'],
        data['hod_name'], data['advisor_name'], data['phone'],
        data['username'], password
    ))
    mysql.connection.commit()

    return jsonify({"message": "Student Registered Successfully"})

# ------------------ STAFF REGISTER ------------------
@app.route('/register_staff', methods=['POST'])
def register_staff():
    data = request.json

    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO staff 
        (name, staff_id, department, subject, phone, username, password)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['name'], data['staff_id'], data['department'],
        data['subject'], data['phone'],
        data['username'], password
    ))
    mysql.connection.commit()

    return jsonify({"message": "Staff Registered Successfully"})

# ------------------ LOGIN ------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    cur = mysql.connection.cursor()

    # Check student
    cur.execute("SELECT password FROM students WHERE username=%s", (username,))
    student = cur.fetchone()

    if student and bcrypt.checkpw(password.encode('utf-8'), student[0].encode('utf-8')):
        return jsonify({"status": "success", "role": "student"})

    # Check staff
    cur.execute("SELECT password FROM staff WHERE username=%s", (username,))
    staff = cur.fetchone()

    if staff and bcrypt.checkpw(password.encode('utf-8'), staff[0].encode('utf-8')):
        return jsonify({"status": "success", "role": "staff"})

    return jsonify({"status": "error", "message": "Invalid Credentials"})

if __name__ == '__main__':
    app.run(debug=True)