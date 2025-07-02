
# Simple Telegram Bot

Sends daily motivational quotes via Telegram bot.

## Setup

1. **Create bot**: Head to your telegram Message @BotFather, type `/newbot`
 
2. **Install**: `pip install requests schedule python-dotenv` 
3. **Create .env file**:
   and type this 
   ```
   BOT_TOKEN=your_token_here
   CHAT_ID=your_chat_id_here
   ```
4**Get chat ID**:
          **you may have to be patient and try gain API may take some time to update**
   - Send message to your bot, then visit:
   `https://api.telegram.org/botYOUR_TOKEN/getUpdates`
   OR
   RUN test.py and look at the response for the chat id  eg 'id':  5327830334

       

## Run

```bash
python bot.py
```

Bot sends one quote daily at 9:00 AM. Change time in code if needed.

## How it works

- Reads quotes from a list
- Tracks which quote to send next in `state.json` and the time set in the state json file
- Loops back to first quote after sending all
- Uses Python `schedule` library for timing