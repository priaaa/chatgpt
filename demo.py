import streamlit as st
import openai
st.title("Chatting with ChatGPT")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )

def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    i = 0
    while True:
        i = i + 1
        user_query = st.text_input("Question"+ str(i))
        if user_query != ":q" or user_query != "":
            # Pass the query to the ChatGPT function
            response = ChatGPT(user_query)
            st.write(f"{user_query} {response}")
    
def ChatGPT(user_query):
    openai.api_key = "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"
  
    completion = openai.Completion.create (
        model="text-davinci-003",
        prompt=user_query,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"])
        
    response = completion.choices[0].text
    return response

main()



