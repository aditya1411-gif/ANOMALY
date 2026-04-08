import json
import random

# Existing (keep this)
def load_task(difficulty="easy"):
    with open(f"data/{difficulty}.json") as f:
        data = json.load(f)

    return random.choice(data)


# NEW FUNCTION (ADD THIS)
def load_all_tasks(difficulty="easy"):
    with open(f"data/{difficulty}.json") as f:
        data = json.load(f)

    return data

# ---- Testing the above code ----

# if __name__ == "__main__":
#     sample = load_task("easy")
#     print(sample)



#   ---- To run the test code ----

# python env/tasks.py