
import requests
import schedule
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Simple quotes list
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It is during our darkest moments that we must focus to see the light.",
    "Believe you can and you're halfway there.",
    "The only impossible journey is the one you never begin.",
    "In the middle of difficulty lies opportunity.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "The way to get started is to quit talking and begin doing.",
    "Don't be afraid to give up the good to go for the great.",
    "Innovation distinguishes between a leader and a follower.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, "state.json")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def get_next_quote():
    # Read current state
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
        index = data.get("index", 0)
    else:
        index = 0
    
    # Get quote and update index
    quote = quotes[index]
    next_index = (index + 1) % len(quotes)  # Loop back to 0 after last quote
    
    # Save new state (preserve time if it exists)
    state_data = {"index": next_index}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            existing_data = json.load(f)
        if "time" in existing_data:
            state_data["time"] = existing_data["time"]
    else:
        state_data["time"] = "09:00"  # Default time
    
    with open(STATE_FILE, "w") as f:
        json.dump(state_data, f)
    
    return quote

def get_schedule_time():
    """Get the schedule time from the state.json file"""
    if not os.path.exists(STATE_FILE):
        return "09:00"  # Default time
    
    with open(STATE_FILE, "r") as f:
        data = json.load(f)
    return data.get("time", "09:00")

def send_daily_quote():
    quote = get_next_quote()
    send_message(quote)
    print(f"Sent: {quote}")

# Get schedule time from JSON file
schedule_time = get_schedule_time()

# Schedule daily message at configurable time
schedule.every().day.at(schedule_time).do(send_daily_quote)

print(f"Bot started. Will send daily quotes at {schedule_time}")

while True:
    schedule.run_pending()
    time.sleep(60)