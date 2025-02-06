# Importing Flask framework for web development
from flask import Flask

# Generating a random number between 0 and 9
import random as rnd
num = rnd.randint(0, 9)
print(num)

# Creating a Flask web application instance
app = Flask(__name__)

# Defining the home route ('/') of the application
@app.route("/")
def hello_world():
    """Displays a greeting message and an image."""
    return '<h1 style="text-align:center">Guess a number between 0 and 9</h1>'\
           '<img align="middle" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200">'

# Defining a dynamic route that takes an integer input from the user
@app.route("/<int:guess>")
def guess_number(guess):
    """Compares user's guess with the randomly generated number and returns feedback."""
    if guess > num:
        return '<h1 style="text-align:center; color:purple;">Too high, try again!</h1>'\
               '<img align="middle" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="200">'
    elif guess < num:
        return '<h1 style="text-align:center; color:red;">Too Low, try again!</h1>'\
               '<img align="middle" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="200">'
    else:
        return '<h1 style="text-align:center; color:green;">You found me!</h1>'\
               '<img align="middle" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="200">'

# Running the Flask application only if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Enables debug mode for easier development
