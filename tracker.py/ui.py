import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd

def show_report():
    conn = sqlite3.connect('time_tracker.db')
    df = pd.read_sql_query("SELECT * FROM usage", conn)
    
    def categorize_application(application):
        if not application:
            return "Unknown"
        if "chrome" in application.lower():
            return "Web Browsing"
        elif "word" in application.lower():
            return "Work"
        return "Other"

    df['category'] = df['application'].apply(categorize_application)
    category_summary = df.groupby('category')['duration'].sum().reset_index()

    report = "\n".join([f"{row['category']}: {row['duration']} seconds" for index, row in category_summary.iterrows()])
    messagebox.showinfo("Report", report)

root = tk.Tk()
root.title("Time Tracker")

report_button = tk.Button(root, text="Show Report", command=show_report)
report_button.pack()

root.mainloop()
