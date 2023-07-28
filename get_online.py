import time
from pyrogram import Client, filters
from pyrogram.handlers import UserStatusHandler
api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
bot_token = '6165024744:AAG6Gljx2VgZlQvMnn3KKByMK_lm476wktM'
# Create a Pyrogram client instance
app = Client(
    "morse_coderbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


# Define a function to get the online status of a user
async def get_user_status(user_id):
    await app.start()
    status = await app.get_users(user_id)
    print(status)
    if status.status == 'online':
        print(f"The user with ID {user_id} is online.")
    else:
        print(f"The user with ID {user_id} is offline.")
# 2nd way
# async def check_user_online(user_id):

#     while True:
#         if app.is_connected:

#             user_data = await app.get_users(user_id)
#             global start_time

#             last_online_data = user_data.last_online_date

#             if last_online_data == None :
#                 print("Online")
#             if last_online_data != None :
#                 print ("Offline")



app.run(get_user_status(1896596326))
