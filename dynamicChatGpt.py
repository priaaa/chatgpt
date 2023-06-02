import streamlit as st
import openai
from streamlit_chat import message

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
    chatWithUser(1)
        
    
def chatWithUser(title):
    user_input = st.sidebar.text_input("Question" + str(title))
    if st.sidebar.button("Send Ans"+ str(title)):
        response = chat_with_gpt3(user_input)
        st.text_area("Chatbot Response" + str(title), value=response)
        title = title + 1
        chatWithUser(title)
            
if __name__ == "__main__":
     main()
            
        

        

    
