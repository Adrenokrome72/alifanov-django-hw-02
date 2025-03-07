from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
import csv

CONTENT = []

def load_data_from_csv():
    global CONTENT
    if not CONTENT:  # Загружаем данные только один раз
        with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            CONTENT = [
                {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
                for row in reader
            ]

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    load_data_from_csv()
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
