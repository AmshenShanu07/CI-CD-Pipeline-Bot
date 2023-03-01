from cicd import app
from pyrogram import Client, filters
from pyrogram.types import Message
from subprocess import call, check_output
import os

@app.on_message(filters.command('start'))
async def start_handler(bot:Client,event:Message):
    username = f'{event.from_user.first_name} {event.from_user.last_name}'
    message = f'''**Hello {username}**'''

    await event.reply_text(text=message)


@app.on_message(filters.command("deploy"))
async def credits_handler(bot:Client,event:Message):
    await event.reply_text(text="Deploying Started")
    log = check_output(['bash','./deploy.sh'])
    file = open('log.txt','w+')
    file.write(log.decode('utf-8'))
    file.close()
    await event.reply_document(document='./log.txt')
    os.remove('./log.txt')
    print(log.decode('utf-8'))
    await event.reply_text(text="Deploying Completed")

@app.on_message(filters.command("run"))
async def credits_handler(bot:Client,event:Message):
    cmd = event.text
    cmd = cmd.replace('/run ','').split(' ')
    print(cmd)
    log = check_output(cmd)
    file = open('log.txt','w+')
    file.write(log.decode('utf-8'))
    file.close()
    await event.reply_document(document='./log.txt')
    os.remove('./log.txt')

app.run()