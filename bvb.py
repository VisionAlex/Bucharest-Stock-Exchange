from bs4 import BeautifulSoup
import requests
import csv
import re

class Bvb:

	@staticmethod
	def get_price(ticker):
		url =''.join(['http://bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=', ticker])
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		value = soup.find('strong').text
		return float(value)

	@staticmethod
	def get_csv_data():
		url ='https://www.bvb.ro/FinancialInstruments/Markets/SharesListForDownload.ashx?filetype.csv'
		response= requests.get(url)
		with open('bvb_data.csv', 'wb') as f:
			f.write(response.content)
	
	@staticmethod
	def get_ticker_list():
		ticker_list =[]
		url ='https://www.bvb.ro/FinancialInstruments/Markets/SharesListForDownload.ashx?filetype.csv'
		response = requests.get(url)
		for c in response.iter_lines():
			ticker_list.append(str(c).split(';')[0].strip('b\''))
		return ticker_list[1:]
			
	@staticmethod
	def get_ticker_name_price(ticker):
		url =''.join(['http://bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=', ticker])
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		try:
			name = soup.h2.text.strip("\r\n ")
			price = float(soup.strong.text)
		except Exception as e:
			print(e)
		if name and price:
			return (ticker, name, price)

#ticker_list = Bvb.get_ticker_list()
#print(ticker_list)
