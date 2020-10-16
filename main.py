#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:20 2020

@author: IvanPopravka

WARNING: all the URLs must be taken from https://bcs-express.ru/kotirovki-i-grafiki
You choose shares, futures, etc. Then click it and copy the full URL. As it showed
above but with the /any-share-name ending
"""
import requests
import pync

from bs4 import BeautifulSoup
from time import sleep

# You can set yours. Just google "What is my user-agent" and then copy-paste it.
headers = {"user-agent":"Mozilla/5.0 (Linux; Android 7.0; BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"}


class Stock_object:
	""" Class which defines the stock object"""

	def __init__(self, url, headers=headers):
		self.url = url
		self.headers = headers
		self.title = self.set_title()
		self.currency = self.set_currency()

	def set_title(self):
		""" Function to set title at the beginning"""
		request = requests.get(url=self.url, headers=headers)
		data = request.text
		soup = BeautifulSoup(markup=data, features="lxml")
		title = soup.find('h1').text
		return title
	
	def set_currency(self):
		""" Function to define currency at the beginning"""
		request = requests.get(url=self.url, headers=headers)
		data = request.text
		soup = BeautifulSoup(markup=data, features="lxml")
		currency = soup.find(name='div', attrs={'class', 'js-currency-code'}).text
		return currency

	def set_initial_value(self):
		"""As the variable must be initialized before the comparison
			this function sets the initial value for this variable"""
		request = requests.get(url=self.url, headers=headers)
		data = request.text
		soup = BeautifulSoup(markup=data, features="lxml")
		initial_value = soup.find(name='div', attrs={'class','js-price-close'}).text
		return initial_value

	def send_notification(self, new_value, profit):
		"""Function that runs pop up notification (requires Mac Software)"""
		message = f"New price for {self.title} = {new_value} ({profit}%)"
		pync.notify(message, title='Stock market', sound='Apple')
		print("[!] INFORMED\n")

	def calculate_profit(self, new_value, old_value):
		"""Function which counts the difference in %, where
		increase = (new-origin)/origin*100 and
		decrease = (origin-new)/origin*100"""
		new_value = float(new_value.replace(',','.'))
		old_value = float(old_value.replace(',','.'))

		if (new_value - old_value) > 0:
			increase = (new_value - old_value)/old_value * 100
			return round(increase, ndigits=3)

		elif (new_value - old_value) < 0:
			decrease = (old_value - new_value)/old_value * 100 * (-1)
			return round(decrease, ndigits=3)

		else:
			return 0

	def start_extracting_info(self):
		"""Function which waites for the change of the old price
		and then prints its difference in % and calls the 
		notification function"""
		old_price_value = self.set_initial_value()
		new_price_value = old_price_value
		print(f"[starting point] = {old_price_value}\n")

		while True:
			if old_price_value == new_price_value:
				while old_price_value == new_price_value:
					request = requests.get(url=self.url, headers=headers)
					print(f"[response] - {request.status_code}") # Can comment it. Just for debugging
					data = request.text
					soup = BeautifulSoup(markup=data, features="lxml")
					new_price_value = soup.find(name='div', attrs={'class', 'js-price-close'}).text
					sleep(5)
			else:
				profit = self.calculate_profit(new_price_value, old_price_value)
				self.send_notification(new_price_value, profit)
				old_price_value = new_price_value
				print(f"[NEW starting point] = {new_price_value}")
				print(f"[Percentage Change] = {profit} % \n")
				sleep(10)

	def run(self):
		"""Function to run the script"""
		print(f"[title] - {self.title}")
		print("[status] - Running...")
		self.start_extracting_info()

if __name__ == "__main__":
	obj1_url = 'https://bcs-express.ru/kotirovki-i-grafiki/yakg'
	obj1 = Stock_object(url=obj1_url)
	obj1.run()