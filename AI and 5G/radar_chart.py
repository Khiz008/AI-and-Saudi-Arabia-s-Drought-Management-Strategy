import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the dataset
data = {
    'Vision 2030': [1, 1, 1, 1, 1, 1],  # Yes for all
    'National Innovation Plan': [0, 1, 1, 0, 1, 1],  # Mix of Yes/No
    'National Water Strategy 2030': [0, 1, 0, 1, 0, 0],  # Mix of Yes/No
    'Saudi Arabia\'s Drought Management Strategy': [1, 1, 1, 1, 1, 1]  # Yes for all
}

# International agreements/SDGs as axes
categories = ['Paris Agreement', 'UN Convention', 'GPAI', 'SDG 6', 'SDG 9', 'SDG 13']

# Convert to DataFrame
df = pd.DataFrame(data, index=categories)

# Number of variables we're plotting
num_vars = len(categories)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop by appending the start to the end
angles += angles[:1]

# Radar chart initialization
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw one axis per variable + add labels
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories)

# Plot each KSA strategy
for strategy, values in df.items():
    values = values.tolist()
    values += values[:1]  # Close the loop
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=strategy)
    ax.fill(angles, values, alpha=0.25)  # Fill area for visibility

# Add a title and legend
plt.title('KSA Strategies Alignment with International Agreements/SDGs', size=15, color='darkblue', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the plot
plt.show()
