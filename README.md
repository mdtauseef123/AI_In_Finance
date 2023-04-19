This project helps in predictive analysis on the stock price of the specified stocks.
This project is written in Python.
It works in the following manner:- 
  i.Firstly it will fetch the specified stock's data yesterday and day before yesterday closing price.
  ii.Then it will calculate the difference of that price and then percentage difference.
  iii.If the percentage difference is greater than or equal to 1 then it will send an alert message to the registered users.(Here I have uses the Twilio API for sending    the text messages and News API for fecthing news regarding that particular company.
  iv. Since the news count is very high so I just use first 3 articles of the results.
  v.And at last send the message to the user.
