from logic import SnakeEnv
from stable_baselines3 import DQN
import argparse

parser = argparse.ArgumentParser(
                    prog='snack4snake eval',
                    description='Runs snack4snake AI models')
parser.add_argument('model_path')

# Pfad zum Modell
model_path = parser.parse_args().model_path
model = DQN.load(model_path)


num_episodes = 100

# Ausführung
eval_env = SnakeEnv(render_mode="human")
obs, _ = eval_env.reset()

for _ in range(num_episodes):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = eval_env.step(action)

    if terminated or truncated:
        obs, _ = eval_env.reset()

eval_env.close()
