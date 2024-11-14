import streamlit as st
import fitz  # PyMuPDF para manipulação de PDF
from datetime import datetime
from io import BytesIO

# Função para mesclar vários PDFs em um único arquivo
def merge_pdfs(files):
    merged_pdf = fitz.open()  # Novo arquivo PDF para receber as páginas combinadas
    
    for file in files:
        pdf = fitz.open("pdf", file.read())  # Abre cada arquivo PDF carregado
        merged_pdf.insert_pdf(pdf)  # Adiciona cada página ao PDF final
        pdf.close()
    
    # Salva o PDF mesclado em um buffer de bytes
    pdf_buffer = BytesIO()
    merged_pdf.save(pdf_buffer)
    merged_pdf.close()
    pdf_buffer.seek(0)
    
    return pdf_buffer

# Interface do Streamlit
st.header("Unificador de Arquivos :blue[PDF] ", divider='green')

uploaded_files = st.file_uploader("**Carregue vários arquivos PDF**", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} **arquivos carregados com sucesso!**")
    st.divider()
    if st.button("Juntar PDFs e Baixar"):
        # Mescla os PDFs carregados
        merged_pdf_buffer = merge_pdfs(uploaded_files)
        
        # Gera o nome do arquivo PDF com a data atual
        current_date = datetime.now().strftime("%Y-%m-%d")
        pdf_filename = f"pdf_mesclado_{current_date}.pdf"
        
        # Botão para baixar o PDF mesclado
        st.download_button(
            label="Baixar PDF Mesclado",
            data=merged_pdf_buffer,
            file_name=pdf_filename,
            mime="application/pdf"
        )
