# Stage 11: class Tokenizer creation to class Tokenizer: Counts words in a prompt as tokens
class Tokenizer:
    """Counts words as tokens"""
    def count_tokens(self, text: str) -> int: #type hint means the function return int 
        return len(text.split())
    
