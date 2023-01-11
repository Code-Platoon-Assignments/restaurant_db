import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ.get('SLACK_TOKEN'))
BOT_ID = client.api_call("auth.test")['user_id']
client.chat_postMessage(channel='#Pairs', text='sup')

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    print(payload)
    print(event)
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    
    if BOT_ID != user_id :
        client.chat_postMessage(channel='#Pairs', text='yo')

def reaction_added(event_data):
  emoji = event_data["event"]["reaction"]
  print(emoji)

@slack_event_adapter.on("reaction_added")
@app.route("/")
def hello(event_data):
  return "Hello there!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)