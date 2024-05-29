import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pangkatdua(ctx):
    await ctx.send('masukkan angka bebas, nanti aku hitung pangkat 2 nya')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f'pangkat dua dari angka yang kamu kirimkan adalah {(int(message.content)**2)}')
          
@bot.command()
async def meme(ctx):
    import random, os
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)    

def get_duck_image_url():    
    import requests
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url) 

@bot.command()
async def animals(ctx):
    import random, os
    animals_name = random.choice(os.listdir('animals'))
    with open(f'animals/{animals_name}', 'rb') as f:
        animalpic = discord.File(f)
    await ctx.send(file=animalpic)

bot.run("")
