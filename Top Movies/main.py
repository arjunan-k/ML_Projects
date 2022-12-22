import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
a = soup.find_all(name="h3", class_="title")
movie_list = []

for tag in a:
    b = tag.getText().split()
    b.remove(b[0])
    c = ' '.join(b)
    movie_list.append(c)


def reverse_list(x):
    new_list = x[::-1]
    return new_list


final_list = reverse_list(movie_list)
with open("movie.txt", "w") as file:
    file.write("\n".join(final_list))