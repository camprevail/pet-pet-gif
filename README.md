# pet-pet-gif
Python adaptation of https://github.com/aDu/pet-pet-gif  

![](https://raw.githubusercontent.com/camprevail/pet-pet-gif/main/example/froge-petpet.gif)
![](https://raw.githubusercontent.com/camprevail/pet-pet-gif/main/example/oshaberi-petpet.gif)
![](https://raw.githubusercontent.com/camprevail/pet-pet-gif/main/example/sadcat-petpet.gif)


### Usage:
```py
from petpetgif import petpet  
petpet.make(source, dest)
```
- source:  A filename (string), pathlib.Path object or a file object. (This parameter corresponds
           and is passed to the PIL.Image.open() method.)
   

- dest: A filename (string), pathlib.Path object or a file object. (This parameter corresponds
           and is passed to the PIL.Image.save() method.)
  
Basic example:
```py
from petpetgif import petpet
petpet.make('test.png', 'out.gif')
```

Discord.py example:
```py
import os, re, requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
from petpetgif import petpet as petpetgif

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def petpet(ctx, emoji):
    emoji = list(filter(bool, re.split("[:<>]", emoji)))
    try:
        if emoji[0] == 'a':
            await ctx.reply("Sorry, you can't use animated emojis.")
            return
        elif emoji[1].isdigit():
            emoji_id = emoji[1]
    except:
        await ctx.reply("Sorry, you can't use regular emojis.")


    img = requests.get(f"https://cdn.discordapp.com/emojis/{emoji_id}.png")
    source = BytesIO(img.content) # file-like container to hold the emoji in memory
    source.seek(0)
    dest = BytesIO() # container to store the petpet gif in memory
    petpetgif.make(source, dest)
    dest.seek(0)
    await ctx.send(file=discord.File(dest, filename=f"{emoji[0]}-petpet.gif"))


client.run(token)
```