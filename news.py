from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

# Учетные данные для подключения к Telegram
api_id = 'Ваш_api_id'
api_hash = 'Ваш_api_hash'
phone_number = 'Ваш_номер_телефона'

# Идентификатор канала
channel_id = -1001394050290

# Ключевые слова для поиска
keywords = ["путина", "трамп"]

# Создание клиента
client = TelegramClient('session', api_id, api_hash)

async def main():
    await client.start()
    
    if not await client.is_user_authorized():
        await client.sign_in(phone_number)
        # Если требуется код подтверждения, введите его
        # await client.sign_in(code=input('Enter the code: '))
    
    try:
        # Получение сообщений из канала
        messages = await client.get_messages(channel_id, limit=100)
        news_text = ""
        
        for message in messages:
            if message.text and any(keyword in message.text.lower() for keyword in keywords):
                news_text += f"{message.text}\n\n"
        
        if news_text:
            print(news_text)
        else:
            print("Нет новостей за последние сообщения.")
    except PeerIdInvalidError as e:
        print(f"Ошибка чтения канала: {e}")

    await client.disconnect()

import asyncio
asyncio.run(main())
