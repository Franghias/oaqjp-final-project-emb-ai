import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    
    header = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting emotion's scores from the response
    # If the response status code is 200, extract the emotion scores from the response
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # Else, output none for all the emotion scores
    elif response.status_code == 400:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
           }
    else:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
           }
    
    dominant_emotion_score = 0
    if anger_score > dominant_emotion_score:
        dominant_emotion_score = anger_score
        dominant_emotion = 'anger'
    
    if disgust_score > dominant_emotion_score:
        dominant_emotion_score = disgust_score
        dominant_emotion = 'disgust'

    if fear_score > dominant_emotion_score:
        dominant_emotion_score = fear_score
        dominant_emotion = 'fear'

    if joy_score > dominant_emotion_score:
        dominant_emotion_score = joy_score
        dominant_emotion = 'joy'

    if sadness_score > dominant_emotion_score:
        dominant_emotion_score = sadness_score
        dominant_emotion = 'sadness'

    # Return the response text from the API
    return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
           }