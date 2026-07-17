# cyberdefense-agents
AI-agent-for-cyberdefense

**Steps for Downloading the Model**
---
You need a GGUF model file. Here's the easiest way:
1. Go to https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF
2. Download Meta-Llama-3-8B-Instruct-Q4_K_M.gguf (~5GB)
3. Place it in the models/ directory
4. Rename it to llama-3-8b-instruct.gguf (optional, for simplicity)

**Workflow for Prototype:**
- The program is passed some cyber environment object
- The observation builder then takes this environment object and parses it to build an observation or in other words update the state of the agent
- the agent then executes a discrete action within the action space based off of the state 
- The environment is then updated based off of this action
- a reward is calculated
- goes right back to the observation builder and the process repeats itself
