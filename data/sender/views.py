from django.shortcuts import render
from django.http import HttpResponse
import random

def main(request):
	mas = [100, 99, 111, 102, 112, 130, 90, 10]
	return HttpResponse(f'{mas[random.randint(0, 7)]}')