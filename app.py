import re
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for sessions to work

# 1. ADD THIS HOME ROUTE TO FIX THE 404 ERROR
@app.route('/')
def home():
    return render_template('login.html')  # Change 'login.html' to whatever your login page file is named

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '').strip().lower()
    
    # Student pattern: 7 digits followed by @sacs.edu.ph
    student_pattern = r'^\d{7}@sacs\.edu\.ph$'
    
    # Teacher pattern: 1-2 letters, dot, surname letters, @sacs.edu.ph
    teacher_pattern = r'^[a-z]{1,2}\.[a-z]+@sacs\.edu\.ph$'
    
    if re.match(student_pattern, email):
        session['user'] = email
        return redirect(url_for('student_page'))
        
    elif re.match(teacher_pattern, email):
        session['user'] = email
        return redirect(url_for('teacher_portal'))
        
    else:
        return render_template('login.html', error="Invalid email format. Please check your school email.")

@app.route('/teacher-portal')
def teacher_portal():
    if 'user' not in session:
        return redirect(url_for('home'))
    return render_template('teacher_portal.html')

@app.route('/compose')
def student_page():
    return render_template('compose.html')

if __name__ == '__main__':
    app.run(debug=True)