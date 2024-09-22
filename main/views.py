from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            try:
                # Convert the file to the format required for sending to FastAPI
                file_data = file.read()  # Read the image file
                files = {'file': (file.name, file_data, file.content_type)}

                # Make a request to FastAPI with the image
                response = requests.post('http://127.0.0.1:8000/predict/', files=files)
                
                # Check if FastAPI responds with a successful prediction
                if response.status_code == 200:
                    prediction = response.json().get("prediction")
                    return render(request, 'result.html', {'prediction': prediction, 'filename': file.name})
                else:
                    return render(request, 'index.html', {'error': f"Error from FastAPI: {response.status_code} - {response.text}"})
            except Exception as err:
                return render(request, 'index.html', {'error': f"An error occurred: {err}"})
        else:
            return render(request, 'index.html', {'error': 'No file uploaded!'})
    
    return render(request, 'index.html')
