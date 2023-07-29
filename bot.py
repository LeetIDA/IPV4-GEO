import discord
import requests
import re

client = discord.Client(intents=discord.Intents.all())
CHANNEL_ID = 

def get_geo_info(ip):
    response = requests.get(f"https://ipapi.co/{ip}/json/")
    data = response.json()
    return data
@client.event
async def on_ready():
    print('=> Logged in as {0.user}'.format(client))
    # Set the bot status
    activity = discord.Game(name="Made With 🤍 By IDA")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        match = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", message.content)
        if match:
            ip = match.group()
            geo_info = get_geo_info(ip)
            embed = discord.Embed(title="Geo Info", color=0x00ff00)
            embed.add_field(name="IP Address", value=ip)
            embed.add_field(name="Country", value=geo_info["country_name"])
            embed.add_field(name="Region", value=geo_info["region"])
            embed.add_field(name="City", value=geo_info["city"])
            embed.add_field(name="Latitude", value=geo_info["latitude"])
            embed.add_field(name="Longitude", value=geo_info["longitude"])
            embed.add_field(name="Org", value=geo_info["org"])
            embed.add_field(name="Requested By", value=f"{message.author.name}#{message.author.discriminator}")
            await message.channel.send(embed=embed)
            await message.delete()

client.run("")
