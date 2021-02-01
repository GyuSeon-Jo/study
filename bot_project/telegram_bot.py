 # import modules
from telegram.ext import Updater, MessageHandler, Filters
import random

my_token = '1425792124:AAHEDYcBQ0h7bVsEY_kB5HoqBAs4_lLBMSc'

print('start telegram chat bot...')

send_who = ['누구', '자기소개', '이름', '정체']
repl_who = ['저는 로몬이에요!', '로몬이라고 해요', '제 이름은 로몬이에요 성은 솔 씨입니다']

send_hello = ['안녕', '반가', '반갑']
repl_hello = ['안녕하세요!', '반가워요!', '반갑습니다!']

send_need = ['싶']
repl_need = ['왜 그것이 필요한가요?', '어째서요?', '저도 그래요']

send_time = ['언제', '몇 시', '몇시']
repl_time = ['곧일지도 몰라요', '얼마 안남았어요!', '조금만 참으세요']

send_thanks = ['고마', '고맙', '감사']
repl_thanks = ['천만에요!', ' 당신을 위해서인걸요', '별일 아니에요']

send_why = ['때문에', '싶어서', '니까']
repl_why = ['그렇군요', '잘 알겠어요', '그 마음 이해해요']

repl_no = ['무슨 말인지 잘 모르겠네요', '네? 다시 말해보시겠어요?', '왜 그런 말을 하세요?']

# message reply function
def get_message(update, context):
    text = update.message.text
    chat_id = update.message.chat_id

    ans = True

    for i in range(len(send_who)):
        if send_who[i] in text:
            update.message.reply_text(random.choice(repl_who))
            ans = False

    for i in range(len(send_hello)):
        if send_hello[i] in text:
            update.message.reply_text(random.choice(repl_hello))
            ans = False


    for i in range(len(send_need)):
        if send_need[i] in text:
            update.message.reply_text(random.choice(repl_need))
            ans = False

    for i in range(len(send_time)):
        if send_time[i] in text:
            update.message.reply_text(random.choice(repl_time))
            ans = False

    for i in range(len(send_thanks)):
        if send_thanks[i] in text:
            update.message.reply_text(random.choice(repl_thanks))
            ans = False

    for i in range(len(send_why)):
        if send_why[i] in text:
            update.message.reply_text(random.choice(repl_why))
            ans = False

    if ans:
        update.message.reply_text(random.choice(repl_no))

updater = Updater(my_token, use_context=True)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()