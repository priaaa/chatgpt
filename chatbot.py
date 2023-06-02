import streamlit as st
import openai
openai.api_key = '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'
def chat_with_gpt3(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    st.title("GPT-3 Chatbot")

    st.sidebar.subheader("Chatbot")

    user_input = st.sidebar.text_input("User Input")
    if st.sidebar.button("Send"):
        response = chat_with_gpt3(user_input)
        st.text_area("Chatbot Response", value=response)

if __name__ == "__main__":
    main()


