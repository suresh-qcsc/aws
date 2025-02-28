import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Data for the graph
time = [-10, 0, 15, 30, 90, 90, 150, 150]  # Time intervals in minutes: 0:30,1:30,2:30, etc.
requests = [135, 135, 135, 4000, 4000, 4000, 4000, 4000]
concurrency = [100, 100, 100, 3100, 3100, 3600, 3600, 4100]  #Corrected concurrency increments

# Concurrency limit line
time_limit = [-10, 330]  # Time range for limit line
concurrency_limit = [5000, 5000]  # Fixed concurrency limit value

time_labels = ['', '0:30', '1:30', '2:30', '3:30', '4:30', '5:30']  # Labels in hh:mm format
ticks = [0, 30, 90, 150, 210, 270, 330]  # Updated X-axis ticks to match all labels

fig, ax = plt.subplots(figsize=(14, 7), facecolor='#000000')
ax.set_facecolor('#000000')
ax.grid(color='white', linestyle='-', linewidth=1.2, alpha=0.8)
ax.set_ylim(-200, 5500)  # Adjusted y-axis limits for better visibility

line_requests, = ax.plot([], [], marker='o', linestyle='-', markerfacecolor='#7AA116', markeredgecolor='#7AA116', markeredgewidth=3, color='#7AA116', markersize=10, linewidth=2, label='Requests')
line_concurrency, = ax.plot([], [], marker='o', linestyle='-', markerfacecolor='#00A4A6', markeredgecolor='#00A4A6', markeredgewidth=3, color='#00A4A6', markersize=10, linewidth=2, label='Concurrent Executions')
line_concurrency_limit, = ax.plot(time_limit, concurrency_limit, linestyle='-', color='#00A4A6', linewidth=3, label='Account Concurrency Limit (5000)')

# Labels and Title
ax.set_xlabel('Time (minutes)', fontsize=14, color='white')
ax.set_ylabel('')  # Keep y-label empty

# Add colored labels for y-axis separately
ax.text(-0.06, 0.2, "Number of Requests", fontsize=14, color="#7AA116", ha="center", va="center", rotation=90, transform=ax.transAxes)
ax.text(-0.06, 0.44, "and", fontsize=14, color="white", ha="center", va="center", rotation=90, transform=ax.transAxes)
ax.text(-0.06, 0.70, "Concurrent Executions", fontsize=14, color="#00A4A6", ha="center", va="center", rotation=90, transform=ax.transAxes)
ax.text(0, 6000, 'An Illustration of AWS Lambda\'s Effectiveness in Managing Traffic Bursts', fontsize=16, color='#C925D1')
ax.set_xticks(ticks)
ax.set_xticklabels(time_labels, fontsize=12, color='white')
ax.set_yticks([100, 500, 1000, 2000, 3000, 4000, 5000])
ax.set_yticklabels([100,'500',1000,'2000', 3000,'4000', 5000], fontsize=12, color='white')
ax.legend(fontsize=12, edgecolor='white', loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=3)

# annotations

annotations = [
    ('', -10, 400,0 , 400, '#7AA116'),
    ('', 30, 4150, -37, 4150, '#7AA116'),
    ('', 30, 4150, -37, 4150, '#7AA116'),
    ('4000⚡Burst of Requests', -5, 4100, -25, 4100, '#ED7100'),
    ('+3000 (Increase concurrency by 3,000 immediately)', 30, 3100, 35, 2800, '#00A4A6'),
    ('', 30, 4150, -37, 4150, '#ED7100'),
    ('+500  (Lambda adds 500 invocations per minute)', 90, 3600, 95, 3300, '#00A4A6'),
    ('+500  (Lambda auto-scales further)', 150, 4100, 155, 3750, '#00A4A6')
]

annotation_texts = []

def update(frame):
    line_concurrency_limit.set_data(time_limit[:frame-1], concurrency_limit[:frame-1])
    line_requests.set_data(time[:frame], requests[:frame])
    line_concurrency.set_data(time[:frame], concurrency[:frame])
    
    for i, (text, x, y, xt, yt, color) in enumerate(annotations):
        if frame > i:
            annotation_texts.append(ax.annotate(text, xy=(x, y), xytext=(xt, yt), color=color, fontsize=12, fontweight='bold'))
    return line_requests, line_concurrency, *annotation_texts

ani = animation.FuncAnimation(fig, update, frames=len(time)+1, interval=25, blit=True) #len(time) + 1

# Save animation as GIF
ani.save("Lambda_concurrency_graph.gif", writer='pillow', fps=1)

# Display the plot
plt.show()
