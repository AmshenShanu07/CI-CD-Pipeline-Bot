from cicd import app
from pyrogram import Client, filters
from pyrogram.types import Message
from subprocess import call


@app.on_message(filters.command('start'))
async def start_handler(bot:Client,event:Message):
    username = f'{event.from_user.first_name} {event.from_user.last_name}'
    message = f'''**Hello {username}**'''

    await event.reply_text(text=message)


@app.on_message(filters.command("deploy"))
async def credits_handler(bot:Client,event:Message):
    await event.reply_text(text="Deploying Started")
    call('./deploy.sh',shell=True)
    await event.reply_text(text="Deploying Completed")

app.run()