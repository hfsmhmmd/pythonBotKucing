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

def identify_ringworm(user_message):
    ringworm_keywords = ["bulu", "rontok", "kulit", "berwarna", "merah", "luka"]
    return any(keyword in user_message for keyword in ringworm_keywords)

def identify_scabies(user_message):
    scabies_keywords = ["membengkak", "muka", "kelopak mata", "menggesek", "kulit", "gelisah", "luka", "garuk", "keras"]
    return any(keyword in user_message for keyword in scabies_keywords)

def identify_skin_allergies(user_message):
    allergies_keywords = ["muka", "mata", "bengkak", "berair", "telinga", "membengkak", "cairan kuning"]
    return any(keyword in user_message for keyword in allergies_keywords)


# Function to handle user messages
def handle_message(update, context):
    user_message = update.message.text.lower()
    conversational_state = context.user_data.get('conversational_state')

    # # if conversational_state == WAITING_FOR_START:
    # if identify_ringworm(user_message):
    #     context.user_data['conversational_state'] = 'WAITING_FOR_GEJALA_TAMBAHAN_RW'
    #     update.message.reply_text("...")
    # elif identify_scabies(user_message):
    #     context.user_data['conversational_state'] = 'SB_POSITIVE_2'
    #     update.message.reply_text("...")
    # elif identify_skin_allergies(user_message):
    #     context.user_data['conversational_state'] = 'SA_POSITIVE_1'
    #     update.message.reply_text("...")

    rabies_keywords = ["hewan", "pelihara", "tiba-tiba", "perilaku", "aneh", "tidak", "mau", "dekat", "kalau", "cahaya", "suara", "ketakutan", "dengar"]

    # Define different combinations of keywords that might indicate rabies-related meanings
    rabies_similar_combinations = [
        ["hewan", "pelihara", "tiba-tiba", "perilaku", "aneh"],
        ["tidak", "mau", "dekat", "kalau", "cahaya"],
        ["takut", "dengar", "suara"]
    ]

    leptospirosis_keywords = ["kulit", "mata", "gusi", "hewan", "pelihara", "warna", "sangat", "pucat", "air", "seni", "coklat"]
    leptospirosis_similar_combinations = [
    ["kulit", "mata", "gusi", "hewan", "pelihara"],
    ["air", "seni", "coklat"]]
    
    heartworm_keywords = ["anjing", "batuk", "terus", "tidak", "mau", "olahraga", "jalan", "pagi", "hewan", "pelihara", "sangat", "cepat", "lelah", "terus-terusan"]

    # Define different combinations of keywords that might indicate HEARTWORM-related meanings
    heartworm_similar_combinations = [
        ["batuk", "terus", "terus"],
        ["tidak", "mau", "olahraga", "jalan", "pagi"],
        ["sangat", "cepat", "lelah", "olahraga", "terus-terusan", "batuk"]
    ]

    flutd_keywords = ["hewan", "pelihara", "sering", "sekali", "pipis", "keluar", "sedikitsedikit", "terkadang", "warna", "merah", "lihat", "sakit", "kucing", "buang", "air", "kecil", "jumlah", "sedikit"]

    # Define different combinations of keywords that might indicate FLUTD-related meanings
    flutd_similar_combinations = [
        ["pipis", "keluar", "sedikitsedikit", "terkadang", "warna", "merah", "lihat", "sakit"],
        ["kucing", "sering", "sekali", "buang", "air", "kecil", "jumlah", "sedikit", "warna", "merah"]
    ]

    distemper_keywords = ["anjing", "demam", "lama", "hari", "sudah", "3", "serta", "turun", "nafsu", "makan", "berat", "badan", "suhu", "naik", "berapa", "tidak", "turun"]

    # Define different combinations of keywords that might indicate DISTEMPER-related meanings
    distemper_similar_combinations = [
        ["demam", "lama", "3", "hari", "lama", "serta", "turun", "nafsu", "makan", "berat", "badan"],
        ["suhu", "naik", "lama", "berapa", "hari", "lalu", "tidak", "nafsu", "makan", "berat", "badan", "turun"]
    ]

    # Define DIABETES-related keywords
    diabetes_keywords = ["nafsu", "makan", "hewan", "pelihara", "baik", "berat", "badan", "malah", "turun", "kucing", "tingkat", "alami"]

    # Define different combinations of keywords that might indicate DIABETES-related meanings
    diabetes_similar_combinations = [
        ["nafsu", "makan", "hewan", "pelihara", "baik", "berat", "badan", "malah", "turun"],
        ["kucing", "nafsu", "makan", "tingkat", "berat", "badan", "alami", "turun"],
        ["anjing", "berat", "badan", "turun", "nafsu", "makan", "tingkat"]
    ]

    # Define CATFLU-related keywords
    catflu_keywords = ["kucing", "bersin", "terus", "hidung", "ingus", "mata", "belek", "hewan", "pelihara", "sering", "sekali", "banyak"]

    # Define different combinations of keywords that might indicate CATFLU-related meanings
    catflu_similar_combinations = [
        ["kucing", "bersin", "terus", "hidung", "ingus", "mata", "belek"],
        ["hewan", "pelihara", "hidung", "ingus", "sering", "sekali", "bersin", "mata", "banyak", "belek"]
    ]

    # Define CANINE_PARVOVIRUS-related keywords
    parvovirus_keywords = ["anjing", "jadi", "lesu", "hilang", "selera", "makan", "perut", "lihat", "kembung", "tidak", "mau", "besar", "gitu"]

    # Define different combinations of keywords that might indicate CANINE_PARVOVIRUS-related meanings
    parvovirus_similar_combinations = [
        ["anjing", "jadi", "lesu", "hilang", "selera", "makan", "perut", "lihat", "kembung"],
        ["anjing", "tidak", "mau", "makan", "perut", "lihat", "besar", "kembung", "gitu"]
    ]





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
            context.user_data['conversational_state'] = 'RW_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm. Conversational State: {}".format( context.user_data))
         
        else : 
            del context.user_data['conversational_state']
              
            context.user_data['conversational_state'] = 'RW_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm.Conversational State: {}".format( context.user_data))
        

    elif conversational_state == 'RW_NEGATIVE_4':
        if 'luka' or 'luka bundar' or 'luka berbentuk bundar' in user_message:
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")   
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_NEGATIVE_5'
    
    elif conversational_state == 'RW_NEGATIVE_5':
        if "tidak" in user_message:
            if "itu saja" in user_message or "tidak ada" in user_message:
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'RW_NEGATIVE_6'
                update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Ringworm.")

    
    elif conversational_state == 'RW_NEGATIVE_6' or conversational_state=='RW_POSITIVE_3':
        if "apa yang dimaksud dengan penyakit ringworm?" in user_message \
        or ("maksud" in user_message and ("penyakit" in user_message or ("penyakit" in user_message and "ringworm" in user_message))) \
        or ('maksud' in user_message and "apa" in user_message) \
        or "apa penyakit ringworm sering terjadi pada kucing atau anjing?" in user_message \
        or ("kucing" in user_message or "anjing" in user_message) and ("sakit" in user_message and "ringworm" in user_message and "sering" in user_message) \
        or "bagaimana penyakit ringworm dapat terjadi?" in user_message \
        or ("bagaimana" in user_message and "sakit" in user_message and "ringworm" in user_message and "jadi" in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_QNA_7'
            update.message.reply_text("Ringworm adalah penyakit yang sering dialami oleh kucing maupun anjing yang diakibatkan oleh jamur (Microsporum canis) yang hidup di kulit dan bulu.")

    elif conversational_state == "RW_QNA7":
        if ("bagaimana gejala" in user_message or "apa saja ciri" in user_message) \
        and ("gejala" in user_message or "ciri" in user_message) \
        and ("lain" in user_message or "lainnya" in user_message) \
        and ("kucing" in user_message or "anjing" in user_message) \
        and ("terkena" in user_message or "mengalami" in user_message) \
        and ("penyakit ringworm" in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_QNA_8'
            update.message.reply_text("""Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit ringworm:
                            1.	Bulu rontok dan rusak di daerah wajah dan telinga.
                            2.	Terdapat sisa kulit kering yang menyerupai kotembe atau sisik.
                            3.	Daerah bulu yang terdapat ringworm biasanya berbentuk lingkaran (circular).
         
                                      
                                                                 """)
            
    # Handle the user's inquiry about additional symptoms or characteristics of ringworm
    elif conversational_state == "RW_QNA_8":
        if ("bagaimana cara pengobatan" in user_message or "bagaimana cara penanganan" in user_message) \
                and ("ringworm" in user_message or "penyakit ringworm" in user_message):
            # Provide information about the treatment or management of ringworm
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_QNA_9'
            update.message.reply_text("""Anda bisa memandikan kucing atau anjing yang terkena ringworm setiap 2 hari sekali dan mengoleskan krim anti jamur setiap 1 atau 2 kali sehari di bagian yang terkena ringworm menggunakan sarung tangan karet.

                    !! Catatan Penting !!
                    Layanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Sehingga hanya dokter hewan yang dapat memberikan diagnosis serta cara penanganan atau pengobatan yang lebih akurat setelah pemeriksaan lebih lanjut. Kami sarankan untuk segera membuat janji temu dengan dokter hewan atau pergi ke klinik hewan terdekat dari rumah anda untuk memastikannya kembali.
                    """)

    elif conversational_state == "RW_QNA9_":     
        if "terima kasih" in user_message \
        or "membawanya ke klinik" in user_message \
        or "membuat janji dengan dokter hewan" in user_message \
        or "hal seperti ini sangat membantu saya" in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_END'
            update.message.reply_text(""" Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu anda! Semoga kucing atau anjing anda bisa cepat sehat dan ceria kembali!❤️🐱""")
                 
    # Respond with acknowledgment or additional guidance if needed




 #SB
    elif conversational_state == 'SB_POSITIVE_2':
        if ('ya' in user_message and ('bulu rontok' in user_message or 'bulunya rontok' in user_message)) \
            or ('bulunya rontok' in user_message and 'penebalan kulit' not in user_message) \
            or ('tidak ada' in user_message and 'penebalan kulit' not in user_message and 'bulu' in user_message and 'rontok' in user_message):
                    del context.user_data['conversational_state']
                    context.user_data['conversational_state'] = 'SB_POSITIVE_3'
                    update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data))
        
        elif 'tidak' in user_message or 'tidak tahu'  in user_message or 'tidak rontok'  in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_NEGATIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya pengeriputan pada kulit atau air seni yang dikeluarkan berwarna coklat?: {}".format( context.user_data))


    elif conversational_state == 'SB_POSITIVE_3':
            if 'pipis' in user_message and 'berwarna coklat' in user_message\
                or 'tidak' in user_message or 'itu saja' in user_message:
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_NEGATIVE_4'
                update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Scabies. Conversational State: {}".format( context.user_data))
    

    elif conversational_state == 'SB_NEGATIVE_5':
        if (('warna air seni' in user_message or 'warna pipis' in user_message) and 'berwarna coklat' in user_message) \
        or ('kulit' in user_message and 'keriput' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_NEGATIVE_6'
            update.message.reply_text("  Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data))
    
    elif conversational_state == 'SB_NEGATIVE_6': 
           if 'iya' or 'ya' in user_message or 'tidak' in user_message or 'itu saja' in user_message:
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_NEGATIVE_7'
                update.message.reply_text("  Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data))
    


    #mulai AI
    #SA
    elif conversational_state == 'SA_POSITIVE_1':
         if 'iya' in user_message and ('kulit' in user_message and 'merah' in user_message) and ('garuk' in user_message or 'digaruk' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_2'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format( context.user_data)) 

    elif conversational_state == 'SA_POSITIVE_2':
        if 'terkadang' in user_message and ('muntah' in user_message or 'bersin' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = "SA_POSITIVE_3" 
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format(context.user_data))
   
    elif conversational_state == 'SA_POSITIVE_3':
        if 'terkadang' in user_message and ('muntah' in user_message or 'bersin' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_4'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format(context.user_data))

    elif conversational_state == 'SA_POSITIVE_4':
        if 'sepertinya' in user_message and 'mengalami diare' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Conversational State: {}".format(context.user_data))


    elif conversational_state == 'SA_POSITIVE_4':
        if 'tidak' in user_message or 'tidak ada' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Skin Allergies. Conversational State: {}".format(context.user_data))




    elif conversational_state == 'RA_POSITIVE_1':
        if 'ya' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA_POSITIVE_2'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")
            
    elif conversational_state == 'RA_POSITIVE_2':
        if 'air liur' in user_message and 'banyak' in user_message \
                or 'marah' in user_message and ('tiba-tiba' in user_message or 'tanpa sebab' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")
            
    elif conversational_state == 'RA_POSITIVE_3':
        if 'tidak' in user_message or 'tidak ada' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA_POSITIVE_4'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi virus yang dikenal sebagai penyakit Rabies.")

         
    

   #penentu alur flow penyakit
    
    # ringworm    
    elif conversational_state is None:
                    
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
        
        #skin alergies
        elif(('muka' in user_message or 'mata' in user_message) and 'bengkak' in user_message and 'berair' in user_message) \
        or ('telinga' in user_message and 'membengkak' in user_message and 'cairan kuning' in user_message):
            context.user_data['conversational_state'] = 'SA_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, kulit yang memerah meradang karena suka di garuk (gatal)? \n Conversational State: {}".format( context.user_data))
        


        elif any(word in user_message for word in rabies_keywords) \
            or any(all(word in user_message for word in combination) for combination in rabies_similar_combinations):
            context.user_data['conversational_state'] = 'RA_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, takut dengan air dan nafsu makannya menurun? \n Conversational State: {}".format( context.user_data))


        elif any(word in user_message for word in leptospirosis_keywords) \
            or any(all(word in user_message for word in combination) for combination in leptospirosis_similar_combinations):
                context.user_data['conversational_state'] = 'LS_POSITVE_1'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda. Saya menduga ada kemungkinan LEPTOSPIROSIS. Apakah ada gejala tambahan yang dapat anda sampaikan? \n Conversational State: {}".format(context.user_data))

        elif any(word in user_message for word in heartworm_keywords) \
            or any(all(word in user_message for word in combination) for combination in heartworm_similar_combinations):
                context.user_data['conversational_state'] = 'HW_POSITIVE_1'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penurunan nafsu makan dan berat badan? \n Conversational State: {}".format(context.user_data))

        #FLUTD

        elif any(word in user_message for word in flutd_keywords) \
        or any(all(word in user_message for word in combination) for combination in flutd_similar_combinations):
            context.user_data['conversational_state'] = 'FD_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penurunan nafsu makan dan berat badan? \n Conversational State: {}".format(context.user_data))
        
        # Distemper
        
        elif any(word in user_message for word in distemper_keywords) \
        or any(all(word in user_message for word in combination) for combination in distemper_similar_combinations):
            context.user_data['conversational_state'] = 'DT_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, mengalami muntah disertai diare? \n Conversational State: {}".format(context.user_data))

        #diabetes
        elif any(word in user_message for word in diabetes_keywords) \
        or any(all(word in user_message for word in combination) for combination in diabetes_similar_combinations):
            context.user_data['conversational_state'] = 'DIABETES_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, kualitas bulu menjadi buruk atau mengalami keriput pada kulitnya? \n Conversational State: {}".format(context.user_data))


        #catflu
        
        elif any(word in user_message for word in catflu_keywords) \
        or any(all(word in user_message for word in combination) for combination in catflu_similar_combinations):
            context.user_data['conversational_state'] = 'CATFLU_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, terdapat sariawan di bagian lidah/gusi sehingga tidak mau makan? \n Conversational State: {}".format(context.user_data))


        # canine parvovirus
        # Check if any CANINE_PARVOVIRUS-related keywords or similar combinations are present in the user message
        elif any(word in user_message for word in parvovirus_keywords) \
        or any(all(word in user_message for word in combination) for combination in parvovirus_similar_combinations):
            context.user_data['conversational_state'] = 'CANINE_PARVOVIRUS_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, mengalami muntah disertai diare? \n Conversational State: {}".format(context.user_data))


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
