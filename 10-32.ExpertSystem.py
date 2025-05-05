def diagnose():
    """
    A simple expert system for medical diagnosis using rule-based reasoning.
    The system asks the user about specific symptoms, then recommends a
    preliminary possible diagnosis based on a few rules.
    
    This system is for educational purposes only.
    """
    print("Welcome to the Medical Diagnosis Expert System (for educational purposes only).")
    print("Please answer the following questions with 'yes' or 'no'.\n")
    
    fever = input("Do you have a fever? (yes/no): ").strip().lower()
    cough = input("Do you have a cough? (yes/no): ").strip().lower()
    sore_throat = input("Do you have a sore throat? (yes/no): ").strip().lower()
    runny_nose = input("Do you have a runny nose? (yes/no): ").strip().lower()
    body_ache = input("Do you have body aches? (yes/no): ").strip().lower()
    
    # Basic rules to determine possible diagnoses
    if fever == "yes" and cough == "yes" and sore_throat == "yes":
        diagnosis = "You might have a respiratory infection such as the flu or COVID-19. Please consult a healthcare provider."
    elif fever == "yes" and body_ache == "yes" and cough == "yes":
        diagnosis = "Your symptoms may indicate the flu. Consider seeing a doctor."
    elif fever == "yes" and cough == "yes":
        diagnosis = "There might be an infection such as bronchitis or pneumonia. It is advised to seek medical advice."
    elif runny_nose == "yes" and sore_throat == "yes":
        diagnosis = "These symptoms suggest you might have a common cold or allergies."
    elif runny_nose == "yes":
        diagnosis = "You might be experiencing mild allergies or a common cold."
    else:
        diagnosis = "Symptoms are not very specific. If you feel unwell, please consult a healthcare professional for further evaluation."
    
    print("\nPreliminary Diagnosis:")
    print(diagnosis)

if __name__ == "__main__":
    diagnose()



# ====================================================================
# Theory : 


