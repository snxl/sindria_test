import ast
from os import environ
from typing import List, Tuple

from openai import OpenAI

from src.clients.gpt.gpt import GPTClient


class OpenaiGPT4TurboClient(GPTClient):
    def send_question_to_evaluation(self, text: str) -> Tuple[List[str], List[str]]:
        client = OpenAI(
            api_key=environ.get('OPENAI_API_KEY')
        )

        system_message = """
            To maintain a consistent response format, provide two arrays, 'requisites' and 'concepts, 
            in the following JSON format:
            {
                "requisites": ["requisite1"], 
                "concepts": ["concept1"]
            }
            Make sure to write all the requisites and concepts in Portuguese of Brazil.
        """

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            # response_format={"type": "json_object"}, #issue on openai for some versions
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ]
        )

        response_content = response.choices[0].message.content
        response_content = response_content.replace('```json', '').replace('```', '').strip()

        answer = ast.literal_eval(response_content)

        requisites = answer.get('requisites', [])
        concepts = answer.get('concepts', [])

        return requisites, concepts
