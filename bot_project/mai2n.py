import telegram

api_key = '1425792124:AAHEDYcBQ0h7bVsEY_kB5HoqBAs4_lLBMSc'

bot = telegram.Bot(token=api_key)
updates = bot.getUpdates()

bot_id = 1597201732

#bot.sendMessage(chat_id=bot_id,text="안녕하세요, 로몬입니다.")