from modules.ai_client import get_ai_response


def generate_run_sheet(language, service_type, cameras, platforms, sermon_title, special_elements):
    system_prompt = f"""
    You are an expert church media director and production coordinator.

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

    Build a detailed production run sheet for this service:

    Service Type: {service_type}
    Number of Cameras: {cameras}
    Platforms/Tools Used: {platforms}
    Sermon Title: {sermon_title}
    Special Elements: {special_elements}

    Include:
    1. Time
    2. Segment
    3. Speaker/Lead
    4. Slides/Media
    5. Camera Direction
    6. Audio Notes
    7. Livestream Notes
    """

    return get_ai_response(system_prompt, user_prompt)