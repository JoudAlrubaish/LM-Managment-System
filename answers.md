# Project Questions

# 1. What is the difference between a class and an object?

A class is a template or blueprint while the object ia a copy or instance created from this class.

# 2. Why did we use LanguageModel as an abstract class?

To create a common template for all models classes and make every child class to implement its version of generate_response() method.

# 3. What is the purpose of super()?

We use super() to call super/parent class's constructor. 

# 4. What is the difference between inheritance and composition?

Inheritance means a child class innherit attributes and methods from parent class.

Composition means a class combines objects from another class.

# 5. What is the difference between composition and aggregation?

In composition we create the object inside the class, while in aggregation we create the object outside and then passed to the class.

# 6. Where does polymorphism appear in the project?

Appears in GPTModel  and LlamaModel, they use the same generate_response() method but return different responses.

# 7. What is the difference between a class attribute and an instance attribute?

A class attribute created in the class and shared by all instances, while instance attribute belongs to one object/instance only.

# 8. Why did we use @property?

To control how private attributes could be accesed. 

# 9. When should we use a static method?

When the method does not need class data.

# 10. When should we use a class method?

When the method needs class data.

# 11. Why did we override generate_response()?

Because each model generates a different response.

# 12. What is the purpose of __str__ and __repr__?

__str__ gives a simple description.

__repr__ gives a technical description.

# 13. Why did we create a custom exception?

To handle invalid prompts entered by showing a clear error message.

# 14. What problem does ModelManager solve?

It stores, removes, finds, lists, and selects models.

# 15. How could this project be connected to a real API later?

By replacing the simulated response with a real API request using an API key.