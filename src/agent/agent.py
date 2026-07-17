from models.llm import LocalLLM
from src.utils.json_extraction import extract_json_from_text

class Agent:

    def __init__(self, model_path: str):

        self.llm = LocalLLM(model_path)

        self.system_prompt = (
            "You are a callm and helpful AI assistant."
            "You explain concepts simply and avoid unnecessary jargon"
            "You are honest about what you know and don't know"
        )

    
    def simple_generate(self, user_input: str) -> str:

        return self.llm.generate(user_input)
    
    def generate_structured(self, user_input: str, schema: str) -> dict | None:
        
        prompt = f"""{self.system_prompt}

CRITICAL INSTRUCTIONS:
1. Respond with ONLY valid JSON
2. No explanations, no markdown, no extra text before or after the JSON
3. Start your response with {{ and end with }}

Schema you must follow:
{schema}

User request: {user_input}

Response (JSON only):"""
        
        for attempt in range(3):
            response = self.llm.generate(prompt, temperature=0.0)
            parsed = extract_json_from_text(response)
            
            if parsed is not None:
                return parsed
        
        return None

