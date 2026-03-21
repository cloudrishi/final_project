import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f"\n{'Statement':<45} {'Dominant Emotion'}")
        print("-" * 62)

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        print(f"\n{'I am glad this happened':<45} {result['dominant_emotion']}")
        self.assertEqual(result['dominant_emotion'], 'joy')
        print("-" * 62)
    
    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        print(f"\n{'I am really mad about this':<45} {result['dominant_emotion']}")
        self.assertEqual(result['dominant_emotion'], 'anger')
        print("-" * 62)
    
    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        print(f"\n{'I feel disgusted just hearing about this':<45} {result['dominant_emotion']}")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        print("-" * 62)

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        print(f"\n{'I am so sad about this':<45} {result['dominant_emotion']}")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        print("-" * 62)

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        print(f"\n{'I am really afraid that this will happen':<45} {result['dominant_emotion']}")
        self.assertEqual(result['dominant_emotion'], 'fear')
        print("-" * 62)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)