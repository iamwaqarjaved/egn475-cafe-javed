# Import the Flask class so I can build a web application.
from flask import Flask

# Create my Flask application using this Python file.
app = Flask(__name__)

# Connect the website's main homepage URL to the function below.
@app.route("/")
# Define the function that handles requests to the homepage.
def home():
    # Display a welcome message when someone visits the homepage.
    return "Welcome to Bella Vista Cafe"

# Connect the about page URL to the function below.
@app.route("/about")
# Define the function that handles requests to the about page.
def about():
    # Display a short description of Bella Vista Cafe.
    return "Bella Vista Cafe is a family-owned cafe serving fresh coffee and homemade food."