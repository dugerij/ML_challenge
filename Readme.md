## This repo contains a solution to the FoondaMate challenge.
# About the function
The solution is a function i have termed sentence_checker. It takes the sentence being analysed as its only argument.

The code is written employing simple logic in python.
It checks for query words such as 'Can', 'Could', 'Will', 'Would', 'May' and 'Might' in the submitted sentence string to sort sentences into either category. The solution is able to accurately sort all the sentences provided in the challenge scenario.

# About the tests
I have employed pytest package, to write two tests which check if all the provided sentences are appropriately sorted.

However to run the test_ml.py:

-  pip install -U pytest
-  pytest
