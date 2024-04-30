import nltk
import random

# NLTK setup
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Define some sample rules (you can expand these)
rules = {
    'print': {
        'patterns': [
            'print the value of <variable>',
            'output the value of <variable>',
            'display <variable>',
        ],
        'responses': [
            'print(<variable>)',
            'print("{}: {}".format("<variable>", <variable>))',
        ]
    },
    'loop': {
        'patterns': [
            'repeat <n> times:',
            'loop <n> times:',
        ],
        'responses': [
            'for i in range(<n>):',
            '\t# Do something <n> times',
        ]
    },
    # Add more rules as needed
}

# Function to match pattern
def match_pattern(pattern, sentence):
    words = word_tokenize(sentence)
    tags = pos_tag(words)
    pattern_words = pattern.split()
    pattern_tags = pos_tag(pattern_words)

    if len(words) != len(pattern_words):
        return False

    for i in range(len(words)):
        if pattern_words[i] == '<variable>':
            continue
        if pattern_words[i] != words[i] or pattern_tags[i][1] != tags[i][1]:
            return False
    return True

# Function to generate code
def generate_code(sentence):
    for intent, data in rules.items():
        for pattern in data['patterns']:
            if match_pattern(pattern, sentence):
                response = random.choice(data['responses'])
                if '<variable>' in response:
                    variable = input("Enter the value for <variable>: ")
                    response = response.replace('<variable>', variable)
                return response
    return "I'm sorry, I don't understand."

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    code = generate_code(user_input.lower())
    print("AI: ", code)
