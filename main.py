import data_files
import requests
from twilio.rest import Client

STOCK_NAME = "AXIS"
COMPANY_NAME = "Axis Bank"
TWILIO_SID = "ACefb6d7b3f5fb3fbd3dd3b82f4537deb8"
TWILIO_AUTH_TOKEN = "b5c954e144de0b1285cadc73f095b785"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7e58e64a472a416da431127b93f56eed"


required_data = data_files.stocks_data[STOCK_NAME]
yesterday_price = float(required_data[0])
day_before_yesterday_price = float(required_data[1])
difference = yesterday_price - day_before_yesterday_price
percentage = round((difference / yesterday_price) * 100)


up_down = None
if difference > 0:
    up_down = "Up By"
else:
    up_down = "Down By"


#Setting up the client for TWILIO for sending the messages.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
if abs(percentage) >= 1:
    news_parameter = {
                "qInTitle": COMPANY_NAME,
                "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_data = news_response.json()["articles"]
    first_three = news_data[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{abs(percentage)}%\nHeadline : {article['title']}."
                          f" \nBrief: {article['description']}" for article in first_three]
    for articles in formatted_articles:
        message = client.messages.create(
                    body=articles,
                    from_='+16206708975',
                    to='+917033543642'
        )
