from modules.ai_client import get_ai_response


def generate_alerts(language, service_type, service_length, cameras, volunteer_count, platforms):
    system_prompt = """
    You are an expert church production risk analyst.

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

    Analyze this church production setup and generate smart alerts.

    Service Type: {service_type}
    Service Length: {service_length} minutes
    Number of Cameras: {cameras}
    Volunteer Count: {volunteer_count}
    Platforms/Tools Used: {platforms}

    Identify:
    1. Staffing risks
    2. Timing risks
    3. Livestream risks
    4. Media risks
    5. Bilingual communication risks if relevant
    6. Suggested solutions
    """

    return get_ai_response(system_prompt, user_prompt)