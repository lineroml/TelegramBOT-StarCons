import graficas

def start(update, context):
    update.message.reply_text("Saludos, Estrellita!")
    saludo = "saludo.txt"
    f = open(saludo, encoding='utf8').read()
    update.message.reply_text(f)

def stars(update, context):
    graficas.allstars()
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('allstars.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def boyero(update,context):
    graficas.cns("Boyero")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Boyero.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def casiopea(update,context):
    graficas.cns("Casiopea")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Casiopea.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def cazo(update,context):
    graficas.cns("Cazo")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Cazo.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def cygnet(update,context):
    graficas.cns("Cygnet")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Cygnet.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def geminis(update,context):
    graficas.cns("Geminis")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Geminis.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def hydra(update,context):
    graficas.cns("Hydra")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('Hydra.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def osamayor(update,context):
    graficas.cns("OsaMayor")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('OsaMayor.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def osamenor(update,context):
    graficas.cns("OsaMenor")
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('OsaMenor.png', 'rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")

def allcons(update,context):
    update.message.reply_text("Espera un momento... ⭐️")
    graficas.allcns()
    chatid = update.message.chat.id
    try:
        context.bot.send_photo(chat_id=chatid, photo=open('allcons.png','rb'))
    except Exception as e:
        update.message.reply_text("No pude mostrar nada.. :c")


