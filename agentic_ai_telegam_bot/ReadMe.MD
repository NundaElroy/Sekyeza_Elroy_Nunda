

---

# Simple Telegram Bot

Sends daily motivational quotes via a Telegram bot.

---

## Features

- Sends one quote daily at a scheduled time (default: 9:00 AM).
- Reads quotes from a list and tracks progress using `quote_state.json`.
- Loops back to the first quote after all quotes are sent.
- Utilizes Python's `schedule` library for timing.
- Allows editing the scheduled time in the `quote_state.json` file using a specific format (e.g., `09:00` for single-digit hours).

---

## Setup

Follow these steps to set up the bot:

### 1. Create the Bot
- Open Telegram and message **@BotFather**.
- Type `/newbot` and follow the instructions to create your bot.
- Copy the bot token provided after setup.

### 2. Install Dependencies
Run the following command to install required Python libraries:

```bash
pip install requests schedule python-dotenv
```

### 3. Create a `.env` File
Create a `.env` file in the project directory and add the following variables:

```env
BOT_TOKEN=your_token_here
CHAT_ID=your_chat_id_here
```

Replace `your_token_here` with the token you received from **@BotFather** and `your_chat_id_here` with your (you can follow on how to get it below)chat ID.

### 4. Get Your Chat ID
NOTE FIRST SEND SOME MESSAGE TO YOUR BOT example hello this will help us to get the chat id 
There are two methods to obtain your chat ID:

1. **Via Telegram API:**  
   - Send a message to your bot.
   - Replace `YOUR_TOKEN` with your bot's token and visit:  
     `https://api.telegram.org/botYOUR_TOKEN/getUpdates`.
   - Look for `'id': 5327830334` in the response (example).
   
2. **Using the Test Script:**  
   - Run `test.py` in your project directory.
   - Check the response for the chat ID.

💡 **Note:** The Telegram API may take some time to update. Be patient if the chat ID doesn't appear immediately.

---

## Run the Bot

To start the bot, execute:

```bash
python bot.py
```

The bot will send one quote daily at 9:00 AM by default. You can modify the scheduled time in the `quote_state.json` file by editing the `"time"` field using the 24-hour format `HH:MM`. Ensure that single-digit hours are prefixed with a zero (e.g., `09:00`).

---

## How It Works

- Reads quotes from a predefined list.
- Tracks the next quote to send and scheduled timing in `state.json`.
- Sends quotes sequentially, looping back to the first quote when all are sent.
- Uses Python's `schedule` library for timing.

---

Let me know if you'd like me to commit this update to your repository!