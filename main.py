from pyrogram import Client, filters, enums, idle
import logging
import time

logging.getLogger("pyrogram").setLevel(logging.ERROR)

API_ID = 15391168
API_HASH = "687ad15281afb4c713ecfdb7eb4dc0c1"
SESSION = "BQDq2cAAdfyfIQWWRik3w50H_V4RwlNV-4OMcjlU9ssbqtDmKOZ4A1jG50h49c7wXa8U88juQsqaY-eeT-eMfaLTJBxy-vn56rOz-QCpQV7yrBC9fnpwPkzx2N9iAIUIrmY_bCi_zwzr0_anS1KotVGIpxna3EkD4_clrJ-iW1tjaD-0spj545USrkY3eOXjx6Wdstg-ztbqmP3fZTcqWZq-_smKNvROEWWIUSBXNdIT4nkZ7Lau5__zaWnaTeq6p7kJwR6H9TTmxvfBo089xTWB8bCXyXi-DIj0zF7qCav7HgqBgcK0rQYfTchU5-RJl9xwCckM_LTW_X0AKHQ0IKnxcztsRwAAAABr0tDzAA"
CHANNEL1 = [-1001967985329] #CryptoSignal 
CHANNEL2 = [-1002134043782] #DailyCrypto 
CHANNEL3 = [-1001836953820] #NFTs 
CHANNEL4 = [-1001735485488] #Forex 
CHANNEL5 = [-1001884616660] #CryptoMarket 
CHANNEL6 = [-1001650528840] #CryptoCharts 
CHANNEL7 = [-1002013242101, -1001756925514] #OnlyFans 
CHANNEL8 = [-1001158173226, -1001519261559, -1001135294866, -1001773596827,  -1001814299872, -1001375391249, -1001682050761] #KoreanPorn 
CHANNEL9 = [-1001141525624, -1001501735081] #Indian 
CHANNEL10 = [-1001930410361, -1001186856961, -1001170620390, -1001253718428] #Adults 

SEND_CHANNEL1 = -1001975545088
SEND_CHANNEL2 = -1001815583176 
SEND_CHANNEL3 = -1001616172559
SEND_CHANNEL4 = -1001963654938
SEND_CHANNEL5 = -1001662625654
SEND_CHANNEL6 = -1001845206438
SEND_CHANNEL7 = -1002036716708
SEND_CHANNEL8 = -1002024134723
SEND_CHANNEL9 = -1002041927691
SEND_CHANNEL10 = -1001919387481

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
