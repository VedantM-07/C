def get_response(message):
    """
    Returns a response based on the user's input message.
    """
    # Normalize the message to lowercase.
    message = message.lower().strip()
    
    # Check for greetings.
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    
    # Check for pricing queries.
    elif "price" in message or "cost" in message:
        return "Our prices vary by product. Can you tell me which product you're interested in?"
    
    # Check for product inquiry.
    elif "product" in message or "detail" in message:
        return "We offer a wide variety of products. Could you specify which one you are interested in?"
    
    # Check for help request.
    elif "help" in message:
        return "Sure, I'd be happy to help! Please tell me more about what you need."
    
    # Check for farewell.
    elif "bye" in message or "exit" in message:
        return "Thank you for visiting. Have a great day!"
    
    # Default response if nothing else matches.
    else:
        return "I'm sorry, I didn't understand that. Could you please clarify?"

def chatbot():
    """
    Runs a simple command line based chatbot session.
    """
    print("Welcome to our Chatbot! (Type 'exit' or 'bye' to end the chat)")
    
    while True:
        # Read input from the user.
        user_input = input("You: ")
        
        # Check if the user wants to exit.
        if user_input.lower().strip() in ["exit", "bye"]:
            print("Chatbot: Thank you for visiting. Goodbye!")
            break
        
        # Get and print the chatbot's response.
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()




# ==============================================================

