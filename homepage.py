import streamlit as st

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width:50%;
        }
    </style>
    """, unsafe_allow_html=True
)
# containers
# columns

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

secao_usuario = st.session_state
nome_usuario = None
if "username" in secao_usuario:
    nome_usuario = secao_usuario.name
    
coluna_esquerda, coluna_direita = st.columns([1, 1.5])

coluna_esquerda.title("Cotralti Corp.")
if nome_usuario:
    coluna_esquerda.write(f"#### Bem vindo, {nome_usuario}") # markdown
botao_dashboards = coluna_esquerda.button("Calculadora de Frete Tonelada")
botao_indicadores = coluna_esquerda.button("Calculadora de Frete Dedicado")

if botao_dashboards:
    st.switch_page("calculadorafrete.py")
if botao_indicadores:
    st.switch_page("fretededicado.py")

container = coluna_direita.container(border=True)
container.image("cotraltiimage.jpg")
st.write("""
         &copy; 2024 - Luis Felipe A. David. Todos os direitos reservados
         """)