from slack_sdk import WebClient

import os
import pathlib as Path
from dotenv import load_dotenv


load_dotenv()
client = WebClient(token=os.environ['slack-token'])

def send_message(channel, message, blocks=None):
    if blocks:
        client.chat_postMessage(channel=channel, text=message, blocks=blocks)
    else: 
        client.chat_postMessage(channel=channel, text=message)

