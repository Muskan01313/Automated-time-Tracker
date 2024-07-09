import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('time_tracker.db')

df = pd.read_sql_query("SELECT * FROM usage", conn)

# Add categorization
def categorize_application(application):
    if not application:
        return "Unknown"
    if "chrome" in application.lower():
        return "Web Browsing"
    elif "word" in application.lower():
        return "Work"
    return "Other"

df['category'] = df['application'].apply(categorize_application)

# Group by category and sum durations
category_summary = df.groupby('category')['duration'].sum().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(category_summary['category'], category_summary['duration'])
plt.xlabel('Category')
plt.ylabel('Time Spent (seconds)')
plt.title('Time Spent on Different Categories')
plt.show()
