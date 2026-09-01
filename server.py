''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer_route():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the dominant emotion and score from the response
    dominant_emotion = response['dominant_emotion']
    score = response['score']
    # Return a formatted string with the dominant emotion and score
    
    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the dominant emotion and score
        return "The given text has been identified as {} with a score of {}.".format(dominant_emotion, score)

@app.route("/")
def render_index_page():
  return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
