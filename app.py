import streamlit as st
import pandas as pd
import numpy as np
import io


st.title('Aplikasi Pengolahan THC')
st.write("""Ini digunakan untuk menyatukan file THC FINAL, TAK, TLP dan KDP""")

uploaded_files = st.file_uploader("Unggah file Excel", accept_multiple_files=True, type=["xlsx"])

if uploaded_files:
    dfs = {}
    for file in uploaded_files:
        df = pd.read_excel(file, engine='openpyxl')  # Baca file Excel dengan pandas
        dfs[file.name] = df


    # Konversi data menjadi DataFrame
    if 'TAK.xlsx' in dfs:
        df1 = dfs['TAK.xlsx']
    
        new_columns1 = ['DEBIT_PINJAMAN UMUM','DEBIT_PINJAMAN RENOVASI RUMAH','DEBIT_PINJAMAN SANITASI','DEBIT_PINJAMAN ARTA','DEBIT_PINJAMAN MIKROBISNIS','DEBIT_PINJAMAN DT. PENDIDIKAN','DEBIT_PINJAMAN PERTANIAN','DEBIT_TOTAL','CREDIT_PINJAMAN UMUM','CREDIT_PINJAMAN RENOVASI RUMAH','CREDIT_PINJAMAN SANITASI','CREDIT_PINJAMAN ARTA','CREDIT_PINJAMAN MIKROBISNIS','CREDIT_PINJAMAN DT. PENDIDIKAN','CREDIT_PINJAMAN PERTANIAN','CREDIT_TOTAL']
        
        for col in new_columns1:
            if col not in df1.columns:
                df1[col] = 0

        
            st.write("TAK TOTAL:")
            st.write(df1)
