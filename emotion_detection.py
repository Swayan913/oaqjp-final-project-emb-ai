import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input text is blank
    if not text_to_analyze.strip():  # strip() removes leading/trailing spaces
        # Return a dictionary with None for all emotions if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # If text is not blank, proceed with the API call
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    # Convert response text to a dictionary
    response_dict = json.loads(response.text)

    # Extract emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Prepare final output
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result
