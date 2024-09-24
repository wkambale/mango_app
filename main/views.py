from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                
                file_data = file.read()
                files = {'file': (file.name, file_data, file.content_type)}

                # Make a request to FastAPI with the image
                response = requests.post('http://127.0.0.1:8001/predict/', files=files)
                
                if response.status_code == 200:
                    prediction = response.json().get("prediction")
                    return render(request, 'results.html', {'prediction': prediction, 'filename': file.name})
                else:
                    return render(request, 'index.html', {'error': f"Error from FastAPI: {response.status_code} - {response.text}"})
            except Exception as err:
                return render(request, 'index.html', {'error': f"An error occurred: {err}"})
        else:
            return render(request, 'index.html', {'error': 'No file uploaded!'})
    
    return render(request, 'index.html')
