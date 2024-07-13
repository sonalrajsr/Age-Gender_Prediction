
# Image Gender and Age Prediction

This project uses a machine learning model to predict the gender and approximate age from an uploaded image. The model is built using TensorFlow and served using Flask.


## Features

- Predicts gender (Male/Female) and approximate age from uploaded images.
- Supports images close to 200x200 pixels for accurate predictions.
- Web interface built with Flask for easy interaction.


## Installation

Install my-project

```bash
git clone https://github.com/your_username/image-gender-age-prediction.git
cd image-gender-age-prediction

```
    
## Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```


## Uses

- Upload an image using the provided form.
- Click "Upload" to submit the image for prediction.
- View the predicted gender and age on the result page.
## Project Structure

- app.py: Flask application setup and routes.
- model/: Directory containing the trained machine learning model (model.h5).
- static/: Static files including uploaded images and CSS styles.
- templates/: HTML templates (index.html and result.html) for user interface.
## Demo
Visit this link for demo, Working of website and model.
```
https://youtu.be/M3UYmkB8RLI
```
[![Watch the video](https://img.youtube.com/vi/M3UYmkB8RLI/maxresdefault.jpg)](https://www.youtube.com/watch?v=M3UYmkB8RLI)

## Model

![App Screenshot](model.png)