"""
📌 Section 1: General Concepts of Expert Systems
Q: What is an expert system?
A: An expert system is a computer program that simulates the decision-making ability of a human expert. It uses a knowledge base and inference rules to provide recommendations or decisions.

Q: What type of expert system is implemented here?
A: It is a rule-based expert system for medical diagnosis, using if-else conditions to simulate reasoning based on symptoms.

Q: What is the purpose of the system you implemented?
A: It helps users self-evaluate common symptoms like fever, cough, and sore throat and gives a preliminary diagnosis for educational purposes.

Q: What are the main components of your expert system?
A:

Knowledge Base: Encoded as if-else conditions with medical knowledge.

Inference Engine: Uses rules to infer a diagnosis based on user input.

User Interface: CLI (Command Line Interface) using input() and print().

📌 Section 2: Code Understanding and Flow
Q: Explain the flow of your program.
A: The function diagnose():

Welcomes the user.

Asks 5 symptom-based yes/no questions.

Applies a sequence of if-else rules to match symptoms.

Outputs a possible diagnosis.

Q: How is user input taken in your program?
A: Using the built-in input() function, with .strip().lower() to handle formatting.

Q: Why did you use .strip().lower() with input?
A: To clean the input and ensure case-insensitive comparisons like 'Yes', ' YES ' become 'yes'.

Q: How does the system infer a diagnosis?
A: Through forward chaining, where it checks known inputs (symptoms) against rules to reach a conclusion.

Q: Why is this called a rule-based system?
A: Because the logic relies on hard-coded IF-THEN rules, simulating expert reasoning.

Q: What would happen if the user typed something other than "yes" or "no"?
A: The program may not handle unexpected inputs gracefully; input validation could be added.

📌 Section 3: Concepts & Terminology
Q: What is the knowledge base in your code?
A: The set of IF-ELSE conditions representing medical knowledge about symptoms and possible illnesses.

Q: What is the inference engine?
A: The mechanism (in this case, conditional logic) that applies rules to facts (user symptoms) to infer a diagnosis.

Q: What is forward chaining and is it used here?
A: Yes. Forward chaining means starting from known facts (symptoms) and moving forward to conclusions (diagnosis).

Q: Can this expert system learn new rules or update itself?
A: No. It is static; a knowledge engineer must manually update the rules.

Q: What kind of inference mechanism would be used in a more advanced system?
A: A production rule system, backward chaining, or a machine learning model.

📌 Section 4: Practical Applications and Limitations
Q: What are practical applications of such expert systems?
A: Healthcare diagnostics, troubleshooting systems, legal advice systems, customer service bots, etc.

Q: What are the limitations of your current implementation?
A: No GUI, limited rules, no confidence factor, no error handling for invalid input, not dynamic or scalable.

Q: How can your expert system be improved?
A:

Add GUI using Tkinter or web interface.

Expand the knowledge base.

Include severity scoring or confidence levels.

Add natural language input understanding.

📌 Section 5: System Design and Ethics
Q: Why did you include the disclaimer in the code?
A: Because it’s for educational use only and not a substitute for medical advice; such systems must not mislead users.

Q: Is your expert system deterministic or probabilistic?
A: Deterministic. It produces fixed outcomes based on predefined rules without probabilities.

Q: Can this be turned into a web application? How?
A: Yes, using frameworks like Flask or Django to create a backend that accepts input and returns diagnosis.

Q: What is the significance of using functions like diagnose()?
A: It makes the code modular, reusable, and easier to understand and maintain.

📌 Section 6: Extensions and Related Technologies
Q: How does this relate to AI?
A: This is a classic example of symbolic AI, where logic and rules are used instead of learning from data.

Q: Can machine learning replace expert systems?
A: ML can complement expert systems for pattern discovery, but expert systems are still used for explainability and control.

Q: How is this system different from a chatbot?
A: A chatbot focuses on conversational flow. This system makes decisions based on logic. But both can be combined.

Q: What platform did you use to run this code?
A: It can run on any Python environment (like IDLE, VS Code, Jupyter Notebook, or CLI).

Q: What language and version did you use?
A: Python 3.x (assumed), using only built-in functions and no external libraries.



🧠 1. What makes a system an "Expert System"?
A: An expert system simulates human decision-making by using a predefined knowledge base and an inference engine. It mimics how a domain expert would solve problems by reasoning through facts and rules.

🧠 2. How is this expert system different from a regular program?
A: Unlike regular programs that just execute instructions, an expert system:

Encapsulates expert knowledge.

Uses reasoning (inference rules).

Acts like a consultant that gives recommendations based on logic.

🔧 3. Explain the architecture of an expert system.
A:

User Interface – Accepts input (e.g., symptoms).

Knowledge Base – Contains facts and rules.

Inference Engine – Applies logic to match inputs with rules.

Explanation System – (optional) Tells user why a decision was made.

Knowledge Acquisition Module – (optional) For updating knowledge.

🧪 4. What are the reasoning methods in AI expert systems?
A:

Forward Chaining: From known facts to conclusions (used here).

Backward Chaining: From goal to facts (used in diagnostic/proof systems).

Hybrid: Combination of both.

🔍 5. How does forward chaining work in your code?
A: It takes known user responses (yes/no) and starts checking from top rules to bottom. As soon as conditions match a diagnosis, the system outputs the result.

🧩 6. What is pattern matching in expert systems?
A: It's the process where the system compares user input (facts) to the conditions defined in rules to see if a match (pattern) exists for making a decision.

⚙️ 7. Is your expert system rule-based or case-based?
A: It is rule-based. It does not rely on historical cases but on a predefined set of conditions and rules.

🧾 8. How can you scale or extend this expert system?
A:

Add more symptoms and diseases.

Introduce severity levels.

Store rules in an external file or database.

Add confidence scores or probabilistic inference.

🔠 9. Why did you use string comparison (yes, no) for symptoms?
A: It simplifies rule matching. In more advanced systems, input parsing or natural language processing (NLP) could be used.

💾 10. Can this expert system be used for real medical purposes?
A: No. It’s an educational tool. Real-world medical systems require:

Certified medical knowledge.

Continuous updates.

Legal approvals.

Secure and private data handling.

💡 11. What ethical issues are involved in such systems?
A:

Accuracy: Misdiagnosis can be harmful.

Bias: Incomplete rules may discriminate.

Privacy: User data must be protected.

Transparency: Users must know it's not a real doctor.

🖥️ 12. Can you describe how you would build a GUI for this expert system?
A: Using Tkinter (Python GUI library), you could:

Replace input() with form fields.

Add buttons for "Yes"/"No".

Show results in a textbox or popup.

🧠 13. How is your system an example of symbolic AI?
A: Symbolic AI uses explicit knowledge representations (symbols, logic). This system encodes knowledge as rules (IF-THEN), not learned from data like neural networks.

📖 14. Could you implement a learning-based version of this system?
A: Yes, using machine learning. It would:

Train on symptom-disease datasets.

Predict diagnosis using classification models (e.g., Decision Tree, SVM).

📊 15. What are production rules? How are they used in your system?
A: A production rule is an IF-THEN statement.
In this system:

python
Copy
Edit
if fever == "yes" and cough == "yes": diagnosis = "flu"
This is a production rule that triggers an action when its condition is satisfied.

🧪 16. What is a rule conflict, and how do you resolve it?
A: A rule conflict occurs when multiple rules match. In this system, the order of if-elif-else ensures only the first matching rule applies, resolving the conflict by priority.

📍 17. Why is modularity (use of diagnose() function) important here?
A: It:

Makes the code reusable and clean.

Enables testing and expansion (e.g., you can import and use it in GUI or web apps).

Separates logic from execution.

🔁 18. What if you want the system to allow multiple diagnoses?
A: You'd have to:

Store all matching rules in a list.

Evaluate all applicable rules, not just the first.

Return a list of possible diagnoses.

🧾 19. How would a real expert system handle ambiguous answers?
A:

Use confidence scores.

Ask follow-up questions.

Apply probabilistic reasoning (Bayesian inference).

🌐 20. Where are expert systems used today?
A: Examples include:

MYCIN – early medical expert system.

DENDRAL – chemistry compound prediction.

Help desks – automated troubleshooting.

Financial systems – risk analysis.
"""