import streamlit as st
from parse_usbstor import parse_usbstor
from parse_amcache import parse_amcache
from parse_mft import parse_mft

import requests

def parse_usb(raw_text):
    # Replace this with your actual USB parsing logic
    return {
        "Device Name": "Disk&Ven_Kingston&Prod_DataTraveler&Rev_1.00",
        "Serial Number": "00112233445566778899",
        "Last Time Connected": "2024-03-12 09:15:00"
    }


def get_agent_explanation(parsed_json):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {st.secrets['azure_api_key']}"
    }

    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful digital forensics explainer agent."},
            {"role": "user", "content": f"Explain this artifact:\n{parsed_json}"}
        ]
    }

    try:
        response = requests.post(
            st.secrets["azure_endpoint"],
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error contacting Azure agent: {e}"


# Page setup
st.set_page_config(page_title="Digital Forensics Explainer", layout="centered")

# Sample inputs
sample_inputs = {
    "USBSTOR": (
        "Device Name: Disk&Ven_Kingston&Prod_DataTraveler&Rev_1.00\n"
        "Serial Number: 00112233445566778899\n"
        "First Connected: 2024-03-10 09:15:00"
    ),
    "AmCache": (
        "File Path: C:\\Program Files\\CCleaner\\CCleaner.exe\n"
        "SHA1: A1B2C3D4E5F67890ABCDEF1234567890ABCDEF12\n"
        "First Execution Time: 2023-09-15 08:22:00\n"
        "Publisher: Piriform Ltd"
    ),
    "$MFT": (
        "File Name: report.docx\n"
        "File Path: C:\\Users\\Warren\\Documents\\report.docx\n"
        "Created: 2023-08-01 10:15:00\n"
        "Modified: 2023-08-02 14:30:00\n"
        "Accessed: 2023-08-02 14:30:00\n"
        "File Size: 24576\n"
        "Deleted: False"
    )
}

# App title
st.title("🔍 Digital Forensics Explainer")
st.markdown("Use the tabs below to select an artifact type. Paste raw text or load a sample to parse and explain.")

# Tabs for each artifact type
tab1, tab2, tab3 = st.tabs(["USBSTOR", "AmCache", "$MFT"])

with tab1:
    st.header("USB Artifact")

    # Load sample input
    if st.button("Load Sample Input", key="usb_btn"):
        st.session_state.usb_input = sample_inputs["USBSTOR"]

    # Raw input box
    usb_input = st.text_area(
        "Raw artifact text:",
        value=st.session_state.get("usb_input", ""),
        height=200,
        key="usb_input"
    )

    # Parse button
    if st.button("Parse Artifact", key="usb_parse"):
        st.session_state.usb_parsed = parse_usb(usb_input)

    # Show parsed JSON if available
    if "usb_parsed" in st.session_state:
        st.subheader("🧾 Parsed JSON")
        st.code(st.session_state.usb_parsed, language="json")

        # Agent explanation button with spinner
        if st.button("Explain with Azure Agent", key="explain_usb"):
            with st.spinner("🕒 Contacting Azure Agent... Please wait."):
                explanation = get_agent_explanation(st.session_state.usb_parsed)
            st.session_state.usb_explanation = explanation

        # Show explanation if available
        if "usb_explanation" in st.session_state:
            if st.session_state.usb_explanation:
                st.subheader("🧠 Agent Explanation")
                st.write(st.session_state.usb_explanation)
            else:
                st.warning("⚠️ No explanation returned. Please check your input or try again.")

        # Prompt copy box
        st.subheader("🧠 Explanation Prompt")
        st.text_area(
            "Copy this into your Azure agent:",
            value=st.session_state.usb_parsed,
            height=200
        )
        st.success("✅ Tip: Click inside the box and press Ctrl+C to copy.")

with tab2:
    st.header("AmCache Artifact")

    # Load sample input
    if st.button("Load Sample Input", key="amcache_btn"):
        st.session_state.amcache_input = sample_inputs["AmCache"]

    # Raw input box
    amcache_input = st.text_area(
        "Raw artifact text:",
        value=st.session_state.get("amcache_input", ""),
        height=200,
        key="amcache_input"
    )

    # Parse button
    if st.button("Parse Artifact", key="amcache_parse"):
        st.session_state.amcache_parsed = parse_amcache(amcache_input)

    # Show parsed JSON if available
    if "amcache_parsed" in st.session_state:
        st.subheader("🧾 Parsed JSON")
        st.code(st.session_state.amcache_parsed, language="json")

        # Agent explanation button with spinner
        if st.button("Explain with Azure Agent", key="explain_amcache"):
            with st.spinner("🕒 Contacting Azure Agent... Please wait."):
                explanation = get_agent_explanation(st.session_state.amcache_parsed)
            st.session_state.amcache_explanation = explanation

        # Show explanation if available
        if "amcache_explanation" in st.session_state:
            if st.session_state.amcache_explanation:
                st.subheader("🧠 Agent Explanation")
                st.write(st.session_state.amcache_explanation)
            else:
                st.warning("⚠️ No explanation returned. Please check your input or try again.")

        # Prompt copy box
        st.subheader("🧠 Explanation Prompt")
        st.text_area(
            "Copy this into your Azure agent:",
            value=st.session_state.amcache_parsed,
            height=200
        )
        st.success("✅ Tip: Click inside the box and press Ctrl+C to copy.")

with tab3:
    st.header("$MFT Artifact")

    # Load sample input
    if st.button("Load Sample Input", key="mft_btn"):
        st.session_state.mft_input = sample_inputs["$MFT"]

    # Raw input box
    mft_input = st.text_area(
        "Raw artifact text:",
        value=st.session_state.get("mft_input", ""),
        height=200,
        key="mft_input"
    )

    # Parse button
    if st.button("Parse Artifact", key="mft_parse"):
        st.session_state.mft_parsed = parse_mft(mft_input)

    # Show parsed JSON if available
    if "mft_parsed" in st.session_state:
        st.subheader("🧾 Parsed JSON")
        st.code(st.session_state.mft_parsed, language="json")

        # Agent explanation button with spinner
        if st.button("Explain with Azure Agent", key="explain_mft"):
            with st.spinner("🕒 Contacting Azure Agent... Please wait."):
                explanation = get_agent_explanation(st.session_state.mft_parsed)

            # Store explanation in session state for reuse
            st.session_state.mft_explanation = explanation

        # Show explanation if available
        if "mft_explanation" in st.session_state:
            if st.session_state.mft_explanation:
                st.subheader("🧠 Agent Explanation")
                st.write(st.session_state.mft_explanation)
            else:
                st.warning("⚠️ No explanation returned. Please check your input or try again.")

        # Prompt copy box
        st.subheader("🧠 Explanation Prompt")
        st.text_area(
            "Copy this into your Azure agent:",
            value=st.session_state.mft_parsed,
            height=200
        )
        st.success("✅ Tip: Click inside the box and press Ctrl+C to copy.")

# Footer
st.markdown("---")
st.caption("Built by Warren Judson • Modular AI Forensics Agent • Rocklin, CA")