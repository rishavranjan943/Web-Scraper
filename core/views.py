from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        url = request.POST.get('site', '')
        if url:
            try:
                page = requests.get(url)
                if page.status_code == 200:
                    soup = BeautifulSoup(page.content, 'html.parser')
                    link_list = []
                    for link in soup.find_all('a'):
                        list_item = [link.string, link.get('href')]
                        link_list.append(list_item)
                    return render(request, 'scrape.html', {'link_list': link_list})
                else:
                    return render(request, 'scrape.html', {'error_message': 'URL does not exist or cannot be accessed.'})
            except requests.exceptions.RequestException as e:
                return render(request, 'scrape.html', {'error_message': 'Error: ' + str(e)})
        else:
            return render(request, 'scrape.html', {'link_list': []})
    else:
        return render(request, 'scrape.html')
