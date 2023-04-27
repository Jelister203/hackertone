import requests
import telegram
import os
import csv
import time
import random
from dotenv import load_dotenv


load_dotenv()

MESSAGE = 'Ой-ой! Нашли беду! Че делать? Помогите!'
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT = telegram.Bot(token=TELEGRAM_TOKEN)
SLEEP_TIME = 5

def is_valid(request):
	"""Проверяет данные на наличие аномалий. Возвращает True, если аномалии не обнаружены"""
	pass

def sender():
	"""Временная заглушка. Эмулирует входящие данные."""
	while True:
		data = random.randint(0, 100)
		main(data)
		time.sleep(SLEEP_TIME)

def main(request):
	"""на вход получает данные (pandas, numpy или журнал, хз), проверяет их и в случае некорректности отправляет смс через ТГ бота."""
	if not is_valid(request):
		BOT.send_message(TELEGRAM_CHAT_ID, MESSAGE)


if __name__ == "__main__":
	sender()
