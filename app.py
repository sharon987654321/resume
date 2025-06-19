from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'resume_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        cell = request.form['cell']
        email = request.form['email']
        address = request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact (name, cell, email, address) VALUES (%s, %s, %s, %s)",
                    (name, cell, email, address))
        mysql.connection.commit()
        cur.close()
        return "Message Sent Successfully!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)