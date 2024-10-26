import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Document': ['Vision 2030', 'Vision 2030', 'Vision 2030', 'Vision 2030', 'Vision 2030', 'Vision 2030',
                 'National Innovation Plan', 'National Innovation Plan', 'National Innovation Plan', 'National Innovation Plan', 'National Innovation Plan', 'National Innovation Plan',
                 'National Water Strategy 2030', 'National Water Strategy 2030', 'National Water Strategy 2030', 'National Water Strategy 2030', 'National Water Strategy 2030', 'National Water Strategy 2030',
                 'Saudi Arabia\'s Drought Management Strategy', 'Saudi Arabia\'s Drought Management Strategy', 'Saudi Arabia\'s Drought Management Strategy', 'Saudi Arabia\'s Drought Management Strategy', 'Saudi Arabia\'s Drought Management Strategy', 'Saudi Arabia\'s Drought Management Strategy'],
    'International Agreement/SDG': ['Paris Agreement', 'UN Convention', 'GPAI', 'SDG 6', 'SDG 9', 'SDG 13',
                                     'Paris Agreement', 'UN Convention', 'GPAI', 'SDG 6', 'SDG 9', 'SDG 13',
                                     'Paris Agreement', 'UN Convention', 'GPAI', 'SDG 6', 'SDG 9', 'SDG 13',
                                     'Paris Agreement', 'UN Convention', 'GPAI', 'SDG 6', 'SDG 9', 'SDG 13'],
    'Themes Match': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes',  # Vision 2030
                     'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes',  # National Innovation Plan
                     'No', 'Yes', 'No', 'Yes', 'No', 'No',  # National Water Strategy 2030
                     'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']  # Saudi Arabia's Drought Management Strategy
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Pivot the data to have "Document" as the index, and the international agreements/SDGs as columns
pivot_df = df.pivot(index='Document', columns='International Agreement/SDG', values='Themes Match')

# Replace 'Yes' and 'No' with 1 and 0 for plotting
pivot_df = pivot_df.replace({'Yes': 1, 'No': 0})

# Plot the stacked bar chart
pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightgreen', 'lightblue', 'coral', 'lightpink', 'lightyellow', 'orange'])

# Add titles and labels
plt.title('KSA Policies Linked with International Agreements/SDGs')
plt.xlabel('KSA Strategy')
plt.ylabel('Count of Matches (Yes/No)')
plt.xticks(rotation=45)
plt.legend(title='International Agreement/SDG', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
