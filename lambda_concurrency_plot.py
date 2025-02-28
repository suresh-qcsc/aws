import matplotlib.pyplot as plt
import numpy as np

# Burst Data for the graph
time = [0, 30, 90, 90, 150, 150]  #Time intervals in minutes: 0:30, 1:30, 2:30, 3:30, 4:30 etc..
requests = [101, 4000, 4000, 4000, 4000, 4000]
concurrency = [100, 3100, 3100, 3600, 3600, 4000]  #Lambda Concurrency increments

# Lambda concurrency limit line
time_limit = [0, 330]  #Time range for limit line
concurrency_limit = [5000, 5000]  #Fixed concurrency limit value

time_labels = ['0:00', '0:30', '1:30', '2:30', '3:30', '4:30', '5:30']  #Labels in the hh:mm format
ticks = [0, 30, 90, 150, 210, 270, 330]  # Updated X-axis ticks to match all the labels

plt.figure(figsize=(12, 7), facecolor='#1B2B34')
ax = plt.gca()
ax.set_facecolor('#1B2B34')
plt.grid(color='white', linestyle='-', linewidth=1.0, alpha=0.7)
plt.plot(time, requests[:len(time)], marker='o', linestyle='-', color='#7AA116', markersize=8, label='Requests')
plt.plot(time, concurrency[:len(time)], marker='o', linestyle='-', color='#00A4A6', markersize=8, label='Concurrent Executions')
plt.plot(time_limit, concurrency_limit, linestyle='-', color='#00A4A6', linewidth=2, label='Account Concurrency Limit')

# Annotate points
plt.annotate('4000 Requests', xy=(30, 4000), xytext=(-37, 4000), color='#7AA116', fontsize=12, fontweight='bold')
plt.annotate('+3000', xy=(30, 3100), xytext=(40, 2800), color='#00A4A6', fontsize=12, fontweight='bold')
plt.annotate('+500', xy=(90, 3600), xytext=(95, 3300), color='#00A4A6', fontsize=12, fontweight='bold')
plt.annotate('+500', xy=(150, 4100), xytext=(155, 3700), color='#00A4A6', fontsize=12, fontweight='bold')

# Labels and Title
plt.xlabel('Time in minutes', fontsize=14, color='white')
plt.ylabel('Number of Requests and Concurrent Executions', fontsize=14, color='white')
plt.title('Account Concurrency Limit = 5000\nImmediate Concurrency Increase = 3000', fontsize=16, color='white', pad=20)

plt.xticks(ticks, time_labels, fontsize=12, color='white')
plt.yticks([100, 1000, 3000, 5000], fontsize=12, color='white')
plt.legend(fontsize=12, edgecolor='white')

# Display the plot
plt.show()
