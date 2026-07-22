from models.llm import LocalLLM
from src.utils.json_extraction import extract_json_from_text
from src.environment.state import State
from src.environment.cyber_environment import CyberEnvironment
from src.environment.observation_builder import build_observation
from src.actions.action_space import get_valid_actions, execute_action
from src.actions.action_types import ActionTypes


class Agent:

    def __init__(self, model_path: str):

        self.llm = LocalLLM(model_path)

        self.system_prompt = (
            "You are a defensive cyber agent that receives a structured observation of the current system state and must select exactly one valid defensive action."
            "Prioritize containing genuine threats quickly while minimizing unnecessary disruption, false positives, and repeated or invalid actions."
            "Base decisions only on the provided observation, never assume hidden ground truth, and return the chosen action."
        )

    def step(self, state: State) -> dict:
        prompt = f"""{self.system_prompt}

You are an agent. You must decide the next action and respond with ONLY valid JSON.

Current state: {state.to_string()}

Available actions: {[a.value for a in get_valid_actions(state)]}

CRITICAL INSTRUCTIONS:
1. Respond with ONLY valid JSON
2. No explanations, no markdown, no other text
3. Start your response with {{ and end with }}
4. If action is "close_port", you MUST include "port" set to one of the open_ports from the current state
5. For all other actions, omit "port" or set it to null

Required JSON format:
{{"action": "action_name", "port": null, "reason": "explanation"}}


Response (JSON only):"""
        
        for attempt in range(3):
            response = self.llm.generate(prompt, temperature=0.0)
            parsed = extract_json_from_text(response)
            
            if parsed and "action" in parsed:
                if "reason" not in parsed:
                    parsed["reason"] = f"Taking action: {parsed['action']}"
                if parsed['action'] not in [a.value for a in get_valid_actions(state)]:
                    continue
                if parsed['action'] == ActionTypes.CLOSE_PORT.value:
                    port = parsed.get("port")
                    if port not in state.open_ports:
                        continue
                return parsed
                
        return None

    def run_loop(self, environment: CyberEnvironment):

        results = []

        while environment.current_step < environment.max_steps:
            state = build_observation(environment)
            action = self.step(state)

            if not action:
                break

            execute_action(
                environment,
                get_valid_actions(state),
                ActionTypes(action["action"]),
                port=action.get("port"),
            )
            environment.current_step += 1
            results.append(action)

        return results
