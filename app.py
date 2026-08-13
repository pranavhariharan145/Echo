import streamlit as st
from main import agent

st.set_page_config(
    page_title="Echo",
    page_icon="🤖",
    layout="centered",
)

# Combined CSS for User Bubbles & Chat Input Styling
st.markdown("""
<style>

/* --- 1. USER CHAT MESSAGE --- */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageAvatarUser"] {
    display: none !important;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    flex-direction: row-reverse !important;
    width: fit-content !important;
    margin-left: auto !important;
    margin-right: 0 !important;
    border-radius: 25px !important;
    padding: 12px 20px !important;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    flex-grow: 0 !important;
    width: fit-content !important;
    text-align: right !important;
}

/* --- 2. CHAT INPUT & BUTTON --- */
/* Chatinput box */
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div {
    border-radius: 50px !important;
}

/* TEXT SIZE IN CHAT INPUT */
[data-testid="stChatInput"] textarea {
    font-size: 1.1rem 
}

/* Blue submit button */
[data-testid="stChatInput"] button {
    border-radius: 50% !important;
    border: none !important;

}

[data-testid="stChatInput"] button:hover {
    background-color: #FF8164 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
        <h1 style="text-align: center;">🤖 EchoAI</h1>
        <h3 style="text-align: center;">Your Daily AI assistant</h3>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get new user input
user_input = st.chat_input("Ask Echo something...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Echo is thinking..."):
            response = agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            })

            answer = response["messages"][-1].content
            st.write(answer)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })