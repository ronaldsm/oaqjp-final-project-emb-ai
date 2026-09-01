import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}



