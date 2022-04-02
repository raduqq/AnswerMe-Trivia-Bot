import wikipedia

# ! DUMMY
URL = "https://en.wikipedia.org/wiki/The_Best_FIFA_Men%27s_Player"

tokens = URL.split('/')
query = tokens[len(tokens) - 1]
page_name = wikipedia.search(query, results = 1)

page = wikipedia.page(page_name)
content = page.content

print(content)
