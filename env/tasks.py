import json
import random

def load_task(difficulty="easy"):
    with open(f"data/{difficulty}.json") as f:
        data = json.load(f)

    return random.choice(data)

# Testing the above code

if __name__ == "__main__":
    sample = load_task("easy")
    print(sample)