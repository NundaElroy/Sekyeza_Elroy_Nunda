# Simple Reinforcement Learning Agent - Road Crossing
import numpy as np
import random

print("=== REINFORCEMENT LEARNING: ROAD CROSSING AGENT ===\n")

# ENVIRONMENT SETUP
# Road has 5 positions: [0, 1, 2, 3, 4]
# Agent starts at position 0, goal is to reach position 4 (across the road)
# Optimal path: Right -> Left -> Right (to avoid traffic)

positions = 5  # 5 positions on the road (0 to 4)
actions = 2   # 0: Move Left, 1: Move Right

# Initialize Q-table (all values start at 0)
Q = np.zeros((positions, actions))
print("Initial Q-table (all zeros):")
print("Positions: 0, 1, 2, 3, 4")
print("Actions: 0=Left, 1=Right")
print(Q)
print()

# LEARNING PARAMETERS
episodes = 500        # Number of training episodes
learning_rate = 0.8   # How fast the agent learns (0-1)
gamma = 0.9          # How much future rewards matter (0-1)
epsilon = 0.3        # Exploration rate (30% random actions)

print("TRAINING THE AGENT...")
print(f"Episodes: {episodes}, Learning Rate: {learning_rate}, Discount: {gamma}")
print()

# TRAINING LOOP
for episode in range(episodes):
    # Start at random position (but usually position 0)
    state = 0  # Always start from beginning of road
    
    # Agent takes actions until it reaches the goal or gets stuck
    steps_in_episode = 0
    max_steps = 10  # Prevent infinite loops
    
    while state != 4 and steps_in_episode < max_steps:
        # CHOOSE ACTION (Epsilon-greedy strategy)
        if random.uniform(0, 1) < epsilon:
            # EXPLORE: Choose random action
            action = random.randint(0, 1)
        else:
            # EXPLOIT: Choose best known action
            action = np.argmax(Q[state])
        
        # TAKE ACTION AND GET NEXT STATE
        if action == 0:  # Move Left
            next_state = max(0, state - 1)
        else:  # Move Right
            next_state = min(4, state + 1)
        
        # CALCULATE REWARD
        if next_state == 4:
            reward = 100  # Big reward for reaching goal!
        elif next_state == state:
            reward = -10  # Penalty for hitting boundary
        else:
            reward = -1   # Small penalty for each step
        
        # UPDATE Q-TABLE (Q-Learning Formula)
        old_q = Q[state, action]
        next_max = np.max(Q[next_state])
        new_q = old_q + learning_rate * (reward + gamma * next_max - old_q)
        Q[state, action] = new_q
        
        # Move to next state
        state = next_state
        steps_in_episode += 1

# SHOW RESULTS
print("TRAINING COMPLETE!")
print("\nFinal Q-table:")
print("     Left   Right")
for i in range(positions):
    print(f"Pos {i}: {Q[i,0]:6.1f} {Q[i,1]:6.1f}")

print()

# TEST THE TRAINED AGENT
print("TESTING THE TRAINED AGENT:")
print("Starting from position 0, trying to reach position 4...")
print()

state = 0
steps = 0
path = []

print("Agent's journey:")
while state != 4 and steps < 10:
    # Choose best action (no more exploration)
    action = np.argmax(Q[state])
    action_name = "Left" if action == 0 else "Right"
    
    # Take action
    if action == 0:
        next_state = max(0, state - 1)
    else:
        next_state = min(4, state + 1)
    
    print(f"Step {steps + 1}: Position {state} -> Action: {action_name} -> New Position: {next_state}")
    path.append(action_name)
    
    state = next_state
    steps += 1

print(f"\nAgent reached goal in {steps} steps!")
print(f"Action sequence: {' -> '.join(path)}")

# CHECK IF IT MATCHES REQUIRED PATTERN
required_pattern = ["Right", "Left", "Right"]
if len(path) >= 3 and path[:3] == required_pattern:
    print("✓ SUCCESS: Agent learned the required pattern (Right -> Left -> Right)!")
else:
    print(f"Pattern learned: {path}")
    print(f"Required pattern: {required_pattern}")


