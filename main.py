from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import random


# Initialize App and Flask and Friends
app = Flask(__name__)
Bootstrap(app)


# Prompts

prompts = [
    "What would you like to get done today?",
    "Who is someone you love and why?",
    "A Hero's Journey",
    "Favorite Pokemon and Why"
]



# Back End

@app.route('/')
def home():
    prompt = random.choice(prompts)

    return render_template('index.html', prompt=prompt)































if __name__ == "__main__":
    app.run(debug=True)

