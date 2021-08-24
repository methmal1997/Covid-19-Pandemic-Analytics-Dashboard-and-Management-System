from django.shortcuts import render
import requests


# Create your views here.
def index2(request):
    r = requests.get(
        'http://api.mediastack.com/v1/news?access_key=86487dbfd37aa1c7ee940cfb176b6e3e&languages=en&categories=health&keywords=covid&sort=published_desc&published_at&limit=1')
    res = r.json()
    data = res['data']
    icon = []
    title = []
    description = []
    image = []
    url = []
    publish = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        publish.append(i['published_at'])
    icon = zip(title, description, image, url, publish)
    return render(request, 'index2.html', {'icon': icon})


def news(request):
    r = requests.get(
        'http://api.mediastack.com/v1/news?access_key=86487dbfd37aa1c7ee940cfb176b6e3e&languages=en&categories=health&keywords=covid&sort=published_desc&published_at')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    publish = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
        publish.append(i['published_at'])
    news = zip(title, description, image, url, publish)

    return render(request, 'news.html', {'news': news})


def dashboard(request):
    return render(request, 'Dashbord.html')


def covidtest(request):
    return render(request, 'Covid Testing.html')


def hospital(request):
    return render(request, 'Hospital.html')


def vaccination(request):
    return render(request, 'vaccination.html')


def fund(request):
    return render(request, 'fund.html')


def world(request):
    data = True
    globalSummary = None
    countries = None;
    while (data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request, 'world.html',
                  {'globalSummary': globalSummary,
                   'countries': countries})


def lnews(request):
    return render(request, 'local news.html')


def guide(request):
    return render(request, 'guidline.html')


def test(request):
    return render(request, 'test.html')


def temp(request):
    return render(request, 'tempory.html')


def info(request):
    return render(request, 'info.html')
