def chatbot_response(user_input):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm doing great, thanks!",
        "bye": "Goodbye!",
    }
    user_input = user_input.lower().strip()
    return responses.get(user_input, "I don't understand that.")

if __name__ == "__main__":
    print("Chatbot is ready! Type 'quit' to exit.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower().strip() == "quit":
                print("Bot: Goodbye!")
                break
            print("Bot:", chatbot_response(user_input))
        except Exception as e:
            print("An error occurred:", str(e))
