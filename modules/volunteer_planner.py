import pandas as pd
from modules.ai_client import get_ai_response


def load_team_members():
    try:
        return pd.read_csv("data/team_members.csv")
    except Exception:
        return pd.DataFrame()


def generate_volunteer_plan(language, roles_needed, availability):
    team_df = load_team_members()

    if team_df.empty:
        if language == "Spanish":
            return "No se encontraron datos de voluntarios."
        elif language == "Bilingual (English + Spanish)":
            return "English Section\nNo volunteer data found.\n\nSpanish Section\nNo se encontraron datos de voluntarios."
        return "No volunteer data found."

    team_data = team_df.to_string(index=False)

    system_prompt = """
    You are an expert volunteer coordinator for church production teams.

    STRICT LANGUAGE RULES:
    - If language = English, respond ONLY in English.
    - If language = Spanish, respond ONLY in Spanish.
    - If language = Bilingual (English + Spanish), respond in BOTH languages using these exact headers:
      English Section
      Spanish Section
    - Do not mix languages unless Bilingual (English + Spanish) is selected.

    Keep the response structured, clear, practical, and professional.
    """

    user_prompt = f"""
    Selected language: {language}

    Here is the current volunteer data:

    {team_data}

    Roles Needed: {roles_needed}
    Availability Needed: {availability}

    Create:
    1. Suggested assignments
    2. Coverage gaps
    3. Backup suggestions
    4. Notes for bilingual support if helpful
    """

    return get_ai_response(system_prompt, user_prompt)