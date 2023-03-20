import re
from typing import Optional


def clean_text(text: str) -> str:
    """Clean input text by removing non-alphabetic characters and converting to lowercase."""
    sub: str = re.sub(r'[^a-z]+', ' ', text.lower())
    return sub


def match_input(input_text: str, patterns_responses: dict[str, str]) -> Optional[str]:
    """Match user input with stored patterns and return the best matching response."""
    cleaned_input = clean_text(input_text)
    best_match: Optional[str] = None
    best_match_score: int = 0

    for pattern, response in patterns_responses.items():
        score = sum(1 for word in cleaned_input.split() if word in pattern.split())

        if score > best_match_score:
            best_match_score = score
            best_match = response

    return best_match


def update_patterns_responses(input_text: str, response: str, patterns_responses: dict[str, str]) -> None:
    """Update patterns and responses based on user input."""
    cleaned_input = clean_text(input_text)
    patterns_responses[cleaned_input] = response


def chatbot() -> None:
    """Initiate the chatbot."""
    patterns_responses: dict[str, str] = {'hello': 'hi there!'}

    print("Hello! I'm a learning chatbot. Please teach me by typing a message and the response I should give.")
    print("To test my learning, just type your message and I will respond based on what I've learned.")
    print("Type 'exit' to quit the chat.")

    while True:
        user_input: str = input("User: ")

        if user_input.lower() == 'exit':
            break

        if '||' in user_input:
            input_text, response = user_input.split('||', 1)
            update_patterns_responses(input_text.strip(), response.strip(), patterns_responses)
            print("Chatbot: I've learned a new response.")
        else:
            chatbot_response = match_input(user_input, patterns_responses)
            if chatbot_response:
                print(f"Chatbot: {chatbot_response}")
            else:
                print("Chatbot: I don't know how to respond to that yet. Please teach me.")


if __name__ == '__main__':
    chatbot()
