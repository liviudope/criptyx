import streamlit as st
from cryptography.fernet import Fernet

# Titlul aplicației
st.title("Criptare și Decriptare Mesaje")

# Generarea sau introducerea cheii
key_option = st.radio("Vrei să folosești o cheie generată automat sau să introduci una?", ('Generată automat', 'Introdu propria cheie'))

# Variabila pentru cheie trebuie definită
key = None

if key_option == 'Generată automat':
    key = Fernet.generate_key()
    st.write("Cheia generată este:", key.decode())
else:
    key_input = st.text_input("Introdu cheia (trebuie să fie în formatul corect)")
    if key_input:
        key = key_input.encode()

# Asigură-te că ai o cheie înainte de a continua
if key:
    # Crearea instanței Fernet cu cheia generată sau introdusă
    fernet = Fernet(key)

    # Opțiuni pentru criptare sau decriptare
    option = st.radio("Alege ce vrei să faci:", ('Criptează mesaj', 'Decriptează mesaj'))

    if option == 'Criptează mesaj':
        mesaj = st.text_area("Introdu mesajul pentru criptare")
        if st.button("Criptează"):
            if mesaj:
                mesaj_criptat = fernet.encrypt(mesaj.encode())
                st.write("Mesajul criptat este:", mesaj_criptat.decode())
            else:
                st.error("Te rog introdu un mesaj pentru a-l cripta.")

    elif option == 'Decriptează mesaj':
        mesaj_criptat = st.text_area("Introdu mesajul criptat")
        if st.button("Decriptează"):
            try:
                if mesaj_criptat:
                    mesaj_decriptat = fernet.decrypt(mesaj_criptat.encode()).decode()
                    st.write("Mesajul decriptat este:", mesaj_decriptat)
                else:
                    st.error("Te rog introdu un mesaj criptat pentru a-l decripta.")
            except Exception as e:
                st.error(f"Eroare la decriptare: {str(e)}")
else:
    st.warning("Te rog să generezi o cheie sau să introduci una pentru a continua.")