from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


WAITING_FOR_START = 0

# def resetState():
    

# Function to handle the "/start" command
def start(update, context):
    update.message.reply_text("""🐾AAASelamat datang di PetHealthBot!

Terima kasih sudah memilih kami untuk konsultasi kesehatan hewan peliharaan kucing dan anjing anda. Kami hadir untuk memberikan informasi mengenai diagnosa penyakit berdasarkan gejala-gejala yang dialami kucing atau anjing anda.

Untuk memulai konsultasi, silahkan beritahukan gejala kesehatan kucing atau anjing anda. Kami akan dengan senang hati memberikan bantuan sebaik mungkin.

!! Catatan Penting !!
Layanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Jika hewan peliharaan anda mengalami kondisi medis yang serius, kami sarankan anda segera berkonsultasi dengan dokter hewan terdekat.

🌟Kami berharap anda dan hewan peliharaan anda tetap sehat dan bahagia!
""")




# Function to handle user messages
def handle_message(update, context):
    user_message = update.message.text.lower()
    conversational_state = context.user_data.get('conversational_state')

    # if conversational_state == WAITING_FOR_START:

    
    if conversational_state == 'WAITING_FOR_GEJALA_TAMBAHAN_RW':
       
        if 'tidak' in user_message:
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya luka berbentuk seperti lingkaran?")
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_NEGATIVE_4'
            

        elif "bulu" in user_message\
            or 'ya' in user_message  or 'iya' in user_message \
            or ('ketombe' in user_message and 'bulu rontok' in user_message) \
            or ('bulunya rontok' in user_message) \
            or ('ketombe'in user_message and 'bulu' in user_message and 'rontok'  in user_message )   :

            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data))
            del context.user_data['conversational_state']
         
            context.user_data['conversational_state'] = 'WAITING_FOR_GEJALA_TAMBAHAN_LAIN_RW'
      

    elif conversational_state == 'WAITING_FOR_GEJALA_TAMBAHAN_LAIN_RW':
        if 'luka' or 'luka bundar' or 'luka berbentuk bundar' in user_message:
            del context.user_data['conversational_state']
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm.")
         
        else : 
            del context.user_data['conversational_state']
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm.")
    
    elif conversational_state == 'RW_NEGATIVE_4':
        if 'luka' or 'luka bundar' or 'luka berbentuk bundar' in user_message:
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")   
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'WAITING_FOR_GEJALA_TAMBAHAN_LAIN_RW'

    elif conversational_state == 'SB_POSITIVE_2':
        if 'ya' in user_message or 'bulu rontok' in user_message \
            or 'bulunya rontok' in user_message \
            or ('tidak ada' in user_message and 'penebalan kulit' not in user_message and 'bulu' in user_message and 'rontok' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data))

    elif conversational_state == 'SB_POSITIVE_3':
            if 'pipis' in user_message and 'berwarna coklat' in user_message\
                or 'tidak' or 'itu saja':
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_POSITIVE_4'
                update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Scabies. Conversational State: {}".format( context.user_data))
    
    # elif conversational_state == 'SB_POSITIVE_4':

         
   #penentu alur flow penyakit
        #ringworm       
    if "bulu" in user_message and "rontok" in user_message \
            or "bulunya" in user_message or "rontok" in user_message \
            or ("tidak" in user_message and "nafsu" in user_message and "makan" in user_message) \
            or ("tidak" in user_message and "makan" in user_message) \
            or ("kulit" in user_message and "berwarna" in user_message and "merah" in user_message) \
            or ("kulit" in user_message and "luka" in user_message and "warna" in user_message and "merah" in user_message):
                context.user_data['conversational_state'] = 'WAITING_FOR_GEJALA_TAMBAHAN_RW'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya sisa kulit kering seperti ketombe? Conversational State: {}".format( context.user_data))
            #scabies
    elif 'membengkak' in user_message and ('muka' in user_message or 'kelopak mata' in user_message)\
            or 'menggesek' in user_message and ('kulit' in user_message or 'gelisah' in user_message)\
            or 'luka' in user_message and ('garuk' in user_message or 'keras' in user_message):
            context.user_data['conversational_state'] = 'SB_POSITIVE_2'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penebalan pada kulit yang mengakibatkan kerontokan bulu? Conversational State: {}".format( context.user_data))


    elif 'resett' in user_message:
         context.user_data['conversational_state'] = ' '
         update.message.reply_text("Reset! Conversational State: {}".format( context.user_data))

    else :
        update.message.reply_text("I'm sorry, I didn't understand. What would you like to do?    \n {} ".format( context.user_data)) 





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
