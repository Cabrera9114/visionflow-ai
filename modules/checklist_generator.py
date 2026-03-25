from modules.ai_client import get_ai_response


def generate_checklist(language, service_type, platforms, cameras):
    system_prompt = """
    You are an expert church production checklist assistant.

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

    Create a production checklist for this service:

    Service Type: {service_type}
    Platforms/Tools Used: {platforms}
    Number of Cameras: {cameras}

    Include:
    1. Pre-service checklist
    2. Media checklist
    3. Livestream checklist
    4. Camera checklist
    5. Post-service shutdown checklist
    """

    return get_ai_response(system_prompt, user_prompt)