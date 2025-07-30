import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

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

    headline = f"{Fore.RED + Style.BRIGHT}\n🚨 BREAKING NEWS!!! {subject} {action} in {place} 🚨"
    return headline

def main():
    print(f"{Fore.CYAN + Style.BRIGHT}📰 Welcome to the Fake News Headline Generator!\n")
    while True:
        time.sleep(0.5)
        print(generate_headline())

        user_input = input(f"{Fore.YELLOW}\nWant another headline? (yes/no): ").strip().lower()
        if user_input == "no":
            break
        elif user_input != "yes":
            print(f"{Fore.RED}Invalid input. Please type 'yes' or 'no'.")
    print(f"\n{Fore.GREEN}Thanks for using the Fake News Headline Generator. Have a funny day! 😄")

if __name__ == "__main__":
    main()
