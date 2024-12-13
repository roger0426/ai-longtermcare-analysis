import os
import traceback

import openai
from dotenv import load_dotenv
from openai import OpenAI


class OpenAIClient:
    def __init__(self, model="gpt-4o"):
        """
        OpenAIClient for interacting with the OpenAI API.

        Args:
            model (str): The model to use (default: "gpt-4o").
        """
        self.model = model
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found. Please set it in the .env file.")
        self.client = OpenAI(api_key=api_key)

    def request(self, system_prompt, user_prompt, json_mode=True):
        """
        Generate a response from the OpenAI API.

        Args:
            system_prompt (str): The system prompt for context.
            user_prompt (str): The user prompt for input.

        Returns:
            str: The API-generated response.
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": user_prompt
                    }

                ],
                response_format={"type": "json_object"} if json_mode else None,
                temperature=0.0,
            )
            return completion.choices[0].message.content
        except openai.OpenAIError:
            return f"OpenAI API error: {traceback.format_exc()}"
        except Exception:
            return f"An unexpected error occurred: {traceback.format_exc()}"
