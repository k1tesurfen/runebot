# Requirements 
## Install virtual environment with required packages
```python -m venv name_of_your_environment```

### On Windows:
1. In cmd run: `.\name_of_your_environment\Scripts\activate`
2. Run: `pip install -r requirements.txt` 

## Install ffmpeg
In order for the bot to play music in a voice channel follow this:
1. Download ffmpeg.exe from [github.com/BtbN/FFmpeg-Builds/](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Copy the .exe file to ./cogs/

# Run Bot 
Add config.py with credentials

config.py 
---
```
api_key = "your_bots_token"
guild_key = "your_guild_key"
```

guild_key is the Server ID for your discord server. Enable developer mode in discord and right click your server &rarr; Copy Server ID

## Example use of runebot:
Discord has to run on machine this code is executed. 
```
import runebot

runebot.run_discord_bot()
```
