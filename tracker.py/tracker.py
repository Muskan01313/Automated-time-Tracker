import time
import pygetwindow as gw
import sqlite3

# Initialize SQLite
conn = sqlite3.connect('time_tracker.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usage
             (timestamp DATETIME, application TEXT, duration INTEGER)''')

def log_usage(timestamp, application, duration):
    c.execute("INSERT INTO usage VALUES (?, ?, ?)", (timestamp, application, duration))
    conn.commit()

def get_active_window():
    active_window = gw.getActiveWindow()
    if active_window:
        return active_window.title
    return None

# Tracking loop
while True:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    active_window = get_active_window()
    print(f"{timestamp}: Active Window: {active_window}")
    log_usage(timestamp, active_window, 5)  # Assuming 5 seconds interval
    time.sleep(5)
