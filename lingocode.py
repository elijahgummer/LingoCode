def generate_python_code(input_text):
    # Dictionary to map human language to Python code
    language_to_code = {
        "print": "print(",
        "input": "input()",
        "variable": "variable_name =",
        "if": "if condition:",
        "else if": "elif condition:",
        "else": "else:",
        "for loop": "for item in iterable:",
        "while loop": "while condition:",
        "function": "def function_name():",
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/",
        "modulo": "%",
        "greater than": ">",
        "less than": "<",
        "equal to": "==",
        "not equal to": "!="
    }

    # Split the input text into words
    words = input_text.split()

    # Iterate through words to build the code
    generated_code = ""
    i = 0
    while i < len(words):
        word = words[i].lower()

        if word in language_to_code:
            generated_code += language_to_code[word]

            if word == "print":
                generated_code += "\""
                i += 1
                while i < len(words):
                    if words[i].lower() in language_to_code:
                        break
                    generated_code += words[i] + " "
                    i += 1
                generated_code = generated_code.rstrip()  # Remove trailing whitespace
                generated_code += "\""
            elif word == "input":
                # Do nothing, as input() doesn't require additional parameters
                pass
            else:
                # Check if the next word is a variable name or condition
                if i + 1 < len(words):
                    next_word = words[i + 1].lower()
                    if next_word in language_to_code:
                        generated_code += " "
                    else:
                        generated_code += " " + words[i + 1] + " "
                        i += 1

            generated_code += ") "
        else:
            generated_code += word + " "
        i += 1

    return generated_code.strip()

def main():
    print("Welcome to Python Code Generator!")
    print("Enter 'exit' to quit.")

    while True:
        human_input = input("Enter a sentence describing what you want to generate code for: ")
        if human_input.lower() == 'exit':
            print("Exiting...")
            break
        
        generated_code = generate_python_code(human_input)
        print("Generated Python code:", generated_code)

if __name__ == "__main__":
    main()
