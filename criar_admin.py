from models import session , Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["s3cr3t4r14"]).generate()[0]
usuario = Usuario(nome="Luis Felipe", senha=senha_criptografada, email="ldavid@cotralti.com.br", admin=True)
session.add(usuario)
session.commit()
