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

        # Remove stopwords and punctuation
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

        # Lemmatization
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]

        return lemmatized_tokens

    def generate_code(self, input_tokens):
        code = ""

        # Convert natural language input to code
        if "create" in input_tokens and "function" in input_tokens:
            # Check for function name and parameters
            func_idx = input_tokens.index("function")
            func_name = input_tokens[func_idx - 1]
            parameters = input_tokens[func_idx + 1:]

            # Generate function definition
            code += f"def {func_name}({', '.join(parameters)}):\n"
            code += "\t# Write your code here\n"
            code += "\tpass\n"

        elif "define" in input_tokens and "variable" in input_tokens:
            # Check for variable name and value
            var_idx = input_tokens.index("variable")
            var_name = input_tokens[var_idx - 1]
            value = input_tokens[var_idx + 1]

            # Generate variable definition
            code += f"{var_name} = {value}\n"

        else:
            code = "Error: Invalid input"

        return code

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
    print("\nGenerated code:")
    print(generated_code)
    print()
