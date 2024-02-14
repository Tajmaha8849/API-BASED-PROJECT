import requests
from datetime import datetime
import pytz
IST=pytz.timezone('Asia/Kolkata')
raw_TS=datetime.now(IST)
curr_date=raw_TS.strftime("%d-%m-%Y")
curr_time=raw_TS.strftime("%H:%M:%S")


telegram_auth_token="6618522171:AAE_718qao_wMkdUIFSu4QnBsuPQ_0rW4FA"
telegram_group_id="vaccine_notifier99"

msg=f"Message Recieved on {curr_date} at {curr_time}"

def send_msg_on_telegram(message):
    telegram_api_url=f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={msg}"
    tel_resp=requests.get(telegram_api_url)

    if tel_resp.status_code==200:
        print("INFO:Notification has been sent on Telegram.")
    else:
        print("ERROR:Could not send message.")
send_msg_on_telegram(msg)