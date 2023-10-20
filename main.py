import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the data
timezone_df = pd.read_csv('subject_timezone_log.csv')
registry_df = pd.read_csv('subject_registry.csv')

print("Columns in timezone_df:", timezone_df.columns)
print("Columns in registry_df:", registry_df.columns)

# Rename 'subjectID' to 'subject' for consistency
registry_df.rename(columns={'SubjectID': 'subject'}, inplace=True)
print("\nAfter renaming columns in registry_df:", registry_df.columns)

# Filter the subjects based on the given conditions
eligible_subjects = registry_df[
    (registry_df['ISA'] == 'BP03') & 
    (~registry_df['Actual_Visit'].isin(['ED', 'SF']))
]
print("\nNumber of eligible subjects:", len(eligible_subjects))

# Step 2: Merge the two dataframes
merged_df = pd.merge(eligible_subjects, timezone_df, on=['Site', 'subject'])
print("\nNumber of rows in merged_df:", len(merged_df))

# Step 3: Processing the Data
# Count the distinct timezones for each subject
timezone_changes = merged_df.groupby('subject')['timezone_location'].nunique()
print("\nNumber of distinct timezones by subject:", len(timezone_changes))

# Step 4: Visualization
# For the sake of simplicity, let's represent each subject on the y-axis and their number of timezone changes on the x-axis in a heatmap.
heatmap_data = timezone_changes.values.reshape(-1, 1)

# Plotting
plt.figure(figsize=(5, len(timezone_changes)))
sns.heatmap(heatmap_data, cmap='YlGnBu', yticklabels=timezone_changes.index)
plt.title("Timezone Changes by Subject")
plt.xlabel("Number of Timezone Changes")
plt.ylabel("Subjects")
plt.show()
