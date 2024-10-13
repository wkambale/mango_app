# Mango Damage Detection App

This is a web application that detects damages on mangoes using a TensorFlow model with Django as the frontend framework and FastAPI as the API for serving the model. The application allows users to upload images of mangoes and get predictions about the damage.

## Features

- **Multilabel classification**: Detects multiple types of damage such as Anthracnose, Bacterial-Black-spot, and more.
- **Django**: Used for the frontend and handling user uploads.
- **FastAPI**: API for serving TensorFlow models and returning predictions.
- **TensorFlow**: Pre-trained model for mango damage classification.

## Resources
- [Download the Model](https://bit.ly/pyconmodelh5)
- [Colab Notebook](https://bit.ly/vgg19-model)
- [Presentation Slides](https://speakerdeck.com/kambale/serving-machine-learning-models-in-django-with-fastapi)

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)

## Installation (Docker)

**Clone the repository:**

```bash
   git clone https://github.com/your-username/mango_app.git
   cd mango_app
```
**Download the pre-trained TensorFlow model**:

Place the `mango_model.h5` file into the `fastapi_app/model/` directory (you'll need to add the TensorFlow model file manually, as it is not part of this repository).

**Build the Docker image**:

Run the following command in the project root directory to build the Docker image:

```bash
docker compose build
```

## Running the App

**Start the containers**:

Once the image is built, you can run the app using:

```bash
docker compose up
```
This will start the following containers:

A container for the Django web application.
A container for FastAPI to serve the TensorFlow model predictions.

**Access the application**:

The Django app will be available at: `http://localhost:8000/`

FastAPI will be available for prediction at: `http://localhost:8001/predict/`

## API Endpoints
**Django**
`GET /`: The home page where you can upload an image and submit it for prediction.
**FastAPI**
`POST /predict/`: API endpoint to handle image prediction using the TensorFlow model.

**Example usage with curl**:

```bash
curl -X POST "http://localhost:8001/predict/" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@path_to_image_file"
```

## Installation (Django, FastAPI)

## Requirements
- Python 3.8 or above
- Django 3.2+
- FastAPI
- TensorFlow 2.14+
- Uvicorn (for running FastAPI)

**Clone the repository**

```bash
git clone https://github.com/your-username/mango_app.git
cd mango-app
```
**Set up a virtual environment and activate it**

```bash
# For Unix-based systems (Linux/MacOS)
python3 -m venv django-env
source django-env/bin/activate

# For Windows
python -m venv django-env
django-env\Scripts\activate
```
**Install the dependencies**
```bash
pip install -r requirements.txt
```
**Set up Django app**
```bash
python manage.py migrate
```

**Run the Django server**
```bash
python manage.py runserver
```

**Run the FastAPI app**
In a separate terminal window, navigate to the project directory and run:

```bash
uvicorn fastapi_app.api:app --reload --port 8001
```

## Contribution Guidelines
We welcome contributions to the Mango Damage Detection App! Please follow these steps if you’d like to contribute:

Fork the repository: Click the "Fork" button at the top right of this page to copy this repository to your GitHub account.

Clone your forked repository: Use the command below to clone the forked repository to your local machine.

```bash
git clone https://github.com/your-username/mango_app.git
```
Create a new branch: It’s good practice to create a new branch for each feature or bug fix you’re working on.

```bash
git checkout -b feature-branch
```

Make your changes: Write your code and tests, then run the app locally to verify your changes.

Commit your changes: Once you're happy with your changes, commit them with a descriptive message.

```bash
git add .
git commit -m "Add new feature or bug fix"
```

Push to your forked repository:

```bash
git push origin feature-branch
```
Submit a pull request: Go to the original repository on GitHub, and you’ll see a prompt to submit a pull request.

## Guidelines for Contributions
Make sure to write descriptive commit messages.
If you’re fixing a bug, include the issue number in the pull request.
Write tests where applicable and ensure all tests pass before submitting the pull request.
