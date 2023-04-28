import requests
import telegram
import os
import csv
import time
import random
import mypysql
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()

MESSAGE = 'Обнаружена аномалия! Что же с ней делать?'
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT = telegram.Bot(token=TELEGRAM_TOKEN)
SLEEP_TIME = 2
con = pymysql.connect('localhost', 'user17', 
    's$cret', 'testdb')

def is_unique(string):
	with con:
		cur = con.cursor()
		cur.execute(f"SELECT {UID} FROM datasese")
		data = cur.fetchall()
		if data.count(string) == 0:
			return True
		return False

def is_valid(request):
	"""Проверяет данные на наличие аномалий. Возвращает True, если аномалии не обнаружены"""
	logger.info('Проверяем строку...')
	request = request[0].split(';')
	if not is_unique(request[1]):
		return False
	if request[7] == 'Квитанция':
		return False
	return True

def sender():
	"""Временная заглушка. Эмулирует входящие данные."""
	with open('dataset1.csv', newline='', encoding='utf-8') as csvfile:
		spamreader = csv.reader(csvfile)
		for row in spamreader:
			logger.info('Считали строку '+str(row))
			main(row)
			time.sleep(SLEEP_TIME)

def main(request):
	"""на вход получает данные (pandas, numpy или журнал, хз), проверяет их и в случае некорректности отправляет смс через ТГ бота."""
	if not is_valid(request):
		logger.warning('Обнаружена аномальная строка, сообщаем оператору.')
		BOT.send_message(TELEGRAM_CHAT_ID, MESSAGE)
	else:
		with con:
			cur = con.cursor()
			cur.execute(f"INSERT INTO datasese VALUES {request}")


if __name__ == "__main__":
	sender()
