git init
git add .
git commit -m from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# معرف القناة المرسِل منها (source)
SOURCE_CHANNEL = "@testcodep2"

# معرف القناة الهدف (target)
TARGET_CHANNEL = "@testfromp1"

# وظيفة إعادة التوجيه
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التأكد من أن الرسالة قادمة من القناة المصدر
    if update.channel_post and update.channel_post.chat.username == SOURCE_CHANNEL.strip("@"):
        # إعادة توجيه الرسالة إلى القناة الهدف
        await context.bot.forward_message(chat_id=TARGET_CHANNEL, from_chat_id=SOURCE_CHANNEL, message_id=update.channel_post.message_id)



def main():

    BOT_TOKEN = "7934426352:AAGOlePvcqJAF8ZzUIGnQHSJlsBmAssq-0I"

    # إنشاء التطبيق
    application = Application.builder().token(BOT_TOKEN).build()

    # استخدام فلتر التحقق من رسائل القنوات
    application.add_handler(MessageHandler(filters.ALL, forward_message))

    # تشغيل البوت
    application.run_polling()

if __name__ == "__main__":
    main()

git remote add origin https://github.com/ebaaghanem/tele.git
git push -u origin main

