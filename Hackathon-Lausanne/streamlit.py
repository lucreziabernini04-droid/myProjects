import streamlit as st
from rag_apertus import answer_query_with_history  # importa la tua funzione RAG

# --- Configurazione pagina ---
st.set_page_config(page_title="Chatbot Civico Vaud", layout="wide")

# CSS personalizzato per scroll e bolle
st.markdown("""
<style>
.chat-container {
    max-height: 70vh;
    overflow-y: auto;
    padding: 10px;
    border: 1px solid #eee;
    border-radius: 10px;
    background-color: #f7f7f7;
}
.user-bubble {
    background-color: #DCF8C6;  /* verde chiaro per l'utente */
    padding: 10px;
    border-radius: 15px;
    margin: 5px 0;
    text-align: right;
}
.bot-bubble {
    background-color: #FF6B6B;  /* rosso per l'AI */
    color: white;
    padding: 10px;
    border-radius: 15px;
    margin: 5px 0;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

st.title("Chatbot Civico Vaud 🌟")

# --- Memorizza la cronologia ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Chat principale ---
chat_placeholder = st.empty()  # placeholder per chat scrollabile

# Mostra cronologia
def render_chat():
    with chat_placeholder.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for chat in st.session_state.history:
            st.markdown(f'<div class="user-bubble">👤 Tu: {chat["user"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="bot-bubble">🤖 Amico Civico: {chat["bot"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

render_chat()

# --- Input sempre in basso ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Scrivi la tua domanda qui...")
    submit_button = st.form_submit_button("Invia")

    if submit_button and user_input:
        try:
            risposta = answer_query_with_history(user_input)
        except Exception as e:
            risposta = f"Errore nella generazione della risposta: {str(e)}"
        
        st.session_state.history.append({"user": user_input, "bot": risposta})
        render_chat()
