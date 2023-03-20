from pyrogram import Client , filters

app = Client("muhyohelp")

@app.on_message(filters.text)
async def send_me(Client , messange):
    id = messange.from_user.id
    first_name = messange.from_user.first_name
    user_username = messange.from_user.username
    time = messange.date
    text = messange.text
    date_date = f"{time:%m.%d}"
    date_time = f"{time:%H:%M:%S}"

    kuchukcha = "@"

    if user_username == None:
        user_username = "Yo'q"
        kuchukcha = ""
    else :
        user_username = messange.from_user.username

    xabar = f" ID : ** `{id}` ** \nIsm : ** [{first_name}](tg://user?id={id}) ** \nUsername : ** {kuchukcha}{user_username}** \nSana : ** {date_date} ** \nVaqt: **{date_time}** \nXabar : ** {text} **  "
    # await app.send_message(f"{id}","Habaringiz @muhyo07 ga yuborildi Agar 3 soat ichida javob yozmasa Iltimos qaytattan yozing")
    await app.send_message('muhyohistory' , f'{xabar}' )

print("Tekshiring")
app.run()