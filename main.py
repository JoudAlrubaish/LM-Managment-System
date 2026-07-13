#Joud Alrubaish  -  Building a Language Model Management System using OOP

# this file contains testing for the system , from each file we will import the class created 
from pricing import PricingPlan
from models import LanguageModel, GPTModel, LlamaModel
from manager import ModelManager
from conversation import Conversation
from exceptions import InvalidPromptError

# testing pricing plan
pricing = PricingPlan("Standard", 0.02)


# testing GPT model
gpt = GPTModel(
    model_name="GPT-Model",
    provider="OpenAI",
    max_tokens=4096,
    temperature=0.7,
    api_key="secret-key",
    pricing_plan=pricing #Stage 14: Apply Aggregation
)


# testing Llama model
llama = LlamaModel(
    model_name="Llama-Model",
    provider="Local",
    max_tokens=8192,
    temperature=0.5,
    model_path="/models/llama",
    quantization="4-bit",
    pricing_plan=pricing #Stage 14: Apply Aggregation
)


# testing display information
gpt.display_info()
print()

llama.display_info()
print()


# Stage 9: Apply Polymorphism
models = [gpt, llama]

for model in models:
    print(model.generate_response("Explain OOP"))
    print()


# testing model manager
manager = ModelManager()

manager.add_model(gpt)
manager.add_model(llama)

print("Available models:")
manager.list_models()
print()


# Selecting a model
selected_model = manager.select_model("OpenAI", 3000)

if selected_model:
    print("Selected model:", selected_model.model_name)
else:
    print("No suitable model found.")

print()


# testing encapsulation
gpt.temperature = 1.2
print("New temperature:", gpt.temperature)

try:
    gpt.temperature = 4
except ValueError as error:
    print(error)

print()


# testing custom exception
try:
    gpt.generate_response("")
except InvalidPromptError as error:
    print(error)

print()


# testing conversation
conversation = Conversation(1, gpt)

conversation.send_message("Explain object-oriented programming")

print("Conversation history:")
conversation.display_history()
print()


# testing calculate cost 
gpt.calculate_request_cost("Explain object-oriented programming")
print()


# testing magic methods
print(gpt)
print(repr(gpt))
print("Maximum tokens:", len(gpt))
print("Are GPT and Llama equal?", gpt == llama)
print()


# testing class method and static method
print("Total models:", LanguageModel.get_total_models())
print("Valid temperature:", LanguageModel.validate_temperature(0.7))