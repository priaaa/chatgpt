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
    st.title("GPT-3 Conversation Chatbot")

    st.sidebar.subheader("Chatbot")

    # Initialize an empty list of messages
    messages = []
    i = 1

    while True:
        user_input = st.sidebar.text_input("User Input "+ str(i))
        i = i + 1
        if st.sidebar.button("Send"+ str(i)):
            # Append user message to the message list
            messages.append({"role": "user", "content": user_input})

            if user_input.lower() == 'exit':
                st.sidebar.warning("Chat ended. Refresh the page to start again.")
                break

            # Get chatbot response
            response = chat_with_gpt3(messages)
           
            # Append chatbot response to the message list
            messages.append({"role": "chatbot", "content": response})


            
        # Display the chat history
        for message in messages:
            role = message["role"]
            content = message["content"]

            if role == "user":
                st.text_input("User"+ str(message), value=content, disabled=True)
            elif role == "chatbot":
                st.text_area("Chatbot"+ str(message), value=content, disabled=True)
                
                
if __name__ == "__main__":
    main()
