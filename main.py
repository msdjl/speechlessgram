import time
from os import getenv
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv('API_ID'))
api_hash = getenv('API_HASH')
phone = getenv('PHONE')
username = getenv('USERNAME')
messageText = getenv('RESPONSE_MESSAGE')


def main():
    client = TelegramClient(username, api_id, api_hash)
    client.start(lambda: phone)

    @client.on(events.NewMessage())
    async def handler(event):
        if not event.out and event.is_private and event.message.voice:
            sender = await event.get_sender()
            print(time.asctime(), 'A voice message from:', sender.first_name, sender.last_name, '(', sender.username, ')')
            await event.delete()
            await client.send_message(sender, messageText, silent=True)
            time.sleep(1)

    print(time.asctime(), '-', 'Auto-replying...')
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
