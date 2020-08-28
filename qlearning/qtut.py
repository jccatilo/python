import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

LEARNING_RATE = 0.1 #0 TO 1. KEEP AS LOW AS POSSIBLE
DISCOUNT = 0.95 #FUTURE SOMETHING
EPISODES = 25000

SHOW_EVERY = 2000#let us know if ure still alive hehe

DISCRETE_OS_SIZE = [20]*len(env.observation_space.high) #you separate 0.6 to -1.2 into 20 discrete levels
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE
epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES //2
epsilon_decay_value = epsilon/(END_EPSILON_DECAYING- START_EPSILON_DECAYING)

q_table = np.random.uniform(low = -2, high = 0, size  = (DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state (state):
    discrete_state = (state  -env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int))
for episode in range(EPISODES):
    if episode % SHOW_EVERY ==0:
        print(episode)
        render = True
    else:
        render = False
    discrete_state = get_discrete_state(env.reset())
    #print(discrete_state)
    #print(np.argmax(q_table[discrete_state]))# to get max value
    done = False
    while not done:
        if np.random.random()>epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _=env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        if render:
            env.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])#this is where te magic happens
            current_q = q_table[discrete_state+(action, )]
            new_q =(1-LEARNING_RATE* current_q + LEARNING_RATE * (reward + DISCOUNT*max_future_q))
            q_table[discrete_state+(action, )] = new_q
        elif new_state[0]>= env.goal_position:
            print(f"We made it on episode{episode}!!!")
            q_table[discrete_state+(action,)] = 0
        
        discrete_state = new_discrete_state
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value
env.close()