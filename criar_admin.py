from models import session , Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["cotralti01"]).generate()[0]
usuario = Usuario(nome="Thiago Gastal", senha=senha_criptografada, email="thiago.gastal@archroma.com", admin=False)
session.add(usuario)
session.commit()
