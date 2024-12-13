import os
import traceback

import openai
from dotenv import load_dotenv
from openai import AsyncOpenAI


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
        self.client = AsyncOpenAI(api_key=api_key)

    async def request(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generate a response from the OpenAI API.

        Args:
            system_prompt (str): The system prompt for context.
            user_prompt (str): The user prompt for input.

        Returns:
            str: The API-generated response.
        """
        try:
            completion = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {
                        "role": "user",
                        "content": user_prompt
                    }

                ],
                response_format={"type": "json_object"},
                temperature=0.0,
            )
            return completion.choices[0].message.content
        except openai.OpenAIError:
            return f"OpenAI API error: {traceback.format_exc()}"
        except Exception:
            return f"An unexpected error occurred: {traceback.format_exc()}"