# Theory : 
"""

📌 Chatbot Fundamentals
Q1: What is a chatbot?
A: A chatbot is a computer program designed to simulate conversation with human users, especially over the internet. It can be rule-based or use AI/ML for natural conversation.

Q2: What is the purpose of the chatbot you developed?
A: This is a command-line chatbot that simulates basic customer service interactions. It handles greetings, pricing queries, product inquiries, help requests, and farewells.

Q3: Is this chatbot rule-based or AI-based?
A: This chatbot is rule-based. It responds to keywords in the user’s message using conditional (if-elif-else) logic.

🧾 Code-Level Questions
Q4: What does the get_response() function do?
A: It processes the user's message, converts it to lowercase, and checks for specific keywords to generate appropriate replies. If no match is found, it returns a default response.

Q5: Why do we use message.lower().strip()?
A: To normalize the message — converting it to lowercase removes case sensitivity, and .strip() removes leading/trailing whitespace for cleaner processing.

Q6: How does the chatbot know when to end the session?
A: The chatbot() function ends the loop when the user types "exit" or "bye".

Q7: What is the purpose of the if __name__ == "__main__": block?
A: It ensures the chatbot only runs when the file is executed directly, not when imported into another module.

Q8: What happens when the user says something unrecognized?
A: The chatbot replies with a default message: "I'm sorry, I didn't understand that. Could you please clarify?"

🗨️ Chatbot Logic and Functionalities
Q9: What are the types of messages the chatbot can respond to?
A:

Greetings (hello, hi)

Pricing or cost queries

Product details

Help requests

Exit/farewells

Q10: Can this chatbot handle multiple topics in one sentence?
A: No. It is simple and linear, matching keywords independently, not handling compound intents.

Q11: What would happen if the user types "Hi, what is the cost of the product?"?
A: The chatbot will return the greeting response first as hi is matched before cost.

🔁 Control Flow & Looping
Q12: How does the chatbot continue the conversation?
A: Using an infinite while True loop that only breaks when the user types "exit" or "bye".

Q13: Why is a loop used in the chatbot?
A: To keep the chatbot interactive and continuously accept user inputs until termination.

💻 Implementation & Platform
Q14: On what platform can this chatbot run?
A: It can run on any system with Python installed, through the command-line interface (terminal/console).

Q15: Can this be implemented as a web-based chatbot?
A: Yes, but it would need integration with a web server, UI, and possibly Flask or Django for Python-based web deployment.

🧰 Programming Concepts Involved
Q16: What programming concepts are demonstrated in this chatbot?
A:

String manipulation

Conditional branching (if-elif-else)

Functions

Looping (while)

Input/output handling

Basic error tolerance

Q17: Why is keyword-based matching not ideal for large-scale bots?
A: It's limited and not context-aware. For complex conversations, NLP or machine learning is better.

📈 Improvements and Scalability
Q18: How can this chatbot be improved?
A:

Add Natural Language Processing (NLP) for better understanding

Use a dictionary or intent-response mapping

Add memory/context tracking

Integrate with GUI or web interface

Q19: Can we use AI/ML in this chatbot?
A: Not currently. But by using frameworks like NLTK, spaCy, or GPT, we can add AI capabilities.

Q20: What if a user types something like "Tell me about your product and cost"?
A: The chatbot will only match the first keyword it encounters. Handling multiple intents requires more advanced parsing.

📚 Additional Questions
Q21: What is the difference between a chatbot and a virtual assistant?
A: A chatbot is typically task-focused (like customer service), while a virtual assistant (e.g., Alexa, Siri) is broader and more dynamic.

Q22: How is error handling done in this chatbot?
A: There's no explicit error handling; unrecognized inputs are handled by a default reply.

Q23: What is the role of the input() function?
A: It captures the user's message from the command line.

Q24: Can this chatbot be multilingual?
A: Not currently. For multilingual support, additional logic and possibly NLP models are needed.

Q25: How does the chatbot know which response to send?
A: By using if conditions to check for specific substrings in the user’s input.


Q1. How does this chatbot simulate intelligence without using AI or ML?
A: It uses rule-based logic to mimic intelligence by matching keywords in user input. It’s not truly intelligent but gives the illusion by using if-elif conditions that cover common user intents.

Q2. What are the limitations of hardcoding chatbot responses like in this code?
A:

Cannot scale easily for many queries

Difficult to maintain

No natural language understanding

Can't handle variations or slang

Responses are rigid and repetitive

Q3. Can this chatbot remember past conversations or context?
A: No. It is stateless, meaning it treats every message independently. Stateful bots store user context (e.g., name, preferences, past queries).

Q4. How could you refactor the chatbot to make it cleaner or more scalable?
A:

Use a dictionary mapping keywords to responses

Extract logic into intent-matching functions

Implement regular expressions for better pattern matching

Q5. What is an intent in chatbot design?
A: An intent is the purpose behind a user’s input, like asking for pricing or saying hello. Recognizing intent helps the bot choose the correct response.

Q6. How would you store chatbot conversations for analysis or training?
A: Save user and bot messages in a database or a log file, possibly with timestamps, user IDs, and intent tags.

Q7. What is the difference between keyword matching and pattern matching?
A:

Keyword Matching: Looks for exact words (e.g., "price")

Pattern Matching: Uses patterns (like regex) to match phrases, allowing more flexibility

Q8. Why is input() used instead of GUI components?
A: This is a command-line application. input() allows text interaction in the terminal, suitable for quick prototyping or non-GUI interfaces.

Q9. Can this chatbot run on platforms like Slack or Discord?
A: Not directly. It needs to be integrated via APIs or webhook listeners and wrapped in platform-specific bot code (e.g., using discord.py or Slack SDK).

Q10. What Python libraries can help build smarter chatbots?
A:

NLTK / spaCy: For natural language processing

ChatterBot: For training response models

Transformers (Hugging Face): For advanced AI models

Flask: For deploying chatbot APIs

Q11. What is the role of stripping and lowercasing user input?
A: To normalize text for better matching, since "Hi" and "hi " should be treated the same.

Q12. How would you test this chatbot?
A:

Try different input variations

Validate all if-elif conditions

Test exit conditions (bye, exit)

Test invalid/unknown input behavior

Q13. What is the time complexity of this chatbot response generation?
A: O(n), where n is the number of if-elif conditions. Each condition is checked sequentially until a match is found.

Q14. Why is it bad practice to use too many if-elif blocks?
A: It leads to spaghetti code, is hard to read, and difficult to modify when the bot grows. A better approach is using data structures or NLP libraries.

Q15. Can you add fallback suggestions if a user enters something vague?
A: Yes, we can modify the default message to provide hints, like:
"I'm not sure I understood. Try asking about pricing or saying hello!"

Q16. Is there any security concern with a chatbot?
A: Yes. Even a simple bot should handle input validation, avoid code injection (if later extended to databases or web apps), and not leak personal data.

Q17. How would you handle multi-language support?
A:

Detect language using libraries (e.g., langdetect)

Map keywords and responses in multiple languages

Use translation APIs if needed

Q18. Can this chatbot handle spelling errors?
A: Not in its current form. To handle that, we’d need fuzzy matching (e.g., using difflib.get_close_matches()).

Q19. What is modularity and how can you apply it here?
A: Modularity means separating code into reusable blocks. The bot can have separate functions for greeting, product info, cost, etc., making it cleaner and maintainable.

Q20. What is a state machine, and how is it used in chatbots?
A: A state machine is a design that tracks the state of a conversation. In complex bots, it helps navigate between stages like onboarding, product search, and support flow.

Q21. How would you deploy this chatbot for public use?
A:

Wrap it in a web framework like Flask

Create an API endpoint

Host it on a cloud platform (Heroku, Render, or AWS)

Connect it to a frontend or messaging platform


""" 



