# content of test.py
import pytest
import random 

random.seed(21)
# import the is_prime function
    
def sentence_checker(sentence):
    sentence = sentence.lower()
    print(sentence)

    share = ['share', 'give', 'sent',  'gave', 'send']
    email = ['email', 'contact', 'details', 'address', 'digits']
    query_markers = ['can', 'could', 'may', 'might', 'would', 'will']

    if any(word in sentence for word in share) and any(word in sentence for word in email):
        if any(query in sentence for query in query_markers):
            label = 'Students want to know if can share'

        else:
            label = 'student has shared'
            
    else:
        label = ('Sentence does not contain keywords email and shared.')

    return label


def test_sentence():
        """
        test function to test for first group "student has shared"
        """
        test_sharedlist = [
        'I shared your email',
        'I just shared your address',
        "I've sent your email address to my friend",
        "I've shared your email",
        'I already shared email',
        "I've just shared your address",
        'Okay I have shared the email',
        'I have shared your email',
        'I did share your email',
        'I shared your contacts',
        'I shared your digits',
        'I shared your contact details',
        'I shared your contact card',
        'I shared the email with my friends',
        'I have sent this email to my friends',
        'The email has been shared with all my friends',
        ]
        a = random.randint(0, len(test_sharedlist))
        data = test_sharedlist[a]
        result = sentence_checker(data)
        assert result == 'student has shared'

def test_query():
        """
        test function to test for second group "Students want to know if can share"
        """
        test_querylist= [
        'Can I share your email address',
        'May I share your email',
        'Might I share your email',
        'Could we share your email address with my friends',
        'Can I share your email with my friend',
        'Can I send your email to my friend',
        'Can I give your contacts with my friend?',
        ]
        b = random.randint(0, len(test_querylist))
        data = test_querylist[b]
        result = sentence_checker(data)
        assert result == 'Students want to know if can share'