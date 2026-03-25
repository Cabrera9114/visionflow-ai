import streamlit as st
from modules.service_builder import generate_service_plan
from modules.run_sheet import generate_run_sheet
from modules.volunteer_planner import generate_volunteer_plan
from modules.checklist_generator import generate_checklist
from modules.alerts import generate_alerts


def download_text(content, filename="output.txt"):
    st.download_button(
        label="Download Output",
        data=content,
        file_name=filename,
        mime="text/plain"
    )


st.set_page_config(page_title="VisionFlow AI Pro", layout="wide")

with st.sidebar:
    st.title("VisionFlow AI")

    st.markdown("""
    ### Features
    - Service Builder
    - Run Sheet Generator
    - Volunteer Planner
    - Production Checklist
    - AI Alerts

    ### Built With
    - Python
    - Streamlit
    - OpenAI API

    ### Purpose
    Helping church production teams plan smarter and faster.
    """)

st.title("🎛️ VisionFlow AI Pro")
st.subheader("AI Smart Church Production Assistant")
st.markdown("---")
st.info("This AI assistant helps plan and manage church production workflows in real time.")

language = st.selectbox(
    "Choose output language",
    ["English", "Spanish", "Bilingual (English + Spanish)"]
)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Service Builder",
    "Run Sheet Generator",
    "Volunteer Planner",
    "Production Checklist",
    "AI Alerts"
])

with tab1:
    st.header("Service Builder")

    sermon_title = st.text_input("Sermon Title")
    sermon_theme = st.text_input("Sermon Theme")
    speaker_name = st.text_input("Speaker Name")
    service_type = st.selectbox(
        "Service Type",
        ["Sunday Worship", "Youth Service", "Prayer Night", "Conference", "Special Event", "Online-Only Service"]
    )
    service_length = st.number_input("Service Length in Minutes", min_value=30, max_value=300, value=90)
    special_elements = st.text_area("Special Elements")

    col1, col2 = st.columns(2)

    with col1:
        generate_service = st.button("Generate Service Plan")

    with col2:
        clear_service = st.button("Clear Inputs")

    if clear_service:
        st.rerun()

    if generate_service:
        with st.spinner("Generating service plan..."):
            result = generate_service_plan(
                language,
                sermon_title,
                sermon_theme,
                speaker_name,
                service_type,
                service_length,
                special_elements
            )
        st.markdown("### 📄 Output")
        st.markdown("---")
        st.markdown(result)
        download_text(result, "service_plan.txt")

with tab2:
    st.header("Run Sheet Generator")

    rs_service_type = st.selectbox(
        "Service Type",
        ["Sunday Worship", "Youth Service", "Prayer Night", "Conference", "Special Event", "Online-Only Service"],
        key="rs_service_type"
    )
    cameras = st.number_input("Number of Cameras", min_value=1, max_value=10, value=3)
    platforms = st.text_input("Platforms or Tools Used", value="OBS, ProPresenter, ATEM")
    rs_sermon_title = st.text_input("Sermon Title", key="rs_sermon_title")
    rs_special_elements = st.text_area("Special Elements", key="rs_special_elements")

    if st.button("Generate Run Sheet"):
        with st.spinner("Generating run sheet..."):
            result = generate_run_sheet(
                language,
                rs_service_type,
                cameras,
                platforms,
                rs_sermon_title,
                rs_special_elements
            )
        st.markdown("### 📄 Output")
        st.markdown("---")
        st.markdown(result)
        download_text(result, "run_sheet.txt")

with tab3:
    st.header("Volunteer Planner")

    roles_needed = st.text_area(
        "Roles Needed",
        value="Producer, Camera Operator, Lyrics Operator, Livestream Operator, Host"
    )
    availability = st.text_input("Availability Needed", value="Sunday AM")

    if st.button("Generate Volunteer Plan"):
        with st.spinner("Generating volunteer plan..."):
            result = generate_volunteer_plan(language, roles_needed, availability)
        st.markdown("### 📄 Output")
        st.markdown("---")
        st.markdown(result)
        download_text(result, "volunteer_plan.txt")

with tab4:
    st.header("Production Checklist")

    cl_service_type = st.selectbox(
        "Service Type",
        ["Sunday Worship", "Youth Service", "Prayer Night", "Conference", "Special Event", "Online-Only Service"],
        key="cl_service_type"
    )
    cl_platforms = st.text_input(
        "Platforms or Tools Used",
        value="OBS, ProPresenter, ATEM",
        key="cl_platforms"
    )
    cl_cameras = st.number_input(
        "Number of Cameras",
        min_value=1,
        max_value=10,
        value=3,
        key="cl_cameras"
    )

    if st.button("Generate Checklist"):
        with st.spinner("Generating checklist..."):
            result = generate_checklist(language, cl_service_type, cl_platforms, cl_cameras)
        st.markdown("### 📄 Output")
        st.markdown("---")
        st.markdown(result)
        download_text(result, "checklist.txt")

with tab5:
    st.header("AI Alerts")

    al_service_type = st.selectbox(
        "Service Type",
        ["Sunday Worship", "Youth Service", "Prayer Night", "Conference", "Special Event", "Online-Only Service"],
        key="al_service_type"
    )
    al_service_length = st.number_input(
        "Service Length in Minutes",
        min_value=30,
        max_value=300,
        value=90,
        key="al_service_length"
    )
    al_cameras = st.number_input(
        "Number of Cameras",
        min_value=1,
        max_value=10,
        value=3,
        key="al_cameras"
    )
    volunteer_count = st.number_input("Volunteer Count", min_value=1, max_value=50, value=5)
    al_platforms = st.text_input(
        "Platforms or Tools Used",
        value="OBS, ProPresenter, ATEM",
        key="al_platforms"
    )

    if st.button("Generate Alerts"):
        with st.spinner("Generating alerts..."):
            result = generate_alerts(
                language,
                al_service_type,
                al_service_length,
                al_cameras,
                volunteer_count,
                al_platforms
            )
        st.markdown("### 📄 Output")
        st.markdown("---")
        st.markdown(result)
        download_text(result, "alerts.txt")

st.markdown("---")
st.markdown("Built by Eduardo Cabrera-Lopez | VisionFlow AI Pro")