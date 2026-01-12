# chatbot_rule_based.py
import re
import random
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.name = "CodeBot"
        self.responses = {
            "greeting": [
                "Hello! How can I assist you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I help you?"
            ],
            "farewell": [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! Feel free to come back if you have more questions."
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "My pleasure!"
            ],
            "name": [
                f"I'm {self.name}, your AI assistant!",
                f"You can call me {self.name}.",
                f"I'm {self.name}, here to help you."
            ],
            "help": [
                "I can help with: greetings, time/date, basic math, weather info, and general chat.",
                "Try asking me about time, date, or say hello!"
            ],
            "weather": [
                "I can't access real-time weather, but you can check weather.com!",
                "For accurate weather, please check a weather service online."
            ],
            "time": [],
            "date": [],
            "math": [],
            "default": [
                "I'm not sure I understand. Can you rephrase?",
                "Could you explain that differently?",
                "I'm still learning. Could you ask something else?"
            ]
        }
    
    def get_time(self):
        now = datetime.now()
        return now.strftime("The current time is %I:%M %p")
    
    def get_date(self):
        now = datetime.now()
        return now.strftime("Today's date is %B %d, %Y")
    
    def calculate_math(self, expression):
        try:
            # Remove non-math characters for safety
            expr = re.sub(r'[^0-9\+\-\*/\(\)\.\s]', '', expression)
            result = eval(expr)
            return f"The result is: {result}"
        except:
            return "Sorry, I couldn't calculate that. Please use format like '2+2' or '10*5'."
    
    def process_input(self, user_input):
        user_input = user_input.lower().strip()
        
        # Greeting patterns
        if re.search(r'hello|hi|hey|greetings', user_input):
            return random.choice(self.responses["greeting"])
        
        # Farewell patterns
        elif re.search(r'bye|goodbye|see you|farewell', user_input):
            return random.choice(self.responses["farewell"])
        
        # Thanks patterns
        elif re.search(r'thanks|thank you|appreciate', user_input):
            return random.choice(self.responses["thanks"])
        
        # Name patterns
        elif re.search(r'who are you|what is your name|your name', user_input):
            return random.choice(self.responses["name"])
        
        # Help patterns
        elif re.search(r'help|what can you do|abilities', user_input):
            return random.choice(self.responses["help"])
        
        # Weather patterns
        elif re.search(r'weather|temperature|rain|sunny', user_input):
            return random.choice(self.responses["weather"])
        
        # Time patterns
        elif re.search(r'time|what time|current time', user_input):
            return self.get_time()
        
        # Date patterns
        elif re.search(r'date|today\'?s? date|what day', user_input):
            return self.get_date()
        
        # Math patterns
        elif re.search(r'calculate|compute|what is \d+|math', user_input):
            # Extract numbers and operators
            if re.search(r'\d+[\+\-\*/]\d+', user_input):
                match = re.search(r'(\d+[\+\-\*/]+\d+)', user_input)
                return self.calculate_math(match.group(1))
            return "Please provide a math expression like '2+2' or '10*5'"
        
        # Default response
        else:
            return random.choice(self.responses["default"])
    
    def chat(self):
        print(f"{self.name}: {random.choice(self.responses['greeting'])}")
        print("Type 'quit', 'exit', or 'bye' to end the chat.\n")
        
        while True:
            try:
                user_input = input("You: ")
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"{self.name}: {random.choice(self.responses['farewell'])}")
                    break
                
                response = self.process_input(user_input)
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye!")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.chat()