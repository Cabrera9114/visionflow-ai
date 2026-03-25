import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_ai_response(system_prompt, user_prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Missing OPENAI_API_KEY. Please add it to your .env file."

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"