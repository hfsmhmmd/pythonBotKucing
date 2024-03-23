from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Function to handle the "/start" command
def start(update, context):
    update.message.reply_text("Hi! What would you like to do?")

# Function to handle user messages
def handle_message(update, context):
    user_message = update.message.text.lower()

    # Check if user's message contains keywords related to fur shedding
    if 'bulu' in user_message and 'kucing' in user_message and 'rontok' in user_message:
        # Reply and ask if the user's cat is hot
        update.message.reply_text("Apakah kucing Anda panas? (Ya/Tidak)")

        # Set a flag to indicate that we're waiting for user's response
        context.user_data['waiting_for_temperature_response'] = True

    # Check if the bot is waiting for the temperature response
    elif 'waiting_for_temperature_response' in context.user_data:
        # Check the user's response
        if 'ya' in user_message:
            update.message.reply_text("Baik, sepertinya kucing Anda sakit diare.")
        elif 'tidak' in user_message:
            update.message.reply_text("Terima kasih atas informasinya.")
        else:
            update.message.reply_text("Saya tidak mengerti. Tolong jawab dengan 'Ya' atau 'Tidak'.")

        # Clear the flag since we've received the response
        del context.user_data['waiting_for_temperature_response']

    # If none of the above conditions are met
    else:
        update.message.reply_text("I'm sorry, I didn't understand. What would you like to do?")

def main():
    # Create the Updater and Dispatcher
    updater = Updater("7009078826:AAFksyBum-0HASxTb4kQgs9NhyyH3IAYauM", use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
