from pyrogram import Client, filters, enums, idle
import logging
import time

logging.getLogger("pyrogram").setLevel(logging.ERROR)

API_ID = 6595979
API_HASH = "b9625545e9f261a600a049de0b0c310f"
SESSION = "BQBkpYsARGNkSGWYpxDqD26bc1erDPzuFv3hOs0W_E2hs6W2CEgYS-43rXAoEmGiXb7FkegOl-eUsqfzaMlLzk0BBJAHAfG_zDd-01SL6UCf6_a9qdu48EPK5qiVuh5QBj7ymggKwM6T5jKdz95Q4V0fvA047z9gwEsrsvvKBJa6R0Dpq91t-k3Cb4G8m7_Da4FFhd46ZHeZ2xuO0ANhL4W2OGfyEs9g1GtIKB7pBdyxF3LfyS8psI6Y6oQkxqo4CfQhXxfwIOSPRKtcBBTGcnWAxgddw3uT3ZSFuAB0E4gt6oNXxcrB7RHCH29oD2a5Uxy-tsRtH52SyC1nEduMMzWIb-qaswAAAABFk733AA"

CHANNEL1 = [-1001897432334, -1001478977791, -1001194350502] #OngoingSeries
CHANNEL2 = [-1001747183207, -1001658823824] #Piro
CHANNEL3 = [-1001984102010, -1001427229068, -1001722591434, -1001820463923] #CompleteSeries
CHANNEL4 = [-1001983865029, -1001540209531] #PSAMovies
CHANNEL5 = [-1001983663269, -1001840284965, -1001845745571, -1001893184231, -1001462116979, -1001178597606, -1001232464002, -1001321859563, -1001455978726, -1001343951559. -1001759509745] #CompleteKDrama
CHANNEL6 = [-1001989199891, -1001523206621, -1001968208619, -1001678405222] #OngoingKDrama
CHANNEL7 = [-1001970252335, -1001958133498, -1001988107339, -1001581505528, -1001725996591, -1001910441299, -1001747183207, -1001681252607, -1001965916532, -1001540209531, -1001752179568, -1001173751594, -1001166869881, -1001710373179, -1001882096740, -1001595465160, -1001341832564, -1001789691279, -1001805048438] #MovieOnly
CHANNEL8 = [-1001973242128, -1001565540536, -1001392626208, -1001556597544, -1001603305985, -1001650528840, -1001622699395, -1001740835149, -1001633231799, -1001763180500, -1001747183207, -1001268152345, -1001916983429, -1001552423277, -1001671756297] #ForwardCharts
CHANNEL9 = [-1001948931098, -1001161683441, -1001622654998, -1001582520126, -1001727857237, -1001479511317, -1001520053536, -1001327651210, -1001391574614, -1001498123299] #ForwardFreeSignals
CHANNEL10 = [-1001946181391, -1001432744861, -1001545582527, -1001650528840, -1001694883826, -1001758117730, -1001584909083, -1001624286558, -1001692913358, -1001575723251, -1001744021073] #ForwardVipSignals

SEND_CHANNEL1 = -1001566642237
SEND_CHANNEL2 = -1001519694012 
SEND_CHANNEL3 = -1001622478032
SEND_CHANNEL4 = -1001620200646
SEND_CHANNEL5 = -1001705433155
SEND_CHANNEL6 = -1001584832671
SEND_CHANNEL7 = -1001396095544
SEND_CHANNEL8 = -1001860621182
SEND_CHANNEL9 = -1001589760625
SEND_CHANNEL10 = -1001611517743

time.sleep(60)
user = Client(
  name='Auto_Forwarder',
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=SESSION
).start()

media_filter = (filters.document | filters.video | filters.photo | filters.text)

@user.on_message(filters.chat(CHANNEL1) & media_filter)
async def media1(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL1)

@user.on_message(filters.chat(CHANNEL2) & media_filter)
async def media2(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL2)

@user.on_message(filters.chat(CHANNEL3) & media_filter)
async def media3(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL3)

@user.on_message(filters.chat(CHANNEL4) & media_filter)
async def media4(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL4)

@user.on_message(filters.chat(CHANNEL5) & media_filter)
async def media5(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL5)

@user.on_message(filters.chat(CHANNEL6) & media_filter)
async def media6(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL6)

@user.on_message(filters.chat(CHANNEL7) & media_filter)
async def media7(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL7)

@user.on_message(filters.chat(CHANNEL8) & media_filter)
async def media8(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL8)

@user.on_message(filters.chat(CHANNEL9) & media_filter)
async def media9(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL9)

@user.on_message(filters.chat(CHANNEL10) & media_filter)
async def media10(_, message):
  time.sleep(10)
  await message.copy(SEND_CHANNEL10)

print(f'\n\n{user.me.first_name} Started!\n\n')
idle()
