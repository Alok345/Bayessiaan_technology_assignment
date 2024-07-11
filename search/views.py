import requests
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'search/index.html')

def search(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    cabin_selection = request.GET.get('cabin_selection')

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    json_data = {
        'origin': origin,
        'destination': destination,
        'partnerPrograms': [
            'Air Canada',
            'United Airlines',
            'KLM',
            'Qantas',
            'American Airlines',
            'Etihad Airways',
            'Alaska Airlines',
            'Qatar Airways',
            'LifeMiles',
        ],
        'stops': 2,
        'departureTimeFrom': '2024-07-09T00:00:00Z',
        'departureTimeTo': '2024-10-07T00:00:00Z',
        'isOldData': False,
        'limit': 302,
        'offset': 0,
        'cabinSelection': [cabin_selection],
        'date': '2024-07-09T12:00:17.796Z',
    }

    response = requests.post('https://cardgpt.in/apitest', headers=headers, json=json_data)
    data = response.json()

    return JsonResponse(data)
