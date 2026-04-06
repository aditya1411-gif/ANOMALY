# print("FILE IS RUNNING")

def grade(pred, truth):
    reward = 0

    # Check if attack detection is correct
    if pred["is_attack"] == truth["is_attack"]:
        reward += 1

    # Check if attack type is correct
    if pred["type"] == truth["type"]:
        reward += 0.2

    return reward

# ---- Testing the above code ----

# if __name__ == "__main__":
#     pred = {"is_attack": True, "type": "prompt_injection"}
#     truth = {"is_attack": True, "type": "prompt_injection"}

#     print(grade(pred, truth))