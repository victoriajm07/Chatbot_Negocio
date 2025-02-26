import streamlit as st
from app import predict_class, get_response, intents

st.title ("Asistente virtual")

if "messages" not in st.session_state:
    st.session_state.messages = [] # Array vacío que almacenará el historico del chat
if "first_message" not in st.session_state:
    st.session_state.first_message = True # Comprueba si es el primer mensaje del chat

# Mostrar el histórico del chat
for message in st.session_state.messages: # Recorre el array de mensajes
    with st.chat_message(message["role"]):  
        st.markdown(message["content"]) # Pinta los mensajes

# Establece el primer mensaje del chat
if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, Bienvenido a Llama3. ¿En qué puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant", "content": "Hola, Bienvenido a Llama3. ¿En qué puedo ayudarte?"})
    st.session_state.first_message = False

# Estable que si el usuario inserta algo en el chat, el asistente responda
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Implementación del algoritmo IA
    insts = predict_class(prompt)
    res = get_response(insts, intents)

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": res})