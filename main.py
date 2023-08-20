from flask import Flask, render_template ,request,redirect,session
import os
import pymysql

app = Flask(__name__,template_folder="templates")
app.secret_key=os.urandom(24)

conn=pymysql.connect(host="localhost",user="root",password="",database="hacknova")
Cursor=conn.cursor()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login.html')
def Login():
    return render_template('login.html')

@app.route('/register.html')
def register():
    return render_template('register.html') 

@app.route('/logout')
def logout():
    session.pop('user_Id')
    return redirect('/')

@app.route('/feedback.html')
def contact():
    if 'user_Id' in session:
        if 'user_Id' or 'email' in session:
            user_Id = session['user_Id']  
            email = session['email']
            # name = session['name']
            return render_template('feedback.html', email=email)
        elif 'user_Id' not in session:
            return redirect('/login.html')
        else:
            user_Id = None
            return render_template('feedback.html', user_Id=user_Id) 
    else:
        return render_template('login.html')

@app.route('/welcome.html')
def home():
    if 'user_Id' or 'email' in session:
        user_Id = session['user_Id']  
        email = session['email']
        # name = session['name']
        return render_template('welcome.html', email=email)
    elif 'user_Id' not in session:
        return redirect('/login.html')
    else:
        user_Id = None
        return render_template('welcome.html', user_Id=user_Id)

@app.route('/courses.html')
def courses():
    if 'user_Id' in session:
        if 'user_Id' or 'email' in session:
            user_Id = session['user_Id']  
            email = session['email']
            # name = session['name']
            return render_template('courses.html', email=email)
        elif 'user_Id' not in session:
            return redirect('/login.html')
        else:
            user_Id = None
            return render_template('courses.html', user_Id=user_Id) 
    else:
        return render_template('login.html')



@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    Cursor.execute(""" SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE '{}'  """.format(email,password))
    login = Cursor.fetchall()
    if len(login)>0:
        session['user_Id']=login[0][0] 
        session['email']=login[0][1]       #to print the name of the perticular logged in user
        return redirect('/welcome.html')
    else:
        return render_template('/login.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')

    Cursor.execute(""" INSERT INTO `login` (`user_Id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')  """.format(name,email,password))
    conn.commit()

    Cursor.execute(""" SELECT * FROM `login` WHERE `email` LIKE '{}' """.format(email))
    myuser = Cursor.fetchall()
    session['user_Id'] = myuser[0][0]
    return redirect("/login.html")


@app.route('/feedback.html', methods=['POST'])
def contact_us():
    name=request.form.get('name')
    email=request.form.get('email')
    message=request.form.get('message')

    Cursor.execute(""" INSERT INTO `contact_us` (`user_Id`,`name`,`email`,`message`) VALUES (NULL,'{}','{}','{}')  """.format(name,email,message))
    conn.commit()

    return redirect("/feedback.html")



#Language Page

@app.route('/Languages/c.html')
def c():
    return render_template('Languages/c.html')

@app.route('/Languages/course_c.html')
def c_c():
    return render_template('Languages/course_c.html')

@app.route('/Languages/cpp.html')
def cpp():
    return render_template('Languages/cpp.html')

@app.route('/Languages/course_cpp.html')
def c_cpp():
    return render_template('Languages/course_cpp.html')

@app.route('/Languages/java.html')
def j():
    return render_template('Languages/java.html')

@app.route('/Languages/course_java.html')
def c_j():
    return render_template('Languages/course_java.html')

@app.route('/Languages/python.html')
def py():
    return render_template('Languages/python.html')

@app.route('/Languages/course_python.html')
def c_py():
    return render_template('Languages/course_python.html')


#Development Page

@app.route('/development/fed.html')
def fed():
    return render_template('development/fed.html')

@app.route('/development/course_fed.html')
def c_fed():
    return render_template('/development/course_fed.html')

@app.route('/development/bed.html')
def bed():
    return render_template('development/bed.html')

@app.route('/development/course_bed.html')
def c_bed():
    return render_template('/development/course_bed.html')

@app.route('/development/ds.html')
def ds():
    return render_template('development/ds.html')

@app.route('/development/course_ds.html')
def c_ds():
    return render_template('/development/course_ds.html')

@app.route('/development/ml.html')
def ml():
    return render_template('development/ml.html')

@app.route('/development/course_ml.html')
def c_ml():
    return render_template('/development/course_ml.html')

#Data 
@app.route('/dsa/stack.html')
def stack():
    return render_template('dsa/stack.html')

@app.route('/dsa/course_stack.html')
def c_stack():
    return render_template('dsa/course_stack.html')

@app.route('/dsa/queue.html')
def queue():
    return render_template('dsa/queue.html')

@app.route('/dsa/course_queue.html')
def c_queue():
    return render_template('dsa/course_queue.html')

@app.route('/dsa/gnt.html')
def gnt():
    return render_template('dsa/gnt.html')

@app.route('/dsa/course_gnt.html')
def c_gnt():
    return render_template('dsa/course_gnt.html')

app.run(debug=True)