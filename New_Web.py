from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return '<h1>Welcome to My Website!</h1><p>This is a simple Flask app.</p>'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
