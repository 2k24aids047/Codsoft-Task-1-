 TASK 1: Rule-Based Chatbot

 Project Description

This project is a **rule-based chatbot** created using Python.
The chatbot replies to user messages by checking predefined rules using **if-else conditions and pattern matching**.

It can handle simple conversations like greetings, asking the time or date, basic math calculations, and common questions.

Features

* Greets the user
* Responds to thank-you messages
* Tells its name
* Shows current **time and date**
* Solves **basic math expressions**
* Gives a default reply for unknown inputs
* Ends the chat when the user types *bye*, *exit*, or *quit*

 Technologies Used

* Language: **Python**
* Libraries:

  * `re` (for pattern matching)
  * `random` (for random responses)
  * `datetime` (for time and date)

How It Works

1. The user enters a message.
2. The chatbot converts the input to lowercase.
3. It checks the message against predefined patterns.
4. If a rule matches, it gives the correct response.
5. If no rule matches, it gives a default reply.
6. The chat continues until the user exits.

 How to Run the Program
 
1. Install Python on your system.
2. Download or clone the repository.
3. Open the Task 1 folder.
4. Run the program using:

   ```
   python chatbot_rule_based.py
   ```
5. Start chatting with the bot in the terminal.

 Example Interaction
User: Hello
Bot: Hi there! What can I do for you?

User: What is the time?
Bot: The current time is 10:30 AM

User: Calculate 5+3
Bot: The result is: 8

User: Bye
Bot: Goodbye! Have a great day!

 Project Structure
Task1/
 ├── chatbot_rule_based.py
 └── README.md

 What I Learned
* Basics of chatbot development
* Using if-else logic for conversations
* Pattern matching using regular expressions
* Handling user input and output
* Simple error handling in Python
