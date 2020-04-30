__author__ = 'Nima Aram'
#برای اسکریپت های بیشتر به وبسایت ویرگول سر بزنید:)
from bs4 import BeautifulSoup
import requests
api_url = 'https://www.time.ir/'
response = requests.get(api_url)
soup = BeautifulSoup(response.content, 'html.parser')
varShowTodayFull = soup.find(id='ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsiNumeral').text
varShowTodayFullCar = soup.find(id='ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblShamsi').text
varShowDateInt = varShowTodayFull.split('/')
car = varShowTodayFullCar.split(' ')
if car[0] == 'پنج':
    varShowTodayCar = car[0] + car[1]
if car[0] == 'چهار':
    varShowTodayCar = car[0] + car[1]
if car[0] == 'سه':
    varShowTodayCar = car[0] + car[1]
if car[0] == 'دو':
    varShowTodayCar = car[0] + car[1]
if car[0] == 'یک':
    varShowTodayCar = car[0] + car[1]
if car[0] == 'شنبه':
    varShowTodayCar = car[0]
varShowDateYear=varShowDateInt[0]
varShowDateMonth=varShowDateInt[1]
varShowDateDay=varShowDateInt[2]
varShowMonthCar=car[4]
def ShowTodayFull():
    return varShowTodayFull
def ShowTodayFullCar():
    return varShowTodayFullCar
def ShowDateYear():
    return varShowDateYear
def ShowDateMonth():
    return varShowDateMonth
def ShowDateDay():
    return varShowDateDay
def ShowMonthCar():
    return varShowMonthCar
def ShowTodayCar():
    return varShowTodayCar
# یک اسکریپت 50 خطی تاریخ