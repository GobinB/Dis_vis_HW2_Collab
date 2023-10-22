#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into Pandas DataFrames
df1 = pd.read_csv('subject_registry.csv')
df2 = pd.read_csv('subject_timezone_log.csv')


# In[14]:




# Data preprocessing
# Filter rows with ISA 'BP03' and state not 'ED' or 'SF'
filtered_df1 = df1[(df1['ISA'] == 'BP03') & (~df1['Actual_Visit'].isin(['ED', 'SF']))]
filtered_df2 = df2[(df2['ISA'] == 'BP03') & (~df2['state'].isin(['ED', 'SF']))]

# Convert timestamp_iso to datetime objects
#filtered_df1['timestamp_iso'] = pd.to_datetime(filtered_df1['timestamp_iso'])
#filtered_df2['timestamp_iso'] = pd.to_datetime(filtered_df2['timestamp_iso'])




# Filter rows with ISA 'BP03' and state not 'ED' or 'SF'
filtered_df1 = df1[(df1['ISA'] == 'BP03') & (~df1['state'].isin(['ED', 'SF']))]
filtered_df2 = df2[(df2['ISA'] == 'BP03') & (~df2['state'].isin(['ED', 'SF']))]

# Convert timestamp_iso to datetime objects
filtered_df1['timestamp_iso'] = pd.to_datetime(filtered_df1['timestamp_iso'])
filtered_df2['timestamp_iso'] = pd.to_datetime(filtered_df2['timestamp_iso'])






# Merge DataFrames on common column (e.g., SubjectID)
merged_df = pd.merge(filtered_df1, filtered_df2, on='SubjectID', suffixes=('_df1', '_df2'))

# Calculate time zone changes (difference in time_offset columns)
merged_df['timezone_change'] = merged_df['time_offset_df2'] - merged_df['time_offset_df1']

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data=merged_df.pivot('SubjectID', 'timestamp_iso_df1', 'timezone_change'), cmap='coolwarm')
plt.title('Time Zone Changes for Eligible Participants (BP03)')
plt.xlabel('Timestamps from Device 1')
plt.ylabel('Participant IDs')
plt.show()


# In[ ]:





# In[ ]:




