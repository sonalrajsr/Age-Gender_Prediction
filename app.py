from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import ELU
from tensorflow.keras.losses import MeanAbsoluteError
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # Ensure 'static/' folder exists

# Load your saved model with custom objects
custom_objects = {
    'ELU': ELU,
    'mae': MeanAbsoluteError()
}

model = tf.keras.models.load_model('model/model.h5', custom_objects=custom_objects)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        img = Image.open(filepath)
        
        # Convert image to grayscale
        if img.mode != 'L':
            img = img.convert('L')
        
        img = img.resize((200, 200))  # Resize as needed for your model
        img_array = np.array(img)

        # Preprocess the image as required by your model
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        img_array = np.expand_dims(img_array, axis=-1)  # Ensure it has one channel

        # Make predictions
        predictions = model.predict(img_array)
        gender = 'Male' if predictions[0][0] > 0.5 else 'Female'
        age = int(predictions[1][0])  # Adjust based on your model's output

        return render_template('result.html', filename=file.filename, gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)
