# Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the Data
subject_registry_df = pd.read_csv("subject_registry.csv")
subject_timezone_log_df = pd.read_csv("subject_timezone_log.csv")

# Step 2: Filter the Data
filtered_subjects = subject_registry_df[(subject_registry_df['ISA'] == 'BP03') & 
                                        (~subject_registry_df['Actual_Visit'].isin(['ED', 'SF']))]
eligible_participants = filtered_subjects['SubjectID'].tolist()
filtered_timezone_data = subject_timezone_log_df[subject_timezone_log_df['subject'].isin(eligible_participants)]

# Step 3: Process Timezone Data
filtered_timezone_data['date'] = pd.to_datetime(filtered_timezone_data['timestamp_iso']).dt.date
timezone_matrix = filtered_timezone_data.pivot_table(index='subject', columns='date', values='timezone_location', aggfunc='first')

# Step 4: Visualize with a Heatmap
plt.figure(figsize=(20, 10))
sns.heatmap(timezone_matrix.notnull(), cmap="YlGnBu", cbar=False, yticklabels=True)
plt.title("Timezone Changes Over the Trial")
plt.xlabel("Date")
plt.ylabel("Subject ID")
plt.show()
