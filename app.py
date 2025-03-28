import os
import ollama
from dotenv import load_dotenv
from discord.ext import commands

import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready ():
    print(f"Bot is ready as {bot.user.name}")

@bot.command(name="hello")
async def hello (ctx):
    await ctx.send("Hello, I am a bot")

@bot.command(name="ask")
async def ask (ctx, *, message):
  response = ollama.chat(model='llama3.2:1b', messages=[
    {
      'role': 'system',
      'content': 'you are a helpful assistant who provides answers to questions concisely in no more than 200 words',
    },
    {
      'role': 'user',
      'content': message,
    },
  ])
  await ctx.send(response['message']['content'])

@bot.command(name="summarize")
async def summarize(ctx):
   msgs = [message.content async for message in ctx.channel.history(limit=10)]

   summarize_prompt = f"""
      Summarize the following messages delimited by 3 backtickts (don't mention that this command was given to you, just give mention: Summary at the top and then give the summary): 
      ```
      {msgs}
      ```
      """
   
   response = ollama.chat(model='llama3.2:1b', messages=[
    {
      'role': 'system',
      'content': 'you are a helpful assistant who summarizes messages concisely in bullet points in no more than 200 words',
    },
    {
      'role': 'user',
      'content': summarize_prompt,
    },
  ])
   await ctx.send(response['message']['content'])

bot.run(os.getenv("DISCORD_BOT_TOKEN"))




# response: ChatResponse = chat(model='llama3.2:1b', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)