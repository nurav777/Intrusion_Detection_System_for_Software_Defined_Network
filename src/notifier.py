import time
import asyncio
import nest_asyncio
nest_asyncio.apply()
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR-BOT-TOKEN"
CHAT_ID = "YOUR-CHAT-ID"
log_file = "traffic_log.txt"


# This function monitors traffic_log.txt for BLOCKED and UNBLOCK events
async def monitor_log(application: Application):
    print(" Notifier started. Watching traffic_log.txt...")
    await asyncio.sleep(1)  # Let the bot settle
    with open(log_file, "r") as f:
        f.seek(0, 2)  # Go to end

        while True:
            line = f.readline()
            if not line:
                await asyncio.sleep(1)
                continue

            if "[BLOCKED]" in line:
                print(" Harmful IP blocked")
                await application.bot.send_message(chat_id=CHAT_ID, text=f" ALERT:\n{line.strip()}")

            elif "[CMD] UNBLOCK_ALL" in line:
                print(" Unblock command detected")
                await application.bot.send_message(chat_id=CHAT_ID, text=" INFO: Unblock command received. All IPs will be unblocked.")


# Function to perform the actual unblocking (without iptables changes)
def log_unblock_event():
    # Log unblock request (without iptables flush)
    print(" Unblock event logged.")
    timestamp = time.strftime('%H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] [CMD] UNBLOCK_ALL\n")


# When /unblock command is sent by user
async def unblock_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(" /unblock command received from user")
    log_unblock_event()  # Log the unblock event
    await update.message.reply_text(" Unblock request has been logged and will be processed shortly.")


# Initialize bot and background log watcher
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("unblock", unblock_command))

    # Start monitor_log after bot starts
    async def post_init(app: Application):
        asyncio.create_task(monitor_log(app))

    app.post_init = post_init

    # Start the bot (no need to manually manage event loop)
    await app.run_polling()


if __name__ == "__main__":
    try:
        # Just await the main function directly
        asyncio.run(main())  # This should work without event loop conflict
    except KeyboardInterrupt:
        print(" Program interrupted by user")

