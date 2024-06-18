from flask import Flask,render_template
import random

app = Flask(__name__)

fun_facts = [
    "Australia is wider than the moon.",
    "Avocados are berries.",
    "Octopuses have three hearts.",
    "Allodoxaphobia is the fear of other people’s opinions.",
    "Human teeth are the only part of the body that cannot heal themselves.",
    "Google Images was created after Jennifer Lopez wore the green dress at the 2000 Grammys.",
    "Lemons float, but limes sink.",
    "The longest English word is 189,819 letters long.",
    "Neil Armstrong’s hair was sold in 2004 for $3,000.",
    "No number before 1,000 contains the letter A.",
    "The world’s longest concert lasted 453 hours.",
    "It's illegal to own only one guinea pig in Switzerland.",
    "The average cloud weighs over one million pounds.",
    "Bottlenose dolphins are the only other species to have names for themselves.",
    "Your brain alone burns around 400 to 500 calories each day.",
    "Snakes smell with their tongue."
]
@app.route('/')
def home():
    fact = random.choice(fun_facts)
    return render_template('index.html', fact=fact)

if __name__ == '__main__':
    app.run(debug=True)