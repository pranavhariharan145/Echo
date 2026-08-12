import streamlit as st
from main import agent
st.set_page_config(
    page_title="Echo",
    page_icon="🤖",
    layout="centered",
)

st.markdown(
    """
    <h1 style="text-align: center;">🤖 Echo</h1>
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