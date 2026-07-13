# Stage 13: class PricingPlan creation which show the pricing plan for a language models
class PricingPlan:
    """stores pricing information"""
    def __init__(
        self,
        plan_name,
        price_per_1000_tokens
    ) -> None: #type hint means the function doesnot return anything 
        self.plan_name = plan_name
        self.price_per_1000_tokens = price_per_1000_tokens

# method should receive the number of tokens and calculate the cost.
    def calculate_cost(self, tokens: int) -> float:#type hint 
        """Calculate the cost based on token """
        return tokens / 1000 * self.price_per_1000_tokens