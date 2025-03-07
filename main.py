import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

tags = soup.find_all("h3",class_="title")
titles = [title.get_text() for title in tags]
# for title in tags:
#     titles.append(title.get_text())

with open("MovieList.txt",'w',encoding="utf-8") as file:
    for i in range(len(titles)-1,-1,-1):
        file.write(f"{titles[i]}\n")

# # responses = requests.get("https://www.imdb.com/chart/top/")
# responses = requests.get("https://www.chess.com/games/bobby-fischer")
# web_page = responses.text

# soup = BeautifulSoup(web_page,'html.parser')
# print(soup.prettify())

# import requests
# from bs4 import BeautifulSoup

# # Step 1: Send a GET request to the URL
# url = "https://www.chess.com/games/bobby-fischer"
# response = requests.get(url)


# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.find("div",class_="master-players-value"))