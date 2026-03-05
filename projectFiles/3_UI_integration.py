import streamlit as st

# integration 
from connect_memory_with_llm import ask_question

def main():
    st.title('Ask Chatbot!!')
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])
    prompt = st.chat_input("Enter your Question: ")
    
    if prompt: 
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role':'user','content':prompt})
        
        response = ask_question(prompt)
        st.chat_message('assistant').markdown(response)
        st.session_state.messages.append({'role':'assistant','content':response})
    
if __name__ == "__main__":
    main()