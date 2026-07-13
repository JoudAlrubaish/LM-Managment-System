#Stage 19: Add a ModelManager Class : to manage a collection of language models
class ModelManager:
    """Manages language models"""
    def __init__(self):
        """Create empty model manager"""
        self.models = {} 

    def add_model(self, model):
        self.models[model.model_name] = model

    def remove_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]

    def get_model(self, model_name):
        return self.models.get(model_name)

    def list_models(self):
        for model_name in self.models:
            print(model_name)

#Stage 20: Select the Best Model --> based on: 1)The provider name , 2) The model's max_tokens value , 3) The model must be active
    def select_model(self, provider, required_tokens):
        for model in self.models.values():
            if (
                model.provider == provider
                and model.max_tokens >= required_tokens
                and model.is_active
            ):
                return model

        return None