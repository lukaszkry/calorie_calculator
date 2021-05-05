# Web scrapping script

from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen

temp = []

# Loop to web scrap all pages with data
page_number = 1
while page_number < 138:    # 137 is number of pages in kalkulatorkalorii.net
    url = f'https://kalkulatorkalorii.net/tabela-kalorii/{page_number}'
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    # tab-content ->class with all data

    table_content = soup.find('div', class_ = "tab-content").find("tbody")

    # tr -> table row
    products = table_content.find_all('tr')

    for product in products:
        name = product.find("a").get_text().strip()      # get product name
        data = product.find_all("td")

        calories = data[1].get_text()
        protein = data[2].get_text()
        carbs = data[3].get_text()
        fat = data[4].get_text()
        temp.append({
            'Name' : name,
            'Calories': calories,
            'Protein': protein,
            'Carbs': carbs,
            'Fat': fat
        })
    page_number += 1
# Data frame to work with pandas
df = pd.DataFrame(temp)

# 'cleanups'
df = df.apply(lambda x: x.str.replace(',','.') if x.name != 'Name' else x)
df[['Calories', 'Protein', 'Carbs', 'Fat']] = df[['Calories', 'Protein', 'Carbs', 'Fat']].astype(float)

# export data to csv file
df.to_csv(r'calorie_base.csv', index = False)