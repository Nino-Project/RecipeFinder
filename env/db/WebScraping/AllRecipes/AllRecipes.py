# To extract data from Allrecipes. In addition, ingredients that are not
#   identified inside full_ingredients table will be added.

import requests
from bs4 import BeautifulSoup as bSoup

# Appetizers and snaks. Overall amount of web pages 314
URL = 'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/?page='


web_stat = requests.get(URL)

soup = bSoup(requests.get(URL).text, 'html.parser')

x = 1
y = 0  # Test Delete me

URL = URL + str(x)

while web_stat.status_code != 404:
    soup = bSoup(requests.get(URL).text, 'html.parser')

    # Recipes are displayed in a grid format
    recipe_grid = soup.find_all('article', {'class': 'fixed-recipe-card'})

    for row in recipe_grid:
        y += 1
        print('Recipe Number: ', y)

        # Get recipe image link. Download image later at a later process
        recipe_image = row.find(
            'div', {'class': 'grid-card-image-container'}).img['data-original-src']

        # Get recipe title
        recipe_title = (
            row.find('span', {'class': 'fixed-recipe-card__title-link'})).get_text()

        # Get recipe link
        recipe_link = row.find(
            'div', {'class': 'grid-card-image-container'}).a['href']

        # Get recipe rating
        recipe_rating = row.find(
            'div', {'class': 'fixed-recipe-card__ratings'}).span['data-ratingstars']
        recipe_rating = round(float(recipe_rating), 2)

        print(recipe_image)
        print(recipe_title)
        print(recipe_link)
        print(recipe_rating)
        print('____________________')
        print('---URL HERE---:', URL)

    # Removing web page number
    URL = URL[:-(len(str(x)))]
    # Changing web page number with an increment of 1
    x += 1
    # Inserting new web page number
    URL = URL + str(x)
    web_stat = requests.get(URL)
