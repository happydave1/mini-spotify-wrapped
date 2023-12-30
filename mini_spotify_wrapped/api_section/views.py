from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def main(request):
    d = {
        'data': 'hello from django.',
    }
    return JsonResponse(d)
