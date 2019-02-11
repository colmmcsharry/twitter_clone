from flask import Flask, render_template, request, redirect
# from sentiment_analyzer.sentiment_analyzer import TweetAnalyzer
import json
import requests
import sqlite3
from datetime import date

app = Flask(__name__)

conn = sqlite3.connect('twitter.db') 
c = conn.cursor()


# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tweets
             (id INTEGER PRIMARY KEY AUTOINCREMENT, date text, tweet text)''')


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

@app.route('/', methods=['GET', 'POST'])
def Twitclone():
	conn = sqlite3.connect('twitter.db') 
	c = conn.cursor()
	if request.method == 'POST':
		text = request.form['text2']
		todaysdate = date.today()
		c.execute("INSERT INTO tweets(date,tweet) VALUES (?,?)", (todaysdate, text))
		conn.commit()
	show = c.execute ("SELECT * from tweets").fetchall()
	return render_template('index.html', tweets=show)




if __name__ == '__main__':
    app.run()