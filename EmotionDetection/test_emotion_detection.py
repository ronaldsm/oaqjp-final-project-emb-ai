import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
    def test_sadness(self):
        result_2 = emotion_detector('I am so sad about this')
        self.assertEqual(result_2['dominant_emotion'], 'sadness')
        
if __name__ == '__main__':
    unittest.main()
