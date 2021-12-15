import requests
from bs4 import BeautifulSoup
import os

url = "https://www.airbnb.co.uk/s/bergen/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=december&flexible_trip_dates%5B%5D=january&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&search_type=unknown"


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)







'''
Beginning of program - 
Downloading images via scraping
Returns title at this point to show server communicating

'''








'''

<picture><source srcset="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=320 1x, https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=720 2x" media="(max-width: 743px)"><source srcset="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=720 1x, https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=1440 2x" media="(min-width: 743.1px) and (max-width: 1127px)"><source srcset="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=1200 1x, https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=2560 2x" media="(min-width: 1127.1px) and (max-width: 1439px)"><source srcset="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=1680 1x, https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=2560 2x" media="(min-width: 1439.1px)"><img class="_1cb9q3xq" aria-hidden="true" alt="Image 1" loading="eager" src="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=720" data-original-uri="https://a0.muscache.com/im/pictures/718f72ad-d154-49cc-8f54-ad5cb2ef3398.jpg?im_w=720" style="object-fit: cover;"></picture>


'''