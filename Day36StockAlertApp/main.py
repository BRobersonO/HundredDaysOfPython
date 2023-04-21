import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "IBM"
COMPANY_NAME = "IBM"
TODAY = date.today()
YESTERDAY = str(TODAY - timedelta(days=1))
DAYBEFOREYESTERDAY = str(TODAY - timedelta(days=2))

load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get News.
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params = {
    "function": 'TIME_SERIES_DAILY_ADJUSTED',
    "symbol": STOCK,
    "outputsize": 'compact',
    "apikey":   os.getenv('STOCK_API'),
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
yesterday_close = float(stock_data['Time Series (Daily)'][YESTERDAY]['5. adjusted close'])
day_before_yesterday_close = float(stock_data['Time Series (Daily)'][DAYBEFOREYESTERDAY]['5. adjusted close'])
change = yesterday_close - day_before_yesterday_close
up_down = "up" if change > 0 else "down"
percent_change = 100 * (abs(change) / yesterday_close)
print(f"yesterday: {yesterday_close}\nday before: {day_before_yesterday_close}")
print(f"change: {change}\npercent: {percent_change}")
## STEP 2: Use https://newsapi.org
# Get news pieces for the COMPANY_NAME.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    "apiKey":   os.getenv('NEWS_API'),
    "q":        COMPANY_NAME,
    "searchIn": 'title'
}

response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
news_data = response.json()
try:
    headline = news_data['articles'][0]['title']
except:
    headline = "No news found."
print(headline)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if percent_change > 5:
    client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_API'))
    message = client.messages \
                    .create(
                        body=f"{STOCK} went {up_down} by {percent_change}%: " + headline,
                        from_=os.getenv('TWILIO_NUM'),
                        to=os.getenv('PHONE_NUM')
                    )
    print(message.sid)