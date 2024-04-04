from flask import Flask, render_template, redirect, url_for,request ,session,flash
from flask_session import Session
import secrets
from flask_mysqldb import MySQL
import os

# from captcha.image import ImageCaptcha

app = Flask(__name__)

# # Create an instance of the ImageCaptcha class
# image_captcha = ImageCaptcha()

# # Generate a new captcha image and solution
# captcha_data = image_captcha.generate_captcha()
# captcha_image = captcha_data[0]
# captcha_solution = captcha_data[1]




# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '911262'
app.config['MYSQL_DB'] = 'school_result'

mysql = MySQL(app)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student')
def student_page():
    return render_template('student.html')


@app.route('/contact')
def contact_page():
    # Handle contact page logic and rendering
    return render_template('contact.html')

@app.route('/about')
def about_page():
    # Handle about page logic and rendering
    return render_template('about.html')



# Add routes for pay fees and view results pages
@app.route('/pay-fees')
def pay_fees():
    # Handle pay fees logic and rendering
    return render_template('pay_fees.html')

@app.route('/view-fees-paid')
def view_student_fees():

    return 'working on it'

@app.route('/check-result', methods=['GET', 'POST'])
def check_result():
    # if request.method == 'POST':
    #     roll_number = request.form['roll_number']
    #     mother_name = request.form['mother_name']

    #     # Connect to the MySQL database
    #     cur = mysql.connection.cursor()

    #     # Query to retrieve student data
    #     query = "SELECT * FROM students WHERE roll_number = %s AND mother_name = %s"
    #     cur.execute(query, (roll_number, mother_name))
    #     student = cur.fetchone()

    #     if student:
    #         name, roll_number, mother_name, percentage, physics, chemistry, mathematics, biology, it, english, rank = student
    #         passed = percentage >= 40
    #         cur.close()
    #         return render_template('view_result.html', student=student, passed=passed)
    #     else:
    #         cur.close()
    #         return r'Invalid roll number or mother\'s name.'

    return render_template('check_result.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    # if request.method == 'POST':
    #     full_name = request.form['full_name']
    #     mother_name = request.form['mother_name']
    #     roll_number = request.form['roll_number']
    #     amount = request.form['amount']

    #     # Split the full_name into surname, student name, and father's name
    #     name_parts = full_name.split(',')
    #     if len(name_parts) == 3:
    #         surname, student_name, father_name = [part.strip() for part in name_parts]
    #     else:
    #         name_parts = full_name.split()
    #         if len(name_parts) >= 3:
    #             surname = name_parts[0]
    #             student_name = ' '.join(name_parts[1:-1])
    #             father_name = name_parts[-1]
    #         else:
    #             return 'Invalid full name format.'

    #     # Connect to the MySQL database
    #     cur = mysql.connection.cursor()

    #     # Query to check if the student exists
    #     query = "SELECT * FROM students WHERE roll_number = %s"
    #     cur.execute(query, (roll_number,))
    #     student = cur.fetchone()

    #     if student:
    #         # Process payment logic here
    #         # ...

    #         # Redirect to a success page or display a success message
    #         return redirect(url_for('payment_success'))
    #     else:
    #         cur.close()
    #         return 'Invalid roll number.'

    return render_template('payment.html')

app.secret_key = secrets.token_hex(16)  # Generate a secret key for session encryption

# Configure the session to use server-side storage
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sessions')
Session(app)

# Teacher credentials (replace with your actual database or secure storage)
TEACHER_CREDENTIALS = {
    'admin': 'password'

    # Add more teacher IDs and passwords
}

@app.route('/teacher', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        password = request.form['password']

        # Check if the teacher ID and password match
        if teacher_id in TEACHER_CREDENTIALS and TEACHER_CREDENTIALS[teacher_id] == password:
            session['teacher_id'] = teacher_id  # Store the teacher_id in the session
            return redirect(url_for('teacher_dashboard'))
        else:
            error = 'Invalid Teacher ID or Password'
            return render_template('teacher.html', error=error)

    return render_template('teacher.html')

@app.route('/teacher_dashboard')
def teacher_dashboard():
    # Check if the user is authenticated (teacher_id in session)
    if 'teacher_id' in session:
        # Render the teacher dashboard template or perform other actions
        return render_template('teacher_dashboard.html')
    else:
        # Redirect to the teacher login page if not authenticated
        return redirect(url_for('teacher_login'))






app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sessions')
Session(app)

# Admin credentials (replace with your actual database or secure storage)
ADMIN_CREDENTIALS = {
    'admin': 'password'
    # Add more admin IDs and passwords
}

@app.route('/admin_check', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin_id = request.form['admin_id']
        password = request.form['password']

        # Check if the admin ID and password match
        if admin_id in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[admin_id] == password:
            session['admin_id'] = admin_id  # Store the admin_id in the session
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Invalid Admin ID or Password'
            return render_template('admin_check.html', error=error)

    return render_template('admin_check.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    # Check if the user is authenticated (admin_id in session)
    if 'admin_id' in session:
        # Render the admin dashboard template or perform other actions
        return render_template('admin_dashboard.html')
    else:
        # Redirect to the admin login page if not authenticated
        return redirect(url_for('admin_login'))

@app.route('/fill_result')
def fill_result():
    # Render the template for filling student results
    # or perform the necessary logic for filling results
    return render_template('fill_result.html')




@app.route('/submit_scores', methods=['POST'])
def submit_scores():
    if request.method == 'POST':
        # Get form data and remove leading/trailing whitespace
        name = request.form['name'].strip()
        mother_name = request.form['motherName'].strip()
        roll_no = request.form['rollNo'].strip()
        submission_date = request.form['submissionDate']
        physics = request.form['physics']
        chemistry = request.form['chemistry']
        biology = request.form['biology']
        math = request.form['math']

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Insert data into the student_scores table
        query = "INSERT INTO student_scores (name, mother_name, roll_no, submission_date, physics, chemistry, biology, math) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, mother_name, roll_no, submission_date, physics, chemistry, biology, math)
        cur.execute(query, values)

        # Commit the changes and close the connection
        mysql.connection.commit()
        cur.close()

        flash('Scores submitted successfully', 'success')
        return render_template('subject_score_submission.html')
    return 'Error: Invalid request method'


# @app.route('/delete_record', methods=['GET', 'POST'])
# def delete_record():
#     if request.method == 'POST':
#         roll_no = request.form['roll_no']
#         mother_name = request.form['mother_name']

#         # Connect to the MySQL database
#         cursor = mysql.connection.cursor()

#         # Delete the record from the student_scores table
#         query = "DELETE FROM student_scores WHERE roll_no = %s AND mother_name = %s"
#         values = (roll_no, mother_name)
#         cursor.execute(query, values)
#         mysql.connection.commit()

#         if cursor.rowcount > 0:
#             flash('Record deleted successfully', 'success')
#         else:
#             flash(r'No record found with the provided Roll Number and Mother\'s Name', 'error')

#         cursor.close()

#     return render_template('delete_record.html')

@app.route('/delete_record', methods=['GET', 'POST'])
def delete_record():
    if request.method == 'POST':
        roll_no = request.form['roll_no'].strip()
        mother_name = request.form['mother_name'].strip()

        # Connect to the MySQL database
        cursor = mysql.connection.cursor()

        # Delete the record from the student_scores table
        query = "DELETE FROM student_scores WHERE roll_no = %s AND mother_name = %s"
        values = (roll_no, mother_name)
        cursor.execute(query, values)
        mysql.connection.commit()

        if cursor.rowcount > 0:
            flash('Record deleted successfully', 'success')
        else:
            flash('No record found with the provided Roll Number and Mother\'s Name', 'error')

        cursor.close()

    return render_template('delete_record.html')

@app.route('/view-scores', methods=['GET'])
def view_scores():
    # Connect to the MySQL database
    cur = mysql.connection.cursor()

    # Execute a SELECT query to fetch all data from the student_scores table
    query = "SELECT * FROM student_scores"
    cur.execute(query)

    # Fetch all rows from the result
    rows = cur.fetchall()

    # Close the cursor
    cur.close()

    # Calculate total score, percentage, and rank for each student
    student_data = []
    for row in rows:
        id, name, mother_name, roll_no, submission_date, physics, chemistry, biology, math, created_at = row
        total_score = physics + chemistry + biology + math
        percentage = (total_score / 400) * 100
        student_data.append((id, name, mother_name, roll_no, submission_date, physics, chemistry, biology, math, total_score, percentage, created_at))

    # Sort the student data by total score in descending order
    student_data.sort(key=lambda x: x[9], reverse=True)

    # Assign ranks to students
    rank = 1
    ranked_student_data = []
    prev_score = None
    for data in student_data:
        if prev_score != data[9]:
            prev_score = data[9]
            rank = len(ranked_student_data) + 1
        ranked_student_data.append(data + (rank,))

    # Render the HTML template and pass the ranked student data
    return render_template('view_scores.html', students=ranked_student_data)


@app.route('/check-rank', methods=['GET', 'POST'])
def check_rank():
    if request.method == 'POST':
        roll_number = request.form['roll_no'].strip()
        mother_name = request.form['mother_name'].strip()

        # Connect to the MySQL database
        cur = mysql.connection.cursor()

        # Query to retrieve student data
        query = "SELECT * FROM student_scores WHERE roll_no = %s AND mother_name = %s"
        cur.execute(query, (roll_number, mother_name))
        student = cur.fetchone()

        if student:
            # Unpack student data
            id, name, mother_name, roll_no, submission_date, physics, chemistry, biology, math, created_at = student

            # Calculate the total score and percentage
            total_score = physics + chemistry + biology + math
            percentage = (total_score / 400) * 100

            # Calculate the rank
            rank = calculate_rank(total_score)

            # Check if the student passed or failed
            passed = percentage >= 40

            # Render the success or failure template
            if passed:
                return render_template('success.html', name=name, roll_no=roll_no, score=percentage, rank=rank, physics=physics, chemistry=chemistry, biology=biology, math=math)
            else:
                return render_template('failure.html', name=name, roll_no=roll_no, score=percentage,rank=rank,physics=physics,chemistry=chemistry,biology=biology,math=math)
        else:
            cur.close()
            return r'Invalid roll number or mother\'s name.'

    # return render_template('check_result.html')
    return " what is missing"

def calculate_rank(total_score):
    # Connect to the MySQL database
    cur = mysql.connection.cursor()

    # Query to retrieve all student scores sorted by total score in descending order
    query = "SELECT id, physics + chemistry + biology + math AS total_score FROM student_scores ORDER BY total_score DESC"
    cur.execute(query)
    scores = cur.fetchall()

    # Find the rank of the student's score
    rank = 1
    prev_score = None
    for score in scores:
        if prev_score != score[1]:
            prev_score = score[1]
            if score[1] == total_score:
                break
            rank += 1

    cur.close()
    return rank

if __name__ == '__main__':
    app.run(debug=True)