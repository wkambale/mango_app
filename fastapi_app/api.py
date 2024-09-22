from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = FastAPI()

# Load your TensorFlow model
model = tf.keras.models.load_model('model/mango_model.h5')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        image = image.resize((224, 224))  # Adjust size for your model
        image_array = np.array(image) / 255.0  # Normalize if needed
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict using the model
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)
        class_names = ["Anthracnose", "Bacterial-Black-spot", "Fruitly", "Healthy-mango", "Others"]
        
        return JSONResponse(content={"prediction": class_names[predicted_class[0]]})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
