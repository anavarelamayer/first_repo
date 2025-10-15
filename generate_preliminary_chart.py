import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "Mantamonis_bacterial_contamination_analysis (1).xlsx"
df = pd.read_excel(file_path)

# Count the values in the 'Preliminary Verdict' column
verdict_counts = df['Preliminary Verdict:'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
verdict_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Counts of Preliminary Verdicts:')
plt.xlabel('Preliminary Verdict:')
plt.ylabel('Count')
plt.tight_layout()

# Save the chart
plt.savefig('preliminary_classification.png', dpi=300)
plt.show()




