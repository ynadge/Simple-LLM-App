import streamlit as st
from huggingface_hub import InferenceClient

def response_generator(prompt):

		client = InferenceClient(api_key=" ")

		messages = [
			{
				"role": "user",
				"content": prompt
			}
		]

		response = "".join(message.choices[0].delta.content for message in client.chat_completion(
						model="microsoft/Phi-3.5-mini-instruct",
      stream = True,
			messages=messages, 
			max_tokens=500
		))

		return response


st.title('TSimple LLM App')  # App title
# We want the history of prompts entered by user, so we create a session state message variable to hold all of them.
# Streamlit apps are inherently stateful, which means that whenever a user interacts with the app, the entire app is rerun.
# session_state helps maintain some states throughout all the reruns (caused by prompts being entered in this case).
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])
# Display a chat input widget. It will be pinned to the bottom of the page.
prompt = st.chat_input('Enter your prompt here')
if prompt:  # If the user enters a prompt
    st.chat_message('user').markdown(prompt)  # Insert a chat message container.
    # Store the prompt in the session state.
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    # Prompting the LLM
    response = response_generator(prompt)
    # Displaying the response
    st.chat_message('assistant').markdown(response)
    # Store response in session_state just like the prompts.
    st.session_state.messages.append({'role': 'assistant', 'content': response})


# ### Links and Resources:
# - https://docs.streamlit.io/develop/api-reference/chat/st.chat_input
# - https://docs.streamlit.io/develop/api-reference/chat/st.chat_message
# - https://youtu.be/XctooiH0moI?si=A_7WRQf8rMEcJbE7
# - https://youtu.be/w_ZPIHgSPDI?si=pcjdWD9zji8EpXfe

# In[ ]:




