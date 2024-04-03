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

    

    rabies_keywords = ["hewan", "pelihara", "tiba-tiba", "perilaku", "aneh", "tidak", "mau", "dekat", "kalau", "cahaya", "suara", "ketakutan", "dengar"]

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



  
    if 'resett' in user_message:
        del context.user_data['conversational_state']
        update.message.reply_text("Reset! \n \n conversational State: {}".format( context.user_data))

    elif 'setStatus' in user_message:
        # del context.user_data['conversational_state']
        update.message.reply_text("Set State! \n \n ")
    
    elif 'state' in user_message:
        wanted_state = update.message.text
        parts = wanted_state.split()

# Get the second part (index 1) of the split string
        code = parts[1]
        # update.message.reply_text("Reset! \n \n conversational State: {}".format( context.user_data))
        context.user_data['conversational_state'] = code
        update.message.reply_text("Set State!: {}".format(code))
            
    elif 'check' in user_message:
        update.message.reply_text("Check:  \n  conversational State: {}".format( context.user_data))
        # update.message.reply_text("Set State!: {}".format(update.message))

    elif conversational_state == 'RW_POSITIVE_1':
       
        if 'tidak' in user_message:
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya luka berbentuk seperti lingkaran?")
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_NEGATIVE_4'
            

        elif "bulu" in user_message\
            or 'ya' in user_message  or 'iya' in user_message \
            or ('ketombe' in user_message and 'bulu rontok' in user_message) \
            or ('bulunya rontok' in user_message) \
            or ('ketombe'in user_message and 'bulu' in user_message and 'rontok'  in user_message )   :

            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_POSITIVE_2'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n conversational State: {}".format( context.user_data))
      

    elif conversational_state == 'RW_POSITIVE_2':
        if 'luka' or 'luka bundar' or 'luka berbentuk bundar' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm. \n \n conversational State: {}".format( context.user_data))
         
        else : 
            del context.user_data['conversational_state']
              
            context.user_data['conversational_state'] = 'RW_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena infeksi jamur yang dikenal sebagai penyakit Ringworm.\n \n conversational State: {}".format( context.user_data))
        

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

    elif conversational_state == "RW_QNA_7":
        # Define RW7 keywords
        rw7_keywords = ["apa", "maksud", "sakit", "ringworm", "sering", "kucing", "anjing", "bagaimana", "jadi"]

        # Define RW7 similar combinations
        rw7_combinations = [
            ["apa", "maksud", "sakit", "ringworm"],
            ["apa", "sakit", "ringworm", "sering", "kucing", "anjing"],
            ["bagaimana", "sakit", "ringworm", "jadi"]
        ]

        # Check if any RW7-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in rw7_keywords) \
        or any(all(word in user_message for word in combination) for combination in rw7_combinations):
            # Delete any existing conversational state
          
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_QNA_8'
            update.message.reply_text("""Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit ringworm:
                            1.	Bulu rontok dan rusak di daerah wajah dan telinga.
                            2.	Terdapat sisa kulit kering yang menyerupai kotembe atau sisik.
                            3.	Daerah bulu yang terdapat ringworm biasanya berbentuk lingkaran (circular).
                                                                 """)
            
    # Handle the user's inquiry about additional symptoms or characteristics of ringworm
    elif conversational_state == "RW_QNA_8":
        # Define RW8 keywords
        rw8_keywords = ["lalu", "bagaimana", "cara", "pengobatan", "penanganan", "tepat", "sakit", "ringworm"]

        # Define RW8 similar combinations
        rw8_combinations = [
            ["lalu", "bagaimana", "cara", "obat"],
            ["bagaimana", "cara", "penanganan", "obat", "tepat", "sakit", "ringworm"]
        ]

        # Check if any RW8-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in rw8_keywords) \
        or any(all(word in user_message for word in combination) for combination in rw8_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # Set conversational state to RW8
            context.user_data['conversational_state'] = 'RW_QNA_9'
            
            # Reply with the appropriate message
            update.message.reply_text("""Anda bisa memandikan kucing atau anjing yang terkena ringworm setiap 2 hari sekali dan mengoleskan krim anti jamur setiap 1 atau 2 kali sehari di bagian yang terkena ringworm menggunakan sarung tangan karet.

!! Catatan Penting !!
Layanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Sehingga hanya dokter hewan yang dapat memberikan diagnosis serta cara penanganan atau pengobatan yang lebih akurat setelah pemeriksaan lebih lanjut. Kami sarankan untuk segera membuat janji temu dengan dokter hewan atau pergi ke klinik hewan terdekat dari rumah anda untuk memastikannya kembali.
""")


    elif conversational_state == "RW_QNA_9":     
        if "terima kasih" in user_message \
        or "membawanya ke klinik" in user_message \
        or "membuat janji dengan dokter hewan" in user_message \
        or "hal seperti ini sangat membantu saya" in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RW_END'
            update.message.reply_text(""" Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu anda! Semoga kucing atau anjing anda bisa cepat sehat dan ceria kembali!❤️🐱""")
                 
    # Respond with acknowledgment or additional guidance if needed




 #SB scabies
    elif conversational_state == 'SB_POSITIVE_2':
            
            # Define SB_POSITIVE_3 keywords
        sb_positive_3_keywords = ["ya",  "rontok", "tebal", "kulit", "banyak", "memang"]

        # Define SB_POSITIVE_3 combinations
        sb_positive_3_combinations = [
            ["ya",  "rontok" , ],
            ["tidak ada", "tebal", "kulit",  "memang", "rontok"]
        ]

        # Define SB_NEGATIVE_5 keywords
        sb_negative_5_keywords = ["tidak", "terlalu", "hati", "sebut", "rasa", "tidak rontok"]

        # Define SB_NEGATIVE_5 combinations
        sb_negative_5_combinations = [
             ["tidak ", "rontok"],
            ["rasa",  "tidak", "terlalu", "rontok", "tidak rontok"]
        ]

        if any(word in user_message for word in sb_negative_5_keywords) \
                or any(all(word in user_message for word in combination) for combination in sb_negative_5_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_NEGATIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya pengeriputan pada kulit atau air seni yang dikeluarkan berwarna coklat?")
        # Check if any SB_POSITIVE_3-related keywords or similar combinations are present in the user input
        elif any(word in user_message for word in sb_positive_3_keywords) \
                or any(all(word in user_message for word in combination) for combination in sb_positive_3_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_POSITIVE_3'
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")

   
      

    elif conversational_state == 'SB_POSITIVE_3':
            if 'pipis' in user_message and 'berwarna coklat' in user_message\
                or 'tidak' in user_message or 'itu saja' in user_message:
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_POSITIVE_4'
                update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Scabies. \n \n conversational State: {}".format( context.user_data))
    

    elif conversational_state == 'SB_NEGATIVE_5':
        if (('warna air seni' in user_message or 'warna pipis' in user_message) and 'berwarna coklat' in user_message) \
        or ('kulit' in user_message and 'keriput' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SB_NEGATIVE_6'
            update.message.reply_text("  Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n conversational State: {}".format( context.user_data))
    
    elif conversational_state == 'SB_NEGATIVE_6': 
           if 'iya' or 'ya' in user_message or 'tidak' in user_message  or 'tidak ada' in user_message or 'itu saja' in user_message:
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_NEGATIVE_7'
                update.message.reply_text("  Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Scabies. \n \n conversational State: {}".format( context.user_data))
    
    elif conversational_state =='SB_NEGATIVE_7' or conversational_state =="SB_POSITIVE_4":
        if ("apa" in user_message and "maksud" in user_message and "scabies" in user_message) \
            or ("apa" in user_message and "penyebab" in user_message and "scabies" in user_message and ("kucing" in user_message or "anjing" in user_message)) \
            or ("bagaimana" in user_message and "scabies" in user_message and "jadi" in user_message and ("kucing" in user_message or "anjing" in user_message)):
                del context.user_data['conversational_state']
                context.user_data['conversational_state'] = 'SB_QNA_8'
                update.message.reply_text(" Scabies adalah penyakit kulit menular yang disebabkan oleh infestasi tungau Sarcoptes Scabiei dan bersifat zoonosis dengan cara membuat terowongan di bawah lapisan kulit (stratum korneum dan lusidum). \n \n conversational State: {}".format( context.user_data))

    elif conversational_state =="SB_QNA_8":
        # Define SB8-related keywords
        sb8_keywords = ["bagaimana", "gejala", "lain", "alami", "kucing", "anjing", "kena", "sakit", "scabies", "apa", "ciri ciri",  "ciri-ciri", "ciri2","ada", "derita"]

            # Define different combinations of keywords that might indicate SB8-related meanings
        sb8_similar_combinations = [
                ["bagaimana", "gejala", "lain", "alami", "kucing", "anjing", "kena", "sakit", "scabies"],
                ["apa", "ciriciri", "lain", "ada", "kucing", "anjing", "derita", "sakit", "scabies"]
            ]
        # Check if any SB8-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sb8_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sb8_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SB8 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SB_QNA_9'
            update.message.reply_text(""":	Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit Scabies:
                                1.	Air seni yang dikeluarkan berwarna kecoklatan.
                                2.	Hewan penderita tampak gelisah karena rasa gatal, sehingga hewan akan menggaruk atau menggesek tubuhnya sehingga terjadi luka dan pendarahan.
                                3.	Penebalan kulit dan pengeriputan yang mengakibatkan kerontokan bulu pada permukaan tubuh.
                                4.	Tidak nafsu makan, serta ada iritasi dan peradangan pada kulit hewan.
                                \n \n \n \n \n conversational State: {}""".format(context.user_data))


    elif conversational_state =="SB_QNA_9":
         # SB_QNA_9 Keywords
        sb_qna_9_keywords = ["apa", "harus", "laku", "kucing", "anjing", "kena", "sakit", "scabies", "bagaimana", "tangan", "obat", "bisa"]

        # SB_QNA_9 Similar Combinations
        sb_qna_9_similar_combinations = [
            ["apa", "harus", "laku", "kucing", "anjing", "kena", "sakit", "scabies"],
            ["bagaimana", "tangan", "obat", "kucing", "anjing", "kena", "sakit", "scabies"],
            ["obat", "apa", "bisa", "laku", "kucing", "anjing", "kena", "sakit", "scabies"]
        ]
        # Check if any SB_QNA_9-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sb_qna_9_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sb_qna_9_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SB_QNA_9 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SB_QNA_10'
            update.message.reply_text("""Kami bisa memberikan beberapa saran awal yang bisa anda lakukan, yaitu:\n
                                1. Jaga kebersihan kandang dan lingkungan hewan.\n
                                2. Pemberian obat anti parasit dan obat topikal (obat kutu ada yang setiap bulan, 3 bulan, dan 6 bulan (injeksi)).\n !! Catatan Penting !!\n Layanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Sehingga hanya dokter hewan yang dapat memberikan diagnosis serta cara penanganan atau pengobatan yang lebih akurat setelah pemeriksaan lebih lanjut. Kami sarankan untuk segera membuat janji temu dengan dokter hewan atau pergi ke klinik hewan terdekat dari rumah anda untuk memastikannya kembali.""")


    elif conversational_state=="SB_QNA_10":
         # SB_END_11 Keywords
        sb_end_11_keywords = ["terima", "kasih", "akan", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut", "buat", "janji", "dokter", "hewan", "seperti", "sangat", "bantu"]

        # SB_END_11 Similar Combinations (empty since we're not checking combinations)
        sb_end_11_similar_combinations = []

        # Check if any SB_END_11-related keywords are present in the user input
        if any(word in update.message.text for word in sb_end_11_keywords):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SB_END_11 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SB_END_11_ENDED'
            update.message.reply_text("""Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu anda! Semoga kucing atau anjing anda bisa cepat sehat dan ceria kembali!❤️🐱""")

         



    #mulai AI
    #SA
    elif conversational_state == 'SA_POSITIVE_1':
         if 'iya' in user_message and ('kulit' in user_message and 'merah' in user_message) and ('garuk' in user_message or 'digaruk' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_2'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n \n \n conversational State: {}".format( context.user_data)) 

    elif conversational_state == 'SA_POSITIVE_2':
        if 'terkadang' in user_message and ('muntah' in user_message or 'bersin' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = "SA_POSITIVE_3" 
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n \n \n conversational State: {}".format(context.user_data))
   
    elif conversational_state == 'SA_POSITIVE_3':
        if 'terkadang' in user_message and ('muntah' in user_message or 'bersin' in user_message):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_4'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n \n \n conversational State: {}".format(context.user_data))

    elif conversational_state == 'SA_POSITIVE_4':
        if 'sepertinya' in user_message and 'mengalami diare' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? \n \n \n \n conversational State: {}".format(context.user_data))


    elif conversational_state == 'SA_POSITIVE_4':
        if 'tidak' in user_message or 'tidak ada' in user_message:
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'SA_POSITIVE_5'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Skin Allergies. \n \n \n \n conversational State: {}".format(context.user_data))


    #SA NEGATIVE

    elif conversational_state == 'SA_POSITIVE_5':

       # SA_QNA_6 Keywords
        sa_qna_6_keywords = ["suka", "garuk", "seperti", "kulit", "tidak", "terlalu", "merah", "kalau", "lihat", "radang"]

        # SA_QNA_6 Similar Combinations
        sa_qna_6_similar_combinations = [
            ["suka", "garuk"],
            ["seperti", "kulit", "tidak", "terlalu", "merah"],
            ["kalau", "lihat", "kulit", "tidak", "merah", "radang"]
        ]

        # Check if any SA_QNA_6-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa_qna_6_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sa_qna_6_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SA_QNA_6 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SA_NEGATIVE_6'
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda? Misalnya, hewan peliharaan anda mengalami seperti bersin-bersin/muntah/diare?")

    elif conversational_state =="SA_NEGATIVE_6":

        sa_qna_7_keywords = ["iya", "bersinbersin", "muntah", "ya", "akhirakhir", "sering", "muntah", "diare"]

   
        sa_qna_7_similar_combinations = [
            ["bersinbersin", "muntah"],
            ["sering", "muntah", "diare"]
        ]

        # Check if any SA_QNA_7-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa_qna_7_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sa_qna_7_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SA_QNA_7 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SA_NEGATIVE_7'
            update.message.reply_text("Terima kasih atas informasinya. Apakah ada gejala tambahan lainnya yang mungkin dialami oleh hewan peliharaan anda?")

    elif conversational_state =="SA_NEGATIVE_7":
        
        # SA_NEGATIVE_6 Keywords
        sa_negative_6_keywords = ["tidak", "itu", "saja", "ada"]

        # Check if any SA_NEGATIVE_6-related keywords are present in the user input
        if any(word in update.message.text for word in sa_negative_6_keywords):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # SA_NEGATIVE_6 detected, trigger appropriate response
            context.user_data['conversational_state'] = 'SA_NEGATIVE_8'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang anda sampaikan, kemungkinan besar hewan peliharaan anda terkena penyakit kulit yang dikenal sebagai penyakit Skin Allergies.")


        
        # Check if the conversational state is SA8
    elif conversational_state == 'SA_NEGATIVE_8':
        # Define SA9 keywords
        sa9_keywords = ["apa", "maksud", "sakit", "skin", "allergies", "anjing", "sebab", "di", "derita"]

        # Define SA9 similar combinations (empty in this case)
        sa9_similar_combinations = []

        # Check if any SA9-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa9_keywords):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # Set conversational state to SA9
            context.user_data['conversational_state'] = 'SA9'
            
            # Reply message for SA9
            update.message.reply_text("Alergi atau dermatitis alergi adalah jenis reaksi alergi yang paling umum pada anjing dan memiliki 3 penyebab utama, yaitu dermatitis alergi kutu, alergi makanan dan alergi lingkungan.")

    # Check if the conversational state is SA9
    elif conversational_state == 'SA_QNA_9':
        # Define SA10 keywords
        sa10_keywords = ["bagaimana", "ciriciri", "lain", "alami", "anjing", "derita", "sakit", "skin", "allergies", "ada", "kena"]

        # Define SA10 similar combinations (empty in this case)
        sa10_similar_combinations = []

        # Check if any SA10-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa10_keywords):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # Set conversational state to SA10
            context.user_data['conversational_state'] = 'SA_QNA_10'
            
            # Reply message for SA10
            update.message.reply_text("Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit Skin Allergies:\n1. Pembengkakan pada wajah, telinga, bibir, dan kelopak mata.\n2. Kulit merah dan meradang, disertai dengan rasa gatal.\n3. Diare, muntah, dan bersin-bersin.\n4. Infeksi telinga kronis dan mata berair.")
    # Check if any SA11-related keywords or similar combinations are present in the user input
            
    elif conversational_state == 'SA_QNA_10':
        # Define SA11 keywords
        sa_11_keywords = ["pertolongan", "cara", "penanganan", "pengobatan", "anjing", "skin", "allergies"]

        # Define SA11 similar combinations
        sa_11_similar_combinations = [["pertolongan", "cara"], ["penanganan", "pengobatan"]]

        # Check if any SA11-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa_11_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sa_11_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # Set conversational state to SA11
            context.user_data['conversational_state'] = 'SA_QNA_11'
            
            # Reply message for SA11
            update.message.reply_text("Kami bisa memberikan beberapa saran awal yang bisa anda lakukan, yaitu:\n1. Melakukan pembasmian kutu pada anjing dengan cara memandikannya secara rutin.\n2. Mengubah pola makan yang lebih sehat.\n3. Jika alergi yang dialami anjing sangat parah, maka sebaiknya dibawa ke rumah sakit hewan.\n\n!! Catatan Penting !!\nLayanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Sehingga hanya dokter hewan yang dapat memberikan diagnosis serta cara penanganan atau pengobatan yang lebih akurat setelah pemeriksaan lebih lanjut. Kami sarankan untuk segera membuat janji temu dengan dokter hewan atau pergi ke klinik hewan terdekat dari rumah anda untuk memastikannya kembali.")


    # Check if any SA12-related keywords or similar combinations are present in the user input
    elif conversational_state == 'SA_QNA_11':
        # Define SA12 keywords
        sa_12_keywords = ["terima", "kasih", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut", "buat", "janji", "dokter", "hewan", "bantu"]

        # Define SA12 similar combinations
        sa_12_similar_combinations = [["terima", "kasih"], ["terima", "kasih", "segera", "bawa", "klinik"], ["terima", "kasih", "segera", "buat", "janji", "dokter", "hewan"], ["terima", "kasih", "seperti", "sangat", "bantu"]]

        # Check if any SA12-related keywords or similar combinations are present in the user input
        if any(word in update.message.text for word in sa_12_keywords) \
        or any(all(word in update.message.text for word in combination) for combination in sa_12_similar_combinations):
            # Delete any existing conversational state
            del context.user_data['conversational_state']
            
            # Set conversational state to SA12
            context.user_data['conversational_state'] = 'SA_END_12'
            
            # Reply message for SA12
            update.message.reply_text("Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu anda! Semoga kucing atau anjing anda bisa cepat sehat dan ceria kembali!❤️🐱")


    #RABIES  BEIN DI TES SEMUA
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

    elif conversational_state == 'RA_POSITIVE_4':
        # Define RA5 keywords
        ra5_keywords = ["apa", "maksud", "sakit", "rabies"]
        
        # Define RA5 similar combinations
        ra5_combinations = [["apa", "maksud", "sakit", "rabies"]]
        
        # Check if any RA5-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in ra5_keywords) \
                or any(all(word in user_message for word in combination) for combination in ra5_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA_POSITIVE_5'
            update.message.reply_text("Rabies adalah penyakit zoonosis infeksinus lyssavirus pada hewan. Penyakit rabies dapat menular ke manusia melalui air liur atau gigitan hewan yang sudah terinfeksi virus rabies. Karena dapat menyebabkan kematian pada manusia yang tertular penyakit rabies.")

    elif conversational_state == 'RA_POSITIVE_4':
    # Define RA5 keywords and combinations
        ra5_keywords = ["apa", "maksud", "sakit", "rabies"]
        
        # Define RA5 similar combinations
        ra5_combinations = [["apa", "maksud", "sakit", "rabies"]]
        
        # Check if any RA5-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in ra5_keywords) \
                or any(all(word in user_message for word in combination) for combination in ra5_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA5'
            update.message.reply_text("Rabies adalah penyakit zoonosis infeksi virus yang tergolong dalam family rhabdoviridae, genus lyssavirus pada hewan. Penyakit rabies dapat menular ke manusia melalui air liur atau gigitan hewan yang sudah terinfeksi virus rabies.  Karena dapat menyebabkan kematian pada manusia yang tertular penyakit rabies.")
    elif conversational_state == 'RA_POSITIVE_5':
        # Define RA6 keywords and combinations
        ra6_keywords = ["bagaimana", "ciriciri", "lain", "hewan", "pelihara", "kena", "sakit", "rabies"]
        
        # Define RA6 similar combinations
        ra6_combinations = [["bagaimana", "ciriciri", "lain", "hewan", "pelihara", "kena", "sakit", "rabies"]]
        
        # Check if any RA6-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in ra6_keywords) \
                or any(all(word in user_message for word in combination) for combination in ra6_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA6'
            update.message.reply_text("Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit Rabies:\n1. Perubahan perilaku hewan yang secara tiba-tiba, seperti ketakutan, marah, air liur berlebihan, takut air, tidak nafsu makan, takut cahaya dan takut suara.")
    elif conversational_state == 'RA_POSITIVE_6':
        # Define RA7 keywords and combinations
        ra7_keywords = ["bagaimana", "cara", "tangan", "obat", "kucing", "anjing", "kena", "sakit", "rabies",
                        "lalu", "apa", "harus", "laku", "hewan", "pelihara", "kena", "sakit", "rabies"]
        
        # Define RA7 similar combinations
        ra7_combinations = [["bagaimana", "cara", "tangan", "obat", "kucing", "anjing", "kena", "sakit", "rabies"],
                            ["lalu", "apa", "harus", "laku", "hewan", "pelihara", "kena", "sakit", "rabies"]]
        
        # Check if any RA7-related keywords or similar combinations are present in the user input
        if any(word in user_message for word in ra7_keywords) \
                or any(all(word in user_message for word in combination) for combination in ra7_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA7'
            update.message.reply_text("Kami bisa memberikan beberapa saran awal yang bisa Anda lakukan, yaitu:\n1. Segera dibawa ke klinik pemerintah, seperti puskeswan untuk dilakukan karantina selama 14 hari. Jika selama 14 hari hewan masih hidup, kemungkinan hewan tersebut tidak terkena rabies. Namun jika hewan mati sebelum 14 hari, maka nanti akan diambil sampel otaknya dan dilakukan pengecekan lab, benar terkena rabies atau bukan.\n2. Memberikan vaksinasi berkala kepada hewan peliharaan.\n3. Pemberantasan rabies yang dilaksanakan melalui penerapan prinsip-prinsip One Health.\n\n!! Catatan Penting !!\n• Layanan ini tidak dapat menggantikan konsultasi langsung dengan dokter hewan. Sehingga hanya dokter hewan yang dapat memberikan diagnosis serta cara penanganan atau pengobatan yang lebih akurat setelah pemeriksaan lebih lanjut. Kami sarankan untuk segera membuat janji temu dengan dokter hewan atau pergi ke klinik hewan terdekat dari rumah Anda untuk memastikannya kembali.")


    
    elif conversational_state == 'RA_POSITIVE_7':
    # Define RA8 keywords and combinations
        ra8_keywords = ["terima", "kasih", "akan", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut",
                        "buat", "janji", "dokter", "hewan", "seperti", "sangat", "bantu"]
        ra8_combinations = [["terima", "kasih", "akan", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut"],
                            ["terima", "kasih"],
                            ["terima", "kasih", "akan", "segera", "buat", "janji", "dokter", "hewan"],
                            ["terima", "kasih", "seperti", "sangat", "bantu"]]

        # Check if any RA8-related keywords or combinations are present in the user input
        if any(word in user_message for word in ra8_keywords) \
                or any(all(word in user_message for word in combination) for combination in ra8_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'RA_END_8'
            update.message.reply_text("Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu Anda! "
                                    "Semoga kucing atau anjing Anda bisa cepat sehat dan ceria kembali!❤️🐱")

    
    #LS 
    
    #belom di tes
    elif conversational_state == 'LS_POSITIVE_1':
    # Define LS2 keywords and combinations
        ls2_keywords = ["tidak", "ada"]
        ls2_combinations = [["tidak", "ada"]]

        # Check if any LS2-related keywords or combinations are present in the user input
        if any(word in user_message for word in ls2_keywords) \
                or any(all(word in user_message for word in combination) for combination in ls2_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'LS_POSITIVE_2'
            update.message.reply_text("Terima kasih atas informasinya. Berdasarkan gejala yang Anda sampaikan, "
                                    "kemungkinan besar hewan peliharaan Anda terkena infeksi bakteri yang dikenal sebagai penyakit Leptospirosis.")
       
          #belom di tes
        
            
          #belom di tes
    elif conversational_state == 'LS_POSITIVE_2':
    # Define LS3 keywords and combinations
        ls3_keywords = ["apa", "maksud", "sakit", "leptospirosis", "bagaimana", "jadi", "sebab"]
        ls3_combinations = [["apa", "maksud", "sakit", "leptospirosis"],
                            ["bagaimana", "sakit", "leptospirosis", "jadi"],
                            ["apa", "sebab", "sakit", "leptospirosis"]]

        # Check if any LS3-related keywords or combinations are present in the user input
        if any(word in user_message for word in ls3_keywords) \
                or any(all(word in user_message for word in combination) for combination in ls3_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'LS_QNA_3'
            update.message.reply_text("Leptospirosis adalah penyakit yang disebabkan oleh bakteri yang tersebar melalui air seni tikus. Bakteri ini dapat merusak ginjal penderita.")

    elif conversational_state == 'LS_QNA_3':
        # Define LS4 keywords and combinations
        ls4_keywords = ["gejala", "lain", "kucing", "anjing", "leptospirosis", "ciri", "lainnya"]
        ls4_combinations = [["bagaimana", "gejala", "lainnya", "dialami", "kucing", "anjing", "leptospirosis"],
                            ["apa", "saja", "ciri", "lainnya", "kucing", "anjing", "leptospirosis"]]

        # Check if any LS4-related keywords or combinations are present in the user input
        if any(word in user_message for word in ls4_keywords) \
                or any(all(word in user_message for word in combination) for combination in ls4_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'LS_QNA_4'
            update.message.reply_text("Berikut ciri-ciri/gejala/apa yang terjadi ketika kucing atau anjing terkena penyakit Leptospirosis:\n"
                                    "• Air seni yang dikeluarkan berwarna kecoklatan.\n"
             
                                    "• Pada kulit, mata dan gusi berubah warnanya menjadi kekuningan.")
    elif conversational_state == 'LS_QNA_5':
    # Define LS_END_6 keywords and combinations
        ls_end_6_keywords = ["terima", "kasih", "akan", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut",
                            "buat", "janji", "dokter", "hewan", "seperti", "sangat", "bantu"]
        ls_end_6_combinations = [["terima", "kasih", "akan", "segera", "bawa", "klinik", "dekat", "periksa", "lebih", "lanjut"],
                                ["terima", "kasih"],
                                ["terima", "kasih", "akan", "segera", "buat", "janji", "dokter", "hewan"],
                                ["terima", "kasih", "seperti", "sangat", "bantu"]]

        # Check if any LS_END_6-related keywords or combinations are present in the user input
        if any(word in user_message for word in ls_end_6_keywords) \
                or any(all(word in user_message for word in combination) for combination in ls_end_6_combinations):
            del context.user_data['conversational_state']
            context.user_data['conversational_state'] = 'LS_END_6'
            update.message.reply_text("Terima kasih kembali karena telah menggunakan layanan konsultasi kami dan senang bisa membantu Anda! "
                                    "Semoga kucing atau anjing Anda bisa cepat sehat dan ceria kembali!❤️🐱")




   #penentu alur flow penyakit
    
    # ringworm    
    elif conversational_state is None:
          
        if "bulu" in user_message and "rontok" in user_message \
                or "bulunya" in user_message or "rontok" in user_message \
                or ("tidak" in user_message and "nafsu" in user_message and "makan" in user_message) \
                or ("tidak" in user_message and "makan" in user_message) \
                or ("kulit" in user_message and "berwarna" in user_message and "merah" in user_message) \
                or ("kulit" in user_message and "luka" in user_message and "warna" in user_message and "merah" in user_message):
                    context.user_data['conversational_state'] = 'RW_POSITIVE_1'
                    update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya sisa kulit kering seperti ketombe? \n \n \n \n conversational State: {}".format( context.user_data))
        #scabies
        elif 'membengkak' in user_message and ('muka' in user_message or 'kelopak mata' in user_message)\
                or 'menggesek' in user_message and ('kulit' in user_message or 'gelisah' in user_message)\
                or 'luka' in user_message and ('garuk' in user_message or 'keras' in user_message):
                context.user_data['conversational_state'] = 'SB_POSITIVE_2'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penebalan pada kulit yang mengakibatkan kerontokan bulu? \n \n \n \n conversational State: {}".format( context.user_data))
        
        #skin alergies
        elif(('muka' in user_message or 'mata' in user_message) and 'bengkak' in user_message and 'berair' in user_message) \
        or ('telinga' in user_message and 'membengkak' in user_message and 'cairan kuning' in user_message):
            context.user_data['conversational_state'] = 'SA_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, kulit yang memerah meradang karena suka di garuk (gatal)? \n \n \n \n \n conversational State: {}".format( context.user_data))
        


        elif any(word in user_message for word in rabies_keywords) \
            or any(all(word in user_message for word in combination) for combination in rabies_similar_combinations):
            context.user_data['conversational_state'] = 'RA_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, takut dengan air dan nafsu makannya menurun? \n \n \n \n \n conversational State: {}".format( context.user_data))


        elif any(word in user_message for word in leptospirosis_keywords) \
            or any(all(word in user_message for word in combination) for combination in leptospirosis_similar_combinations):
                context.user_data['conversational_state'] = 'LS_POSITVE_1'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda. Saya menduga ada kemungkinan LEPTOSPIROSIS. Apakah ada gejala tambahan yang dapat anda sampaikan? \n \n \n conversational State: {}".format(context.user_data))

        elif any(word in user_message for word in heartworm_keywords) \
            or any(all(word in user_message for word in combination) for combination in heartworm_similar_combinations):
                context.user_data['conversational_state'] = 'HW_POSITIVE_1'
                update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penurunan nafsu makan dan berat badan? \n \n \n conversational State: {}".format(context.user_data))





        #FLUTD

        elif any(word in user_message for word in flutd_keywords) \
        or any(all(word in user_message for word in combination) for combination in flutd_similar_combinations):
            context.user_data['conversational_state'] = 'FD_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, adanya penurunan nafsu makan dan berat badan? \n \n \n conversational State: {}".format(context.user_data))
        
        # Distemper
        
        elif any(word in user_message for word in distemper_keywords) \
        or any(all(word in user_message for word in combination) for combination in distemper_similar_combinations):
            context.user_data['conversational_state'] = 'DT_POSITIVE_1'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, mengalami muntah disertai diare? \n \n \n conversational State: {}".format(context.user_data))

        #diabetes
        elif any(word in user_message for word in diabetes_keywords) \
        or any(all(word in user_message for word in combination) for combination in diabetes_similar_combinations):
            context.user_data['conversational_state'] = 'DIABETES_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, kualitas bulu menjadi buruk atau mengalami keriput pada kulitnya? \n \n \n conversational State: {}".format(context.user_data))


        #catflu
        
        elif any(word in user_message for word in catflu_keywords) \
        or any(all(word in user_message for word in combination) for combination in catflu_similar_combinations):
            context.user_data['conversational_state'] = 'CATFLU_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, terdapat sariawan di bagian lidah/gusi sehingga tidak mau makan? \n \n \n conversational State: {}".format(context.user_data))


        # canine parvovirus
        # Check if any CANINE_PARVOVIRUS-related keywords or similar combinations are present in the user message
        elif any(word in user_message for word in parvovirus_keywords) \
        or any(all(word in user_message for word in combination) for combination in parvovirus_similar_combinations):
            context.user_data['conversational_state'] = 'CANINE_PARVOVIRUS_DETECTED'
            update.message.reply_text("Mohon maaf atas keadaan hewan peliharaan anda sedang kurang baik. Untuk memberikan diagnosa yang lebih akurat terkait penyakitnya, apakah ada gejala tambahan yang mungkin dialami oleh hewan peliharaan anda? Misalnya, mengalami muntah disertai diare? \n \n \n conversational State: {}".format(context.user_data))
      
        elif 'resett' in user_message:
         del context.user_data['conversational_state']
         update.message.reply_text("Reset! \n \n conversational State: {}".format( context.user_data))


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
