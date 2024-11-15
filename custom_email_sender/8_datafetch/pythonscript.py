from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('email_status.db')
cursor = conn.cursor()

# Create a table to store email status
cursor.execute('''
CREATE TABLE IF NOT EXISTS email_status (
    id INTEGER PRIMARY KEY,
    email TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def insert_email_status(email, status):
    cursor.execute('''
    INSERT INTO email_status (email, status)
    VALUES (?, ?)
    ''', (email, status))
    conn.commit()

def visualize_email_status():
    df = fetch_email_status()
    status_counts = df['status'].value_counts()

    plt.figure(figsize=(10, 6))
    status_counts.plot(kind='bar')
    plt.title('Email Status Distribution')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.show()

    

app = Flask(__name__)

@app.route('/')
def dashboard():
    df = pd.read_sql_query('SELECT * FROM email_status', conn)
    status_counts = df['status'].value_counts()
    return render_template('dashboard.html', status_counts=status_counts)

if __name__ == '__main__':
    app.run(debug=True)

