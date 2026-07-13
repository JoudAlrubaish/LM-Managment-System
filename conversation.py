#Stage 18: Add a Conversation Class
class Conversation:
    """Manages a conversation creation and sending messages"""
    def __init__(self, conversation_id , model):
        #attributes
        self.conversation_id = conversation_id 
        self.model = model
        self.messages = [] #messages attribute should start as an empty list

    def send_message(self, prompt: str): #to store the user message
        self.messages.append({
            "role": "user",
            "content": prompt
        })

        response = self.model.generate_response(prompt)

        self.messages.append({
            "role": "assistant",
            "content": response
        })

        return response
    
    #method to display the full conversation history
    def display_history(self):
        for message in self.messages:
            print(message["role"], ":", message["content"])