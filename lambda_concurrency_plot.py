import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches

# Data for the graph
time = [0, 15, 30, 90, 90, 150, 150]  
requests = [135, 135, 4000, 4000, 4000, 4000, 4000]  
concurrency = [100, 100, 3100, 3100, 3600, 3600, 4100]  
# Concurrency limit line
time_limit = [0, 330]  
concurrency_limit = [5000, 5000]  

time_labels = ['', '0:30', '1:30', '2:30', '3:30', '4:30', '5:30']  
ticks = [0, 30, 90, 150, 210, 270, 330]  

fig, ax = plt.subplots(figsize=(14, 7), facecolor='#000000')
ax.set_facecolor('#000000')
ax.grid(color='white', linestyle='-', linewidth=1.2, alpha=0.8)

# Enable ticks on x-axis and y-axis
ax.tick_params(axis='x', direction='inout', length=6, color='white', width=1.2) # X-axis ticks
ax.tick_params(axis='y', direction='inout', length=6, color='white', width=1.2) # Y-axis ticks
ax.set_ylim(-200, 5500)
ax.spines['top'].set_visible(False)  # Hide top border
ax.spines['right'].set_visible(False)  # Hide right border
ax.spines['left'].set_color('white')  # Keep y-axis visible
ax.spines['bottom'].set_color('white')  # Keep x-axis visible
  
line_requests, = ax.plot([], [], marker='o', linestyle='-', markerfacecolor='#7AA116', markeredgecolor='#7AA116', markeredgewidth=3, color='#7AA116', markersize=10, linewidth=2, label='Requests')
line_concurrency, = ax.plot([], [], marker='o', linestyle='-', markerfacecolor='#00A4A6', markeredgecolor='#00A4A6', markeredgewidth=3, color='#00A4A6',markersize=10, linewidth=2, label='Concurrent Executions')
line_concurrency_limit, = ax.plot(time_limit, concurrency_limit, linestyle='-', color='#00A4A6', linewidth=2, label='Account Concurrency Limit (5000)')

# Labels and Title
ax.set_xlabel('Time (minutes)', fontsize=14, color='white')
ax.set_ylabel('') # Keep y-label empty

# Add colored labels for y-axis separately
ax.text(-0.06, 0.2, "Number of Requests", fontsize=14, color="#7AA116", ha="center", va="center", rotation=90, transform=ax.transAxes)
ax.text(-0.06, 0.44, "and", fontsize=14, color="white", ha="center", va="center", rotation=90, transform=ax.transAxes)
ax.text(-0.06, 0.70, "Concurrent Executions", fontsize=14, color="#00A4A6", ha="center", va="center", rotation=90, transform=ax.transAxes)
#ax.text(0, 6000, 'An Illustration of AWS Lambda\'s Effectiveness in Managing Traffic Bursts', fontsize=15, color='#C925D1')
ax.set_xticks(ticks)
ax.set_xticklabels(time_labels, fontsize=12, color='white')
ax.set_yticks([100, 500, 1000, 2000, 3000, 4000, 5000])
ax.set_yticklabels([100, '', 1000, '', 3000, '', 5000], fontsize=12, color='white')
ax.legend(fontsize=12, edgecolor='white', loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=3)

# **  Clocks Setup  **
clock_positions = [(0.23, 0.69), (0.36, 0.69)]  
clocks = []
for pos in clock_positions:
    clock_ax = fig.add_axes([pos[0],pos[1],0.12,0.12])
    clock_ax.set_xlim(-1.5,1.5)
    clock_ax.set_ylim(-1.5,1.5)
    clock_ax.set_xticks([])
    clock_ax.set_yticks([])
    clock_ax.set_frame_on(False)
    # Initialize clock hands
    hour_hand,   = clock_ax.plot([], [], color='white', linewidth=4, alpha=0) #initially set invisible
    minute_hand, = clock_ax.plot([], [], color='#00A4A6', linewidth=2, alpha=0) #initially set invisible
    second_hand, = clock_ax.plot([], [], color='red', linewidth=1.5, alpha=0) #initially set invisible
    clocks.append((clock_ax, hour_hand, minute_hand, second_hand))
# Annotations
annotations = [
    ('4000 ⚡ Burst of Requests', -15, 4100, -33, 4100, '#ED7100'),
    ('+3000 (Increase concurrency by 3,000 immediately)', 30, 3100, 35, 2800, '#00A4A6'),
    ('+500  (Lambda adds 500 invocations per minute)', 90, 3600, 95, 3300, '#00A4A6'),
    ('+500  (Lambda auto-scales further)', 150, 4100, 155, 3750, '#00A4A6')
]

annotation_texts = []
for text, x, y, xt, yt, color in annotations:
    annotation_texts.append(ax.annotate(text,xy=(x, y), xytext=(xt, yt), color=color,fontsize=12, fontweight='bold', alpha=0))  # Initially hidden
    
def update(frame):
    """ Update function for the graph, clocks, and annotations """
    max_frames = 60  
    progress = frame/max_frames
    # Convert animation frame to seconds (86400sec = 24 hrs)
    time_in_seconds = min(progress * 60, 60)
    # Find the current index for plotting based on the progress
    index = min(int(progress*len(time)),len(time)-1)
    line_requests.set_data(time[:index+1],requests[:index+1])
    line_concurrency.set_data(time[:index+1],concurrency[:index+1])
    # Handle annotation appearance at specific frames
    annotation_appear_frames = [15, 30, 45, 55]  # Frames when annotations must appear
    for i, annotation in enumerate(annotation_texts):
        if frame >= annotation_appear_frames[i]:
            annotation.set_alpha(1) # Display annotation
    # Clocks should appear after specific annotations
    if frame >= annotation_appear_frames[1]:  # 2nd annotation triggers first clock
        clock1_active = True
    else:
        clock1_active = False
    if frame >= annotation_appear_frames[2]:  # 3rd annotation triggers second clock
        clock2_active = True
    else:
        clock2_active = False
    # Animate Clocks
    for i, (clock_ax, hour_hand, minute_hand, second_hand) in enumerate(clocks):
        if (i == 0 and clock1_active) or (i == 1 and clock2_active):
            # Calculate angles based on real clock movement
            second_angle = np.deg2rad(time_in_seconds*6)       #6° per second
            minute_angle = np.deg2rad((time_in_seconds/60)*6)  #6° per minute
            hour_angle = np.deg2rad((time_in_seconds/3600)*30) #30° per hour
            hour_hand.set_data([0, 0.5 * np.cos(hour_angle - np.pi/2)],[0, 0.5 * np.sin(hour_angle - np.pi/2)])
            minute_hand.set_data([0, 0.8 * np.cos(minute_angle - np.pi/2)],[0, 0.8 * np.sin(minute_angle - np.pi/2)])
            second_hand.set_data([0, 0.9 * np.cos(second_angle - np.pi/2)],[0, 0.9 * np.sin(second_angle - np.pi/2)])
            # Draw clock face only once when it appears
            if frame == annotation_appear_frames[i+1]:  
                clock_face = patches.Circle((0, 0), 1, fill=False, edgecolor='white', linewidth=1)
                clock_ax.add_patch(clock_face)
            # Make the clock hands visible
            hour_hand.set_alpha(1)
            minute_hand.set_alpha(1)
            second_hand.set_alpha(1)
    return line_requests, line_concurrency, *sum([[h, m, s] for _, h, m, s in clocks], []), *annotation_texts
# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=1000, blit=False) #60 seconds total
# Save animation as GIF file
ani.save("Lambda_concurrency_graph_v1.gif", writer='pillow', fps=10)
plt.show()
