import streamlit as st
import requests

# Substitua "YOUR_ACCESS_KEY" pela sua chave de acesso válida
API_ACCESS_KEY = "9ca044ea657f67cba538ee3622b076f8"
def get_exchange_rate(base_currency, target_currency, amount):
    """Busca a taxa de câmbio e calcula a conversão entre duas moedas."""
    url = f"https://api.exchangerate.host/convert?access_key={API_ACCESS_KEY}&from={base_currency}&to={target_currency}&amount={amount}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para erros HTTP
        data = response.json()
        if data.get("success"):
            return data.get("result")  # O campo 'result' contém o valor convertido
        else:
            error_info = data.get("error", {}).get("info", "Erro desconhecido.")
            st.error(f"Erro da API: {error_info}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")
        return None

def main():
    st.header("💱Conversor de :blue[Moedas] ", divider='green')
    st.write("Converta valores entre diferentes moedas usando taxas de câmbio atualizadas.")

    # Seleção das moedas
    currencies = ['USD', 'EUR', 'BRL', 'GBP', 'JPY', 'AUD', 'CAD']
    base_currency = st.selectbox("Selecione a moeda de origem:", currencies)
    target_currency = st.selectbox("Selecione a moeda de destino:", currencies)

    # Entrada do valor
    amount = st.number_input("Digite o valor a ser convertido:", min_value=0.0, step=0.01)

    # Botão de conversão
    if st.button("Converter"):
        if base_currency == target_currency:
            st.warning("As moedas de origem e destino são iguais. Selecione moedas diferentes.")
        elif amount <= 0:
            st.warning("Digite um valor maior que zero para a conversão.")
        else:
            converted_amount = get_exchange_rate(base_currency, target_currency, amount)
            if converted_amount is not None:
                #st.success(f" Conseguimos converter os valores: **{amount:,.2f} {base_currency}** é igual a **{converted_amount:,.2f} {target_currency}**.")
                st.success(f"Conseguimos converter os valores de : **{amount:_.2f}**".replace('.',',').replace('_','.') + f" {base_currency}" + f" é igual a  **{converted_amount:_.2f}**".replace('.',',').replace('_','.') + f" {target_currency}")
            else:
                st.error("Não foi possível realizar a conversão. Tente novamente mais tarde.")

if __name__ == "__main__":
    main()
