from src.agent.agent import Agent
agent = Agent("models/llama-3-8b-instruct.gguf")



def structured_output():
  schema = """{
    "topic": string,
    "difficulty": "beginner" | "intermediate" | "advanced"
  }"""

  print(agent.generate_structured("Explain Markov Decision Process", schema))

def answer_question():
  schema = """{
      "question": string,
      "answer" : string
  }"""

  print(agent.generate_structured("Explain Markov Decision Process", schema))

structured_output()
answer_question()



 