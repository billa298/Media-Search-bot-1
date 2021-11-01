from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

import os
import threading
os.system("pip3 install -r requirements.txt")
def run():
	os.system("python3 bot.py")


threading.Thread(target=run).start()



app.run(host='0.0.0.0', port=8080)