from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__, template_folder='VasecomProject/', static_folder='VasecomProject/')

# Configure MySQL
db = MySQLdb.connect(
    host='mysql-server',
    user='admin',
    password='AK@1234',
    db='akusers'
)

cursor = db.cursor()

# Create a table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
''')
db.commit()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
     if request.method == 'POST':
        username = request.form['signupUsername']
        email = request.form['signupPassword']

        # Insert data into the database
        cursor.execute('INSERT INTO users (username, email) VALUES (%s, %s)', (username, email))
        db.commit()

        return render_template('products.html')
     
     return render_template('signup.html')


@app.route('/ordered')
def ordered():
    cursor.execute('SELECT username FROM users')
    usernames = [user[0] for user in cursor.fetchall()]

    return render_template('ordered.html', usernames=usernames)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
