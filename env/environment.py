from env.tasks import load_all_tasks
from env.grader import grade


class Environment:
    def __init__(self, difficulty="easy"):
        self.tasks = load_all_tasks(difficulty)
        self.current_index = 0
        self.current_task = None

    def reset(self):
        self.current_index = 0
        self.current_task = self.tasks[self.current_index]
        return self.current_task["input"]

    def step(self, action):
        truth = self.current_task

        # Calculate reward
        reward = grade(action, truth)

        # Move to next task
        self.current_index += 1

        done = self.current_index >= len(self.tasks)

        if not done:
            self.current_task = self.tasks[self.current_index]
            next_state = self.current_task["input"]
        else:
            next_state = None

        info = {
            "truth": truth
        }

        return next_state, reward, done, info