import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados():
    df = pd.read_excel("Tabela_Spice.xlsx")
    return df
#Cabeçalhos do sistemas


    
st.header("Calculadora de :blue[Frete] ", divider='green')

#df = pd.DataFrame(TabelaSpice)
df = carregar_dados()


#Inserindo as colunas na tela
coluna_esquerda , coluna_meio , coluna_direita = st.columns([1, 1, 1])

peso_digitado = coluna_esquerda.number_input(label="Digite o peso em Kg", min_value=0.0, placeholder="Digite o valor do peso", value=None)

rota_digitada = coluna_meio.selectbox(
                        key=1,
                        label="Código",
                        options=df["Código"].unique(),
                        placeholder="Selecione a rota desejada",
                        index=None
)

#filtrando pelo codigo

df_filtro = df[df['Código'] == rota_digitada]

  
def calcular_frete(rota_digitada, peso_digitado, ):
    # Filtrar a linha correspondente ao código fornecido
   
    df_filtro = df[df['Código'] == rota_digitada]
    
    if df_filtro.empty:
        return "Código não encontrado."
    
   
     # Obter os valores mínimos e as faixas de peso
    peso_minimo = df_filtro['Peso Mínimo'].values[0]
    frete_minimo = df_filtro['Frete Mínimo'].values[0]
    
    
    if rota_digitada == 'ARCRS05' or rota_digitada == 'ARCRS06' or rota_digitada == 'ARCSC07':
    
        if peso_digitado <= peso_minimo:
            return frete_minimo
        elif peso_digitado > peso_minimo and peso_digitado <= 1000:
            return df_filtro['Até 1.000'].values[0]
        elif peso_digitado >= 1001 and peso_digitado <= 3000:
            return df_filtro['1.001 a 3.000'].values[0]
        elif peso_digitado >=3001 and peso_digitado <= 6000:
            return df_filtro['3.001 a 6.000'].values[0]
        elif peso_digitado >=6001 and peso_digitado <= 13000:
            return df_filtro['6.001 a 13.000'].values[0]
        else:
            return df_filtro['Acima 13.001'].values[0] 
    
    if rota_digitada != 'ARCRS05' or rota_digitada != 'ARCRS06' or rota_digitada != 'ARCSC07':
    # Verificar a faixa de peso
        if peso_digitado <= peso_minimo:
            return frete_minimo
        elif peso_digitado > peso_minimo and peso_digitado <= 1000:
            return (df_filtro['Até 1.000'].values[0] /1000) * peso_digitado
        elif peso_digitado >= 1001 and peso_digitado <= 3000:
            return (df_filtro['1.001 a 3.000'].values[0] /1000) * peso_digitado
        elif peso_digitado >=3001 and peso_digitado <= 6000:
            return (df_filtro['3.001 a 6.000'].values[0] /1000) * peso_digitado
        elif peso_digitado >=6001 and peso_digitado <= 13000:
            return (df_filtro['6.001 a 13.000'].values[0] / 1000) * peso_digitado
        else:
            return (df_filtro['Acima 13.001'].values[0] / 1000) * peso_digitado


if peso_digitado is not None and rota_digitada is not None:
       
       if st.button("Cᥲᥣᥴᥙᥣᥲr Frᥱtᥱ",help="Favor incluir os dados nos campos!", type="primary"):

        
        valor_frete = calcular_frete(rota_digitada , peso_digitado)
        fretepeso = (valor_frete)
        valorfretekg = fretepeso / peso_digitado
        regiao = df_filtro["Destino Regiões"].values[0]
        taxanf = df_filtro["Taxa (R$ /NFE)"].values[0]
        tipo = df_filtro["Tipo"].values[0]
        adv = df_filtro["ADV(%)"].values[0]
                    
        st.divider()
        
        st.success("𝖢𝗈𝗇𝗌𝖾𝗀𝗎𝗂𝗆𝗈𝗌 𝖼𝖺𝗅𝖼𝗎𝗅𝖺𝗋 𝖺 𝗌𝗎𝖺 𝗌𝗈𝗅𝗂𝖼𝗂𝗍𝖺𝖼̧𝖺̃𝗈 𝗌𝗈𝖻𝗋𝖾 𝗈 𝖿𝗋𝖾𝗍𝖾.")
        coluna_esquerda , coluna_meio , coluna_direita = st.columns([1, 1,1])  
                
        coluna_meio.metric(f"**A Tabela escolhida é** ",f'{rota_digitada}')
        coluna_esquerda.metric("𝗢 𝘃𝗮𝗹𝗼𝗿 𝗱𝗼 𝗙𝗿𝗲𝘁𝗲 𝗥𝗼𝘁𝗮 𝗲́",f'R$ {fretepeso:,.2f} reais')
        coluna_direita.metric("𝗢 𝘃𝗮𝗹𝗼𝗿 𝗱𝗼 **KG** do produto é",f'R$ {valorfretekg:,.2f} reais')
       
        st.divider()
        
        st.write("❶ Para calcular o **FRETE TOTAL** é necessário somar: ( **Frete Rota + Taxa NF + ADValorem + Icms )**.")
        st.write(f"❷ O Destino é as  **{regiao}** .")
        st.write(f"❸ O valor da Taxa de emissão do CTE é de **R$ {taxanf:.2f} reais**.")
        st.write(f"❹ O **AD VALOREM** (_é uma taxa cobrada pelo transportador para proteger a carga contra danos durante a movimentação_) o valor é de **0,05%**.")
        st.write(f"❺ O **ICMS** de transporte (_é o imposto que incide sobre o serviço de transporte de cargas, seja ele rodoviário, ferroviário, aéreo ou aquaviário_)  **RJ x RJ = 22%** , **RJ x _( SP, MG, PR, SC e RS )_ = 12%** .")
        st.write(f"❻ O Tipo da Carga é **{tipo}**.")
        st.divider()
        st.write("""
         &copy; 2024 - Luis Felipe A. David. Todos os direitos reservados
         """) 
else:
    st.button("Calcular Frete",disabled=True)
 
