## This repo contains a solution to the FoondaMate challenge.
# To use code locally
- First install using `pip`
  ```
  pip install git+https://github.com/dugerij/ML_challenge.git
  ```
  
- import the sentence_checker function from the package
  ```
  from ML_challenge.test_ml import sentence_checker
  ```
  
  
- Use the function as described below
  ```
  test_sentence = 'Can I give your contacts with my friend?'
  
  sentence_checker(sentence=test_sentence) 
  ```
  The function returns the appropriate label( i.e 'Students want to know if can share' or 'student has shared') for each sentence passed.

# About the function
The solution is a function i have termed sentence_checker. It takes the sentence being analysed as its only argument.

The code is written employing simple logic in python.
It checks for query words such as 'Can', 'Could', 'Will', 'Would', 'May' and 'Might' in the submitted sentence string to sort sentences into either category. The solution is able to accurately sort all the sentences provided in the challenge scenario.

# About the tests
I have employed pytest package, to write a test which checks if all the provided sentences are appropriately sorted.

# Ideas to improve function
While the above code works to accurately classify the examples provided in the challenge, a better approach would be to employ a text classification model, trained to analyse and classify sentences as statements or questions. The model would be trained to identify more unique sentence structures and accurately classify them as questions or statements.
Models like the oen described above are the rave in NLP, but require large datasets and compute power to train.
