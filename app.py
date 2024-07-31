import streamlit as st
import pandas as pd
import numpy as np
import io


st.title('Aplikasi Pengolahan THC')
st.write("""Ini digunakan untuk menyatukan file THC FINAL, TAK, TLP dan KDP""")

# Function to format numbers
def format_no(no):
    try:
        if pd.notna(no):
            return f'{int(no):02d}.'
        else:
            return ''
    except (ValueError, TypeError):
        return str(no)

def format_center(center):
    try:
        if pd.notna(center):
            return f'{int(center):03d}'
        else:
            return ''
    except (ValueError, TypeError):
        return str(center)

def format_kelompok(kelompok):
    try:
        if pd.notna(kelompok):
            return f'{int(kelompok):02d}'
        else:
            return ''
    except (ValueError, TypeError):
        return str(kelompok)

# File upload
uploaded_files = st.file_uploader("Unggah file CSV", accept_multiple_files=True)

if uploaded_files:
    # Read CSV files
    dfs = {}
    for file in uploaded_files:
        df = pd.read_csv(file, delimiter=';', low_memory=False)
        dfs[file.name] = df

    # Process TAK
    if 'DbSimpanan.csv' in dfs:
        df1 = dfs['TAK.xlsx']
        df1.columns = df1.columns.str.strip()

        new_columns1 = [
                'DEBIT_PINJAMAN UMUM',
                'DEBIT_PINJAMAN RENOVASI RUMAH',
                'DEBIT_PINJAMAN SANITASI',
                'DEBIT_PINJAMAN ARTA',
                'DEBIT_PINJAMAN MIKROBISNIS',
                'DEBIT_PINJAMAN DT. PENDIDIKAN',
                'DEBIT_PINJAMAN PERTANIAN',
                'DEBIT_TOTAL',
                'CREDIT_PINJAMAN UMUM',
                'CREDIT_PINJAMAN RENOVASI RUMAH',
                'CREDIT_PINJAMAN SANITASI',
                'CREDIT_PINJAMAN ARTA',
                'CREDIT_PINJAMAN MIKROBISNIS',
                'CREDIT_PINJAMAN DT. PENDIDIKAN',
                'CREDIT_PINJAMAN PERTANIAN',
                'CREDIT_TOTAL'
            ]

        for col in new_columns1:
            if col not in df1.columns:
                df1[col] = 0

            rename_dict = {
                'KELOMPOK': 'KEL',
                'DEBIT_PINJAMAN ARTA': 'Db PRT',
                'DEBIT_PINJAMAN DT. PENDIDIKAN': 'Db DTP',
                'DEBIT_PINJAMAN MIKROBISNIS': 'Db PMB',
                'DEBIT_PINJAMAN SANITASI': 'Db PSA',
                'DEBIT_PINJAMAN UMUM': 'Db PU',
                'DEBIT_PINJAMAN RENOVASI RUMAH': 'Db PRR',
                'DEBIT_PINJAMAN PERTANIAN': 'Db PTN',
                'DEBIT_TOTAL': 'Db Total2',
                'CREDIT_PINJAMAN ARTA': 'Cr PRT',
                'CREDIT_PINJAMAN DT. PENDIDIKAN': 'Cr DTP',
                'CREDIT_PINJAMAN MIKROBISNIS': 'Cr PMB',
                'CREDIT_PINJAMAN SANITASI': 'Cr PSA',
                'CREDIT_PINJAMAN UMUM': 'Cr PU',
                'CREDIT_PINJAMAN RENOVASI RUMAH': 'Cr PRR',
                'CREDIT_PINJAMAN PERTANIAN': 'Cr PTN',
                'CREDIT_TOTAL': 'Cr Total2'
            }
            
            df1 = df1.rename(columns=rename_dict)
            
            desired_order = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE',
            'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB', 'Db PRR', 'Cr PRR',
            'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
            ]
        
            # Tambahkan kolom yang mungkin belum ada dalam DataFrame
            for col in desired_order:
                if col not in df1.columns:
                    df1[col] = 0

            df1 = df1[desired_order]
        
            st.write("TAK TOTAL:")
            st.write(df1)
