import matplotlib.pyplot as plt

# Data to plot
labels = 'Python', 'C++', 'JavaScript', 'Java','C#'
sizes = [215, 130, 245, 210, 150]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','grey']


# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=140)

plt.axis('equal')
plt.show()