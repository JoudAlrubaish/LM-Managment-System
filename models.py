
#this .py contains 4 classes: LanguageModel class , LoggingMixin class , GPTModel class, LlamaModel class

#import 
from abc import ABC, abstractmethod # Stage 10: Apply Abstraction --> makes LanguageModel abstract 
from tokenizer import Tokenizer
from exceptions import InvalidPromptError

#Stage 1 : Create the Base Class
class LanguageModel(ABC):
    """Base class for language models"""
    total_models = 0
#constructor runs everytime a new model object created
    def __init__(
        self,
        model_name: str,
        provider: str,
        max_tokens: int,
        temperature: float,
        pricing_plan
    ):
        """Create a language model"""
        self.model_name = model_name
        self.provider = provider
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.pricing_plan = pricing_plan
        self.tokenizer = Tokenizer() #Stage 12: Apply Composition --> tokenizer for eeach language model 
        self.__is_active = True

        LanguageModel.total_models += 1 #Stage 3 : Use Class Attributes --> increased every time a new LanguageModel object is created
     
    @property #Stage 6: Apply Encapsulation --> getter using python opreator to get private temp value
    def temperature(self):
        return self.__temperature

    @temperature.setter #setter for temp value and checks before save it 
    def temperature(self, value):
        if 0 <= value <= 2:
            self.__temperature = value
        else:
            raise ValueError("Temperature must be between 0 and 2.")

    @property #tell whether the model is active or not 
    def is_active(self):
        return self.__is_active

    @is_active.setter 
    def is_active(self, value):
        self.__is_active = value

    @classmethod #Stage 4: Use a Class Method get_total_models()
    def get_total_models(cls):
        return cls.total_models

    @staticmethod #Stage 5: Use a Static Method validate_temperature()
    def validate_temperature(value):
        return 0 <= value <= 2 #receive a temp value and verify if it is between these two numbers 

    @abstractmethod #Stage 2 : generate_response --> abstract method  so every child class will create its own version
    def generate_response(self, prompt):
        pass

    def display_info(self): #method to display  model information

        print("Model Name:", self.model_name)
        print("Provider:", self.provider)
        print("Maximum Tokens:", self.max_tokens)
        print("Temperature:", self.temperature)

    def calculate_request_cost(self, prompt): #Sends the token count to the pricing plan then Calculates the cost
        tokens = self.tokenizer.count_tokens(prompt)
        cost = self.pricing_plan.calculate_cost(tokens)

        print("Cost:", cost)
        return cost
#Stage 15: Apply Magic Methods
    def __str__(self): #print the object
        return f"{self.model_name} by {self.provider}"

    def __repr__(self): #technical representation of the object
        return f"{self.__class__.__name__}('{self.model_name}', '{self.provider}')"

    def __len__(self): # max token for the model 
        return self.max_tokens

    def __eq__(self, other): #comparing two objects (T or F) 
        return (
            self.model_name == other.model_name
            and self.provider == other.provider
        )
    
    def check_prompt(self, prompt):
        if not isinstance(prompt, str) or prompt.strip() == "":
            raise InvalidPromptError("Prompt cannot be empty.")
        
#Stage 16: Apply Multiple Inheritance
#provide logging 
class LoggingMixin:
    def log(self, message):
        print("[LOG]", message)


#Stage 7: Apply Inheritance --> by creation of  GPTModel class as child of (LanguageModel) class
class GPTModel(LanguageModel, LoggingMixin):
    """class for GPT model"""
    def __init__(
        self,
        model_name,
        provider,
        max_tokens,
        temperature,
        api_key,
        pricing_plan
    ):
        super().__init__(
            model_name,
            provider,
            max_tokens,
            temperature,
            pricing_plan
        )

        self.api_key = api_key #child class attribute

#Stage 8: Apply Method Overriding for (generate_response()) inside each child class 
    def generate_response(self, prompt):
        self.check_prompt(prompt)
        self.log(f"Sending request to {self.model_name}")
        tokens = self.tokenizer.count_tokens(prompt) #Inside generate_response(), use the tokenizer to count the number of tokens in the prompt
        return f"GPT API response to: {prompt}\nInput tokens: {tokens}"

#Stage 7: Apply Inheritance --> by creation of  LlamaModel class as child of (LanguageModel) class
class LlamaModel(LanguageModel):
    """class for Llama model"""
    def __init__(
        self,
        model_name,
        provider,
        max_tokens,
        temperature,
        model_path,
        quantization,
        pricing_plan
    ):
        super().__init__(
            model_name,
            provider,
            max_tokens,
            temperature,
            pricing_plan
        )
        #child class attributes 
        self.model_path = model_path 
        self.quantization = quantization
  
  #Stage 8: Apply Method Overriding for (generate_response()) inside each child class 
    def generate_response(self, prompt):
        self.check_prompt(prompt)
        tokens = self.tokenizer.count_tokens(prompt)#Inside generate_response(), use the tokenizer to count the number of tokens in the prompt
        return f"Local Llama response to: {prompt}\nInput tokens: {tokens}"

