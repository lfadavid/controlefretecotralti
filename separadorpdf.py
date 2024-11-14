import streamlit as st
import fitz  # PyMuPDF para manipulação de PDF
import os
import zipfile
from io import BytesIO
from datetime import datetime

# Função para separar o PDF em várias páginas e salvar no diretório temporário
def split_pdf(file_bytes):
    pdf = fitz.open("pdf", file_bytes)  # Carrega o PDF diretamente dos bytes
    pages = []
    
    for page_num in range(pdf.page_count):
        pdf_writer = fitz.open()  # Novo arquivo para cada página
        pdf_writer.insert_pdf(pdf, from_page=page_num, to_page=page_num)
        
        # Salva a página em um arquivo temporário
        page_path = f"page_{page_num + 1}.pdf"
        pdf_writer.save(page_path)
        pages.append(page_path)
        pdf_writer.close()
        
    pdf.close()
    return pages

# Função para criar um arquivo ZIP com as páginas separadas
def create_zip(files):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for file in files:
            zip_file.write(file, os.path.basename(file))
    zip_buffer.seek(0)
    return zip_buffer

# Interface do Streamlit
st.header("Separador de Arquivos :blue[PDF] ", divider='green')

uploaded_file = st.file_uploader("**Carregue um arquivo PDF**", type="pdf")

if uploaded_file is not None:
    st.write("Arquivo carregado com sucesso!")
    
    if st.button("Separar PDF e Baixar"):
        # Converte o arquivo carregado para bytes para ser lido pelo PyMuPDF
        file_bytes = uploaded_file.read()
        
        # Divide o PDF em arquivos de páginas
        page_files = split_pdf(file_bytes)
        
        # Gera o nome do arquivo ZIP com a data atual
        current_date = datetime.now().strftime("%Y-%m-%d")
        zip_filename = f"paginas_separadas_{current_date}.zip"
        
        # Cria o arquivo ZIP para download
        zip_buffer = create_zip(page_files)
        
        # Botão para baixar o arquivo ZIP
        st.download_button(
            label="Baixar PDF Separado (ZIP)",
            data=zip_buffer,
            file_name=zip_filename,
            mime="application/zip"
        )
        
        # Limpa os arquivos temporários
        for file in page_files:
            os.remove(file)
