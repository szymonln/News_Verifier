from django.shortcuts import render, redirect
from .models import *
import requests
from text_analysis.analyzer import *
API_KEY = "a3314aa931d244f9bfabe30e5e721446"


# Create your views here.
def add_preferences(request):
    providers = NewsProvider.objects.all()

    if request.POST:
        form = request.POST.dict()

        request.session['selected_domains'] = []

        for field in form:
            if field != 'csrfmiddlewaretoken':
                request.session['selected_domains'].append(field)

        return redirect("/news_list")

    return render(request, 'add_preferences.html', {'providers': providers})


def news_list(request):
    news_json = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news&apiKey="+API_KEY).json()

    if request.POST:
        form = request.POST.dict()
        keystring = form.get("search")
        search_string=""
        keywords = keystring.split(" ")
        for keyword in keywords:
            search_string += keyword + " AND "
        domains = ""
        for domain in request.session['selected_domains']:
            domains += domain + ","

        url = "https://newsapi.org/v2/everything?q="+search_string[:-5]+"&domains="+domains[:-1]+"&apiKey="+API_KEY
        news_json_queried = requests.get(url).json()
        for news in news_json_queried['articles']:
            if news['urlToImage'] is None:
                news['urlToImage'] = "/static/news_icon.png"

        return render(request, 'news_list.html', {'news_list': news_json_queried['articles'],
                                                  'show_providers': "True",
                                                  'providers': request.session['selected_domains']})

    return render(request, 'news_list.html', {'news_list': news_json['articles'],
                                              'google_news': ["Google News Top Headlines"],
                                              'show_providers': "False",
                                              'providers': request.session['selected_domains']})


def news_keywords(request):
    domains = ""
    for domain in request.session['selected_domains']:
        domains += domain + ","

    if request.POST:
        form = request.POST.dict()
        text = form.get("text")
        english = form.get("english")
        polish = form.get("polish")

        keywords = []
        if polish:
            keywords = find_polish_keywords(text)
        if english:
            keywords = find_english_keywords(text)

        search_string = ""

        for keywoard in keywords:
            search_string += keywoard + " OR "

        print(search_string)

        url = "https://newsapi.org/v2/everything?q=" + search_string[:-5] + "&domains=" + domains[:-1] + "&apiKey=" \
              + API_KEY
        news_json_queried = requests.get(url).json()
        for news in news_json_queried['articles']:
            if news['urlToImage'] is None:
                news['urlToImage'] = "/static/news_icon.png"

        return render(request, 'news_list.html', {'news_list': news_json_queried['articles'],
                                                  'providers': request.session['selected_domains']})

    return render(request, "news_check.html", {'providers': request.session['selected_domains']})

