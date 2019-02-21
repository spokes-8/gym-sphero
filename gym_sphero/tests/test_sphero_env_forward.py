import gym
import gym_sphero

def main():
    env = gym.make('Sphero-v0')
    obs = env.reset()
    print(f'Initial Obs: {obs}')

    total_reward = 0

    action = [20, 0]
    for _ in range(20):
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        print(f'Action: {action}')
        print(f'Previous observertion: {obs}')

    env.reset()
    print(f'Total Reward: {total_reward}')

if __name__ == '__main__':
    main()