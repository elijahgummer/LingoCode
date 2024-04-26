import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLPInterface:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_input(self, input_text):
        # Tokenize input text
        tokens = word_tokenize(input_text.lower())

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]

        # Lemmatization
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]

        return lemmatized_tokens

    def generate_code(self, input_text):
        # Placeholder for code generation logic
        # For now, just echo back the input
        return input_text

# Instantiate NLPInterface
nlp_interface = NLPInterface()

# Main loop
while True:
    # Get input from the user
    user_input = input("Enter a coding task: ")

    # Preprocess input
    preprocessed_input = nlp_interface.preprocess_input(user_input)

    # Generate code
    generated_code = nlp_interface.generate_code(preprocessed_input)

    # Display generated code
    print("Generated code:")
    print(generated_code)
    print()
