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
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
from typing import Union, Optional
from petpetgif import petpet as petpetgif

load_dotenv()
token = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def pet(ctx, image: Optional[Union[discord.PartialEmoji, discord.member.Member]]):
    if type(image) == discord.PartialEmoji:
        image = await image.url_as(format='png').read() # retrieve the image bytes
    elif type(image) == discord.member.Member:
        image = await image.avatar_url_as(format='png').read() # retrieve the image bytes
    else:
        await ctx.reply('Please use a custom emoji or tag a member to petpet their avatar.')
        return

    source = BytesIO(image) # file-like container to hold the emoji in memory
    dest = BytesIO() # container to store the petpet gif in memory
    petpetgif.make(source, dest)
    dest.seek(0) # set the file pointer back to the beginning so it doesn't upload a blank file.
    await ctx.send(file=discord.File(dest, filename=f"{image[0]}-petpet.gif"))


client.run(token)
```