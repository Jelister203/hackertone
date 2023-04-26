import requests
import telegram
import os
import csv
import time
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SLEEP_TIME = 5
ENDPOINT = 'http://127.0.0.1:8000'

bot = telegram.Bot(token=TELEGRAM_TOKEN)
message = 'Ой-ой! Нашли беду! Че делать? Помогите!'

def main():
	response = requests.get(ENDPOINT).json()
	if response < 80:
		bot.send_message(TELEGRAM_CHAT_ID, message)


if __name__ == "__main__":
	while True:
		main()
		time.sleep(SLEEP_TIME)
