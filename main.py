import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario
from conversor_moedas import main

  
st.set_page_config(
    page_title="Cotralti T&L",
    page_icon="cotralti_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

lista_usuarios = session.query(Usuario).all() # traz todas as informações do banco de dados

credenciais = {"usernames": {
    usuario.email: {"name": usuario.nome, "password": usuario.senha} for usuario in lista_usuarios
}}

authenticator = stauth.Authenticate(credenciais, "credenciais_hashco", "fsyfus%$6dddss7", cookie_expiry_days=30)

def autenticar_usuario(authenticator):
   resultado_login = authenticator.login()

   if resultado_login is not None:
        nome, status_autenticacao, username = resultado_login
        
        if status_autenticacao:
            return {"nome": nome, "username": username}
        elif status_autenticacao == False:
            st.error("Combinação de usuário e senha inválidas")
        else:
            st.error("Preencha o formulário para fazer login")
   else:
        st.error('Erro no processo de login, tente novamente.')
        return None

def logout():
    authenticator.logout()

# autenticar o usuario
dados_usuario = autenticar_usuario(authenticator)

if dados_usuario:
    
    email_usuario = dados_usuario["username"]
    usuario = session.query(Usuario).filter_by(email = email_usuario).first()
    
    if usuario.admin:
        pg = st.navigation(
        
                    {
                        
                    "𝗛𝗼𝗺𝗲":[st.Page("homepage.py", title="★ Cotralti Corporation")],
                    "𝗖𝗼𝗻𝘀𝘂𝗹𝘁𝗮𝘀 𝗻𝗮 𝗧𝗮𝗯𝗲𝗹𝗮 𝗦𝗽𝗶𝗰𝗲": [st.Page("calculadorafrete.py", title="① Cálculo de Frete Tonelada"),
                                st.Page("fretededicado.py", title="② Rota Dedicada"),
                                st.Page("consultarotas.py", title="③ Consulta por Rotas"),
                                st.Page("rateiofrete.py", title="④ Rateio de Frete por peso")],
                    "𝐔𝐭𝐢𝐥𝐢𝐭𝐚́𝐫𝐢𝐨𝐬":[st.Page("separadorpdf.py", title="📝Separador Arquivos PDF"),
                                 st.Page("juntarpdf.py", title="📝Juntar Arquivos PDF"),
                                 st.Page(main, title="📝Conversor de Moedas")],
                    "𝗖𝗼𝗻𝘁𝗮": [st.Page(logout, title="⊗ Sair"), st.Page("criar_conta.py", title="＋ Criar Conta")]
                    }
        )
    else:
        pg = st.navigation(
        
                  {
                        
                    "𝗛𝗼𝗺𝗲":[st.Page("homepage.py", title="★ Cotralti Corporation")],
                    "𝗖𝗼𝗻𝘀𝘂𝗹𝘁𝗮𝘀 𝗻𝗮 𝗧𝗮𝗯𝗲𝗹𝗮 𝗦𝗽𝗶𝗰𝗲": [st.Page("calculadorafrete.py", title="① Calculadora de Frete Tonelada"),
                                st.Page("fretededicado.py", title="② Rota Dedicada"),
                                st.Page("consultarotas.py", title="③ Consulta por Rotas"),
                                st.Page("rateiofrete.py", title="④ Rateio de Frete por peso")],
                     "𝐔𝐭𝐢𝐥𝐢𝐭𝐚́𝐫𝐢𝐨𝐬":[st.Page("separadorpdf.py", title="📝Separador Arquivos PDF"),
                                 st.Page("juntarpdf.py", title="📝Juntar Arquivos PDF"),
                                 st.Page("conversor_moedas.py", title="📝Conversor de Moedas")],
                    "𝗖𝗼𝗻𝘁𝗮": [st.Page(logout, title="⊗ Sair")]
                    }
        )
        
    pg.run()
