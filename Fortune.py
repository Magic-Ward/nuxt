import random
import time

fortunes = [
    "You will find a missing sock today.",
    "Beware of ducks — they might be watching.",
    "A mysterious stranger will compliment your variable names.",
    "Your next bug will fix itself. Maybe.",
    "Someone will merge your pull request without comments!",
    "Your coffee will be at perfect temperature for 3 seconds.",
    "Today is a good day to rename your files properly.",
]

print("Consulting the code spirits...")
time.sleep(1.5)
print("Generating your fortune...\n")
time.sleep(1.5)

fortune = random.choice(fortunes)
print(f"🔮 Your coding fortune: {fortune}")
