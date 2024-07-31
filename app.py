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
        df_tak = dfs['TAK.xlsx']
    
    if 'TLP.xlsx' in dfs:
        df_tlp = dfs['TLP.xlsx']
    
    if 'KDP.xlsx' in dfs:
        df_kdp = dfs['KDP.xlsx']

    # Process TAK
        new_columns1 = ['DEBIT_PINJAMAN UMUM','DEBIT_PINJAMAN RENOVASI RUMAH','DEBIT_PINJAMAN SANITASI','DEBIT_PINJAMAN ARTA','DEBIT_PINJAMAN MIKROBISNIS','DEBIT_PINJAMAN DT. PENDIDIKAN','DEBIT_PINJAMAN PERTANIAN','DEBIT_TOTAL','CREDIT_PINJAMAN UMUM','CREDIT_PINJAMAN RENOVASI RUMAH','CREDIT_PINJAMAN SANITASI','CREDIT_PINJAMAN ARTA','CREDIT_PINJAMAN MIKROBISNIS','CREDIT_PINJAMAN DT. PENDIDIKAN','CREDIT_PINJAMAN PERTANIAN','CREDIT_TOTAL']
        
        for col in new_columns1:
            if col not in df_tak.columns:
                df_tak[col] = 0

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
            
        df_tak = df_tak.rename(columns=rename_dict)
            
        desired_order = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE', 'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara', 'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok',
            'Db SIPADAN', 'Cr SIPADAN', 'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total', 'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB', 'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
            ]

        # Tambahkan kolom yang mungkin belum ada dalam DataFrame
        for col in desired_order:
            if col not in df_tak.columns:
                df_tak[col] = 0

            df_tak = df_tak[desired_order]
            
        st.write("TAK FINAL:")
        st.write(df_tak)

        #Process TLP df_tlp
        new_columns2 = ['DEBIT_Simpanan Pensiun',
        'DEBIT_Simpanan Pokok',
        'DEBIT_Simpanan Sukarela',
        'DEBIT_Simpanan Wajib',
        'DEBIT_Simpanan Hari Raya',
        'DEBIT_Simpanan Qurban',
        'DEBIT_Simpanan Sipadan',
        'DEBIT_Simpanan Khusus',
        'CREDIT_Simpanan Pensiun',
        'CREDIT_Simpanan Pokok',
        'CREDIT_Simpanan Sukarela',
        'CREDIT_Simpanan Wajib',
        'CREDIT_Simpanan Hari Raya',
        'CREDIT_Simpanan Qurban',
        'CREDIT_Simpanan Sipadan',
        'CREDIT_Simpanan Khusus'
        ]

        for col in new_columns2:
            if col not in df_tlp.columns:
                df_tlp[col] = 0

        
        rename_dict = {
        'KELOMPOK': 'KEL',
        'DEBIT_Simpanan Hari Raya': 'Db Sihara',
        'DEBIT_Simpanan Pensiun': 'Db Pensiun',
        'DEBIT_Simpanan Pokok': 'Db Pokok',
        'DEBIT_Simpanan Sukarela': 'Db Sukarela',
        'DEBIT_Simpanan Wajib': 'Db Wajib',
        'DEBIT_Simpanan Qurban': 'Db Qurban',
        'DEBIT_Simpanan Sipadan': 'Db SIPADAN',
        'DEBIT_Simpanan Khusus': 'Db Khusus',
        'DEBIT_TOTAL': 'Db Total',
        'CREDIT_Simpanan Hari Raya': 'Cr Sihara',
        'CREDIT_Simpanan Pensiun': 'Cr Pensiun',
        'CREDIT_Simpanan Pokok': 'Cr Pokok',
        'CREDIT_Simpanan Sukarela': 'Cr Sukarela',
        'CREDIT_Simpanan Wajib': 'Cr Wajib',
        'CREDIT_Simpanan Qurban': 'Cr Qurban',
        'CREDIT_Simpanan Sipadan': 'Cr SIPADAN',
        'CREDIT_Simpanan Khusus': 'Cr Khusus',
        'CREDIT_TOTAL': 'Cr Total'
    }

        df_tlp = df_tlp.rename(columns=rename_dict)
        
    desired_order = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE', 'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara', 'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok',
            'Db SIPADAN', 'Cr SIPADAN', 'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total', 'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB', 'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
            ]
 # Tambahkan kolom yang mungkin belum ada dalam DataFrame
    for col in desired_order:
        if col not in df_tlp.columns:
            df_tlp[col] = 0

        df_tlp = df_tlp[desired_order]
        
        st.write("TLP FINAL:")
        st.write(df_tlp)
