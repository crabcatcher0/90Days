from django.shortcuts import render
import requests
import asyncio
# Create your views here.



async def homepage(request):
    url = 'https://meowfacts.herokuapp.com/'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        final_data = data.get('data')
    else:
        response = None
    
    context = {
        'data':final_data
    }
    
    return render(request, "home.html", context)