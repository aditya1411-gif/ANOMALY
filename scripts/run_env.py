from env.environment import PromptEnv
from agent.baseline_agent import agent

env = PromptEnv(difficulty="easy")

state = env.reset()
print("INPUT:", state)

action = agent(state)
print("AGENT OUTPUT:", action)

result = env.step(action)
print("RESULT:", result)


# ---- To run this code ----       :   python -m scripts.run_env