from modules.ai_client import get_ai_response


def generate_service_plan(language, sermon_title, sermon_theme, speaker_name, service_type, service_length, special_elements):
    system_prompt = f"""
    You are an expert church production planning assistant.

    STRICT LANGUAGE RULES:
    - If language = English, respond ONLY in English.
    - If language = Spanish, respond ONLY in Spanish.
    - If language = Bilingual (English + Spanish), respond in BOTH languages using these exact headers:
      English Section
      Spanish Section
    - Do not mix languages unless Bilingual (English + Spanish) is selected.

    Keep the response structured, clear, practical, and professional for a real church production team.
    """

    user_prompt = f"""
    Selected language: {language}

    Build a full church service plan with the following details:

    Sermon Title: {sermon_title}
    Sermon Theme: {sermon_theme}
    Speaker Name: {speaker_name}
    Service Type: {service_type}
    Service Length: {service_length} minutes
    Special Elements: {special_elements}

    Include:
    1. Order of service
    2. Estimated timing for each segment
    3. Worship/song theme suggestions
    4. Scripture suggestions
    5. Transition notes
    6. Stage/media notes
    """

    return get_ai_response(system_prompt, user_prompt)