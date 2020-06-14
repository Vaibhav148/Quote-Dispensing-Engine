import pandas as pd
quotes = pd.read_csv('quote_stash.csv')
quotes = quotes[['quote', 'author']]
quotes = quotes.drop_duplicates(subset='author', keep="last")
quotes.to_csv('quotes.csv', index=None)
