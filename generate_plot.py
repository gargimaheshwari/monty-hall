import numpy as np
import matplotlib.pyplot as plt

ss = range(1, 10000)
value = []
doors = np.array([1, 0, 0])
for i in ss:
    np.random.shuffle(doors) #shuffles in-place
    chosen_door = np.random.choice([0, 1, 2])
    idx = np.delete([0, 1, 2], chosen_door)
    if doors[chosen_door] == 1:
        open_door = np.random.choice(idx)
    else:
        open_door = np.where(doors[idx[0]] == 0, idx[0], idx[1])
    chosen_door = int(np.delete([0, 1, 2], (chosen_door, open_door)))
    value.append(doors[chosen_door])
frac = np.cumsum(value)/ss

value = []
for i in ss:
    np.random.shuffle(doors) #shuffles in-place
    chosen_door = np.random.choice([0, 1, 2])
    idx = np.delete([0, 1, 2], chosen_door)
    if doors[chosen_door] == 1:
        open_door = np.random.choice(idx)
    else:
        open_door = np.where(doors[idx[0]] == 0, idx[0], idx[1])
    value.append(doors[chosen_door])
frac_2 = np.cumsum(value)/ss

a = np.full(len(ss), 0.3333)
b = np.full(len(ss), 0.6666)

plt.figure(figsize = (7, 4), dpi = 150)
plt.plot(ss, frac_2, label = "Staying", linewidth = 1.1)
plt.plot(ss, a, alpha = 0.5, color = "black", linewidth = 0.5)
plt.plot(ss, frac, label = "Switching", linewidth = 1.1)
plt.plot(ss, b, alpha = 0.5, color = "black", linewidth = 0.5)
plt.xticks([0, 2000, 4000, 6000, 8000, 10000])
plt.yticks([0, 0.3333, 0.6666, 1.0], labels = [0.0, 0.3, 0.6, 1.0])
plt.xlabel("Number of iterations", labelpad = 10)
plt.ylabel("Probability of winning")
plt.legend(loc = 'upper right')
plt.savefig('plot.png', bbox_inches = 'tight')
