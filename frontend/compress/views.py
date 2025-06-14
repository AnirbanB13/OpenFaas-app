from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import requests
import os

def index(request):
    """Render the main page"""
    return render(request, 'compress/index.html')

def compress_image(request):
    """Handle image compression through Flask backend"""
    if request.method == 'POST' and request.FILES.get('image'):
        try:
            # Forward the image to Flask backend
            files = {'image': request.FILES['image']}
            response = requests.post(
                f"{settings.FLASK_BACKEND_URL}/api/compress",
                files=files
            )
            
            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse(
                    {'error': 'Compression failed'},
                    status=response.status_code
                )
                
        except requests.RequestException as e:
            return JsonResponse(
                {'error': f'Backend service error: {str(e)}'},
                status=500
            )
    
    return JsonResponse(
        {'error': 'Invalid request'},
        status=400
    ) 