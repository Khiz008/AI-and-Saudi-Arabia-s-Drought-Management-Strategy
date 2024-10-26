import pandas as pd

# Define the themes for each document, including GPAI framework
themes = {
    'Vision 2030': ['Innovation & Technology', 'Water Management', 'Climate Change & Action', 'Sustainable Development'],
    'National Innovation Plan': ['Innovation & Technology', 'Global Collaboration'],
    'National Water Strategy 2030': ['Water Management'],
    'Saudi Arabia\'s Drought Management Strategy': ['Innovation & Technology', 'Water Management', 'Climate Change & Action', 'Sustainable Development'],
    'GPAI': ['Innovation & Technology', 'Climate Change & Action', 'Sustainable Development', 'Global Collaboration'],  # GPAI added
    'Paris Agreement': ['Climate Change & Action'],
    'UN Convention for Combatting Desertification': ['Innovation & Technology', 'Water Management', 'Climate Change & Action', 'Sustainable Development', 'Global Collaboration'],
    'SDG 13': ['Climate Change & Action', 'Sustainable Development', 'Global Collaboration'],
    'SDG 6': ['Water Management', 'Sustainable Development'],
    'SDG 9': ['Innovation & Technology', 'Climate Change & Action', 'Sustainable Development'],
}

# Define the themes for international agreements and SDGs
international_themes = {
    'Paris Agreement': ['Climate Change & Action'],
    'UN Convention for Combatting Desertification': ['Innovation & Technology', 'Water Management', 'Climate Change & Action', 'Sustainable Development', 'Global Collaboration'],
    'SDG 13': ['Climate Change & Action', 'Sustainable Development', 'Global Collaboration'],
    'SDG 6': ['Water Management', 'Sustainable Development'],
    'SDG 9': ['Innovation & Technology', 'Climate Change & Action', 'Sustainable Development'],
    'GPAI': ['Innovation & Technology', 'Climate Change & Action', 'Sustainable Development', 'Global Collaboration']  # GPAI added
}

# Create a DataFrame to hold the comparison results
comparison_data = []

# Populate the DataFrame with comparison results
for document, doc_themes in themes.items():
    for int_agreement, int_agree_themes in international_themes.items():
        alignment = any(theme in int_agree_themes for theme in doc_themes)
        comparison_data.append({
            'Document': document,
            'International Agreement/SDG': int_agreement,
            'Themes Match': 'Yes' if alignment else 'No'
        })

# Convert the comparison data to a DataFrame
comparison_df = pd.DataFrame(comparison_data)

# Save the DataFrame to an Excel file
comparison_df.to_excel('themes_comparison_with_GPAI.xlsx', index=False)

print("Comparison table with GPAI has been saved to 'themes_comparison_with_GPAI.xlsx'.")
