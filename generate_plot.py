import numpy as np
import matplotlib.pyplot as plt

sample_space = range(1, 10000)
win_value = []
doors = np.array([1, 0, 0])
for i in sample_space:
    np.random.shuffle(doors) #shuffles in-place
    chosen_door = np.random.choice([0, 1, 2])
    idx = np.delete([0, 1, 2], chosen_door)
    if doors[chosen_door] == 1:
        open_door = np.random.choice(idx)
    else:
        open_door = np.where(doors[idx[0]] == 0, idx[0], idx[1])
    chosen_door = int(np.delete([0, 1, 2], (chosen_door, open_door)))
    win_value.append(doors[chosen_door])
frac_switching = np.cumsum(win_value)/sample_space

win_value = []
for i in sample_space:
    np.random.shuffle(doors) #shuffles in-place
    chosen_door = np.random.choice([0, 1, 2])
    idx = np.delete([0, 1, 2], chosen_door)
    if doors[chosen_door] == 1:
        open_door = np.random.choice(idx)
    else:
        open_door = np.where(doors[idx[0]] == 0, idx[0], idx[1])
    win_value.append(doors[chosen_door])
frac_staying = np.cumsum(win_value)/sample_space

one_third = np.full(len(sample_space), 0.3333)
two_thirds = np.full(len(sample_space), 0.6666)

plt.figure(figsize = (7, 4), dpi = 150)
plt.plot(sample_space, frac_staying, label = "Staying", linewidth = 1.1)
plt.plot(sample_space, one_third, alpha = 0.5, color = "black", linewidth = 0.5)
plt.plot(sample_space, frac_switching, label = "Switching", linewidth = 1.1)
plt.plot(sample_space, two_thirds, alpha = 0.5, color = "black", linewidth = 0.5)
plt.xticks([0, 2000, 4000, 6000, 8000, 10000])
plt.yticks([0, 0.3333, 0.6666, 1.0], labels = [0.0, 0.3, 0.6, 1.0])
plt.xlabel("Number of iterations", labelpad = 10)
plt.ylabel("Probability of winning")
plt.legend(loc = 'upper right')
plt.savefig('plot.png', bbox_inches = 'tight')
