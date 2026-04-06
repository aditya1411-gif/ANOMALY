from env.tasks import load_task
from env.grader import grade

class PromptEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.current_sample = None

    def reset(self):
        self.current_sample = load_task(self.difficulty)
        return self.current_sample["input"]

    def step(self, action):
        truth = self.current_sample

        reward = grade(action, truth)

        done = True

        return {
            "reward": reward,
            "done": done,
            "truth": truth
        }

# Testing the above code

if __name__ == "__main__":
    env = PromptEnv()

    state = env.reset()
    print("INPUT:", state)

    # dummy agent output
    action = {
        "is_attack": True,
        "type": "prompt_injection"
    }

    result = env.step(action)
    print("RESULT:", result)