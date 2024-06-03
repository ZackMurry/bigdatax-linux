from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(8, 12))
ax.set_title('Dataset Generation and Sorting Times vs. N')

file = open('time.txt', 'r')

file.readline() # Toss first line

N_data = []
create_data = []
sort_data = []

for i in range(3):
  parts = file.readline().split(' ')
  N_data.append(parts[0])
  create_data.append(parts[1])
  if parts[2][-1] == '\n':
    parts[2] = parts[2][:-1] # Trim newline if present
  sort_data.append(parts[2])

print(f"N: {N_data}, create: {create_data}, sort: {sort_data}")

ax.set_xlabel('N')
ax.set_ylabel('Time (s)')

# Draw lines
ax.plot(N_data, create_data, 'b')
ax.plot(N_data, sort_data, 'r')

# Draw points
for i in range(len(N_data)):
  ax.scatter(N_data[i], create_data[i], color='b')
for i in range(len(N_data)):
  ax.scatter(N_data[i], sort_data[i], color='r')

plt.legend(['Create', 'Sort'])

plt.show()
