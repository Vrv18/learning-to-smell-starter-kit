"""
Import implementations you want to play around with here
"""
from random_predict import RandomPredictor
from fingerprint_predict import FingerprintPredictor

"""
The implementation you want to submit as your submission
"""
# submission = FingerprintPredictor() # This is a class derived from the L2SPredictor class from evaluator.learning_to_smell
submission = RandomPredictor() # This is a class derived from the L2SPredictor class from evaluator.learning_to_smell
print("Generating prediction using %s" % submission.__class__.__name__)

submission.run()
print("Successfully generated prediction file at %s" % submission.predictions_output_path)
