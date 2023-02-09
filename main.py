# Парсинг главной новостной страницы Sci Rus

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_scientificrussia_posts():
    url = 'https://scientificrussia.ru/news'
    url_SR = 'https://scientificrussia.ru'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.find_all('div', 'wrapper')
    scientificrussia_df = pd.DataFrame()
    for el in news:
        title = el.find('div', 'title').text.strip()
        link = el.find('a').get('href')
        date = el.find('div', 'prop time').text

        news_url = url_SR + link

        res_article = requests.get(news_url)
        soup_article = BeautifulSoup(res_article.text, 'html.parser')
        news_article = soup_article.find_all('div', 'container')
        # for item in news_article:
        article = el.find('p').text

        row = {'date': date, 'title': title, 'description': article, 'link': news_url}
        scientificrussia_df = pd.concat([scientificrussia_df, pd.DataFrame([row])])
    scientificrussia_df.to_excel('./SciRus.xlsx', sheet_name='SciRus', index=False)
    return scientificrussia_df


get_scientificrussia_posts()