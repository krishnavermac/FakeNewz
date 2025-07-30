from flask import Flask, render_template
import random

app = Flask(__name__)

subjects = [
    "Rebel Kid", "Wizard Lizard", "Bulbasaur", "Triceratops", "Bumblebee",
    "Optimus Prime", "Dogesh Kumar", "Captain Chaiwala", "AI Overlord",
    "Mr. Beast Clone", "Alien Ramu", "Cyber Baba"
]

actions = [
    "runs away 🏃‍♂️", "attacks with a sword ⚔️", "declares war on 🔥", 
    "performs a salsa dance 💃", "breaks into tears 😢", "steals a spaceship 🚀",
    "starts a rap battle 🎤", "casts a fireball 🔥", "summons backup 🛡️"
]

places = [
    "the enchanted forest 🌳", "Genie's castle 🏰", "the city of dreams 🏙️", 
    "the underwater kingdom 🐠", "hell 🔥", "heaven ☁️", "a dark cave 🕳️", 
    "Goa beach 🌴", "a haunted mansion 🏚️", "the metaverse 🌐"
]

def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    return f"🚨 BREAKING NEWS!!! {subject} {action} in {place} 🚨"

@app.route("/")
def index():
    headline = generate_headline()
    return render_template("index.html", headline=headline)

if __name__ == "__main__":
    app.run(debug=True)
