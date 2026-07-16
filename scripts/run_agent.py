from agent.agent import Agent

agent = Agent("models/llama-3-8b-instruct.gguf")

schema = """{
  "topic": string,
  "difficulty": "beginner" | "intermediate" | "advanced"
}"""

print(agent.generate_structured("Explain Markov Decision Process", schema))

schema = """{
    "question": string,
    "answer" : string
}"""

print(agent.generate_structured("Explain Markov Decision Process", schema))

 