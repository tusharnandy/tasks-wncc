import requests
url = ('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c01a9f3954ac44fca17a8743cdc4c503')
tech_news = requests.get(url).json()
article = tech_news['articles']
headlines = []
brief = []

for i in article:
    headlines.append(i['title'])
    brief.append(i['description'])

for i in range(len(headlines)):
    check = True
    for j in range(0, i):
        if headlines[j] == headlines[i]:
            check = False
    if(check):
        print(f"{i+1}: {headlines[i]}")
        print(brief[i])
        print('')
