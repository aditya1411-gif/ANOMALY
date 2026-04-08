# Runs full evaluation pipeline and calculates overall agent performance

# Runs full evaluation loop:
# - Gets inputs from environment
# - Sends to LLM agent
# - Receives predictions
# - Evaluates using reward system
# - Prints total and average score

from env.environment import Environment
from agent.llm_agent import get_llm_response


def run_evaluation():
    env = Environment()

    total_reward = 0
    num_steps = 0

    state = env.reset()

    while True:
        # LLM agent prediction
        action = get_llm_response(state)

        # Environment evaluates
        next_state, reward, done, info = env.step(action)

        total_reward += reward
        num_steps += 1

        # Move to next state
        state = next_state

        if done:
            break

    print("\n===== Evaluation Complete =====")
    print(f"Total Steps: {num_steps}")
    print(f"Total Reward: {total_reward}")
    print(f"Average Score: {total_reward / num_steps:.2f}")


if __name__ == "__main__":
    run_evaluation()