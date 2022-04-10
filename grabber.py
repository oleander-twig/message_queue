from bs4 import BeautifulSoup, SoupStrainer
import requests
import queue


def grabber(root_link):
    response = requests.get(root_link)

    list_of_links = []

    for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'][0:6] == '/wiki/':
                if link['href'][6:10] != 'File' and link['href'][6:10] != 'Help':
                    link = "https://en.wikipedia.org"+link['href']
                    #print(link)
                    list_of_links.append(link)

    return list_of_links

def find_path(start_link, finish_link):

    q = queue.Queue()
    q.put(start_link)

    v = dict()
    v[start_link] = ''

    while True:
        link = q.get()
        list_of_links = grabber(link)

        for l in list_of_links:
            if l not in v.keys():
                v[l] = link

        if finish_link in list_of_links:
            break
        [q.put(l) for l in list_of_links]
    
    path = []
    path.append(finish_link)

    link = v[finish_link]
    while link != start_link:
        path.append(link)
        print(link)
        link = v[link]
    
    path.append(start_link)
    
    return len(path), path[::-1]

