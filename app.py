import streamlit as st
import pandas as pd
import numpy as np
import io
import glob
import os

st.title('Aplikasi Pengolahan THC')
st.write("Ini digunakan untuk menyatukan file THC FINAL, TAK, TLP dan KDP")

uploaded_files = st.file_uploader("Unggah file Excel", accept_multiple_files=True, type=["xlsx"])

if uploaded_files:
    dfs = {file.name: pd.read_excel(file, engine='openpyxl') for file in uploaded_files}

    def process_dataframe(df, new_columns, rename_dict, desired_order):
        for col in new_columns:
            if col not in df.columns:
                df[col] = 0
        
        df = df.rename(columns=rename_dict)
        
        for col in desired_order:
            if col not in df.columns:
                df[col] = 0
        
        return df[desired_order]

    combined_df_list = []
    
    if 'THC FINAL.xlsx' in dfs:
        df_thc = dfs['THC FINAL.xlsx']
        combined_df_list.append(df_thc)
        
    if 'TAK.xlsx' in dfs:
        df_tak = dfs['TAK.xlsx']
        new_columns_tak = [
            'DEBIT_PINJAMAN UMUM', 'DEBIT_PINJAMAN RENOVASI RUMAH', 'DEBIT_PINJAMAN SANITASI',
            'DEBIT_PINJAMAN ARTA', 'DEBIT_PINJAMAN MIKROBISNIS', 'DEBIT_PINJAMAN DT. PENDIDIKAN',
            'DEBIT_PINJAMAN PERTANIAN', 'DEBIT_TOTAL', 'CREDIT_PINJAMAN UMUM',
            'CREDIT_PINJAMAN RENOVASI RUMAH', 'CREDIT_PINJAMAN SANITASI', 'CREDIT_PINJAMAN ARTA',
            'CREDIT_PINJAMAN MIKROBISNIS', 'CREDIT_PINJAMAN DT. PENDIDIKAN',
            'CREDIT_PINJAMAN PERTANIAN', 'CREDIT_TOTAL'
        ]
        rename_dict_tak = {
            'KELOMPOK': 'KEL', 'DEBIT_PINJAMAN ARTA': 'Db PRT', 'DEBIT_PINJAMAN DT. PENDIDIKAN': 'Db DTP',
            'DEBIT_PINJAMAN MIKROBISNIS': 'Db PMB', 'DEBIT_PINJAMAN SANITASI': 'Db PSA',
            'DEBIT_PINJAMAN UMUM': 'Db PU', 'DEBIT_PINJAMAN RENOVASI RUMAH': 'Db PRR',
            'DEBIT_PINJAMAN PERTANIAN': 'Db PTN', 'DEBIT_TOTAL': 'Db Total2',
            'CREDIT_PINJAMAN ARTA': 'Cr PRT', 'CREDIT_PINJAMAN DT. PENDIDIKAN': 'Cr DTP',
            'CREDIT_PINJAMAN MIKROBISNIS': 'Cr PMB', 'CREDIT_PINJAMAN SANITASI': 'Cr PSA',
            'CREDIT_PINJAMAN UMUM': 'Cr PU', 'CREDIT_PINJAMAN RENOVASI RUMAH': 'Cr PRR',
            'CREDIT_PINJAMAN PERTANIAN': 'Cr PTN', 'CREDIT_TOTAL': 'Cr Total2'
        }
        desired_order_tak = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE',
            'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara',
            'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok', 'Db SIPADAN', 'Cr SIPADAN',
            'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total',
            'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB',
            'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
        ]
        
        df_tak = process_dataframe(df_tak, new_columns_tak, rename_dict_tak, desired_order_tak)
        st.write("TAK FINAL:")
        st.write(df_tak)
        combined_df_list.append(df_tak)

    if 'TLP.xlsx' in dfs:
        df_tlp = dfs['TLP.xlsx']
        new_columns_tlp = [
            'DEBIT_Simpanan Pensiun', 'DEBIT_Simpanan Pokok', 'DEBIT_Simpanan Sukarela',
            'DEBIT_Simpanan Wajib', 'DEBIT_Simpanan Hari Raya', 'DEBIT_Simpanan Qurban',
            'DEBIT_Simpanan Sipadan', 'DEBIT_Simpanan Khusus', 'CREDIT_Simpanan Pensiun',
            'CREDIT_Simpanan Pokok', 'CREDIT_Simpanan Sukarela', 'CREDIT_Simpanan Wajib',
            'CREDIT_Simpanan Hari Raya', 'CREDIT_Simpanan Qurban', 'CREDIT_Simpanan Sipadan',
            'CREDIT_Simpanan Khusus'
        ]
        rename_dict_tlp = {
            'KELOMPOK': 'KEL', 'DEBIT_Simpanan Hari Raya': 'Db Sihara',
            'DEBIT_Simpanan Pensiun': 'Db Pensiun', 'DEBIT_Simpanan Pokok': 'Db Pokok',
            'DEBIT_Simpanan Sukarela': 'Db Sukarela', 'DEBIT_Simpanan Wajib': 'Db Wajib',
            'DEBIT_Simpanan Qurban': 'Db Qurban', 'DEBIT_Simpanan Sipadan': 'Db SIPADAN',
            'DEBIT_Simpanan Khusus': 'Db Khusus', 'DEBIT_TOTAL': 'Db Total',
            'CREDIT_Simpanan Hari Raya': 'Cr Sihara', 'CREDIT_Simpanan Pensiun': 'Cr Pensiun',
            'CREDIT_Simpanan Pokok': 'Cr Pokok', 'CREDIT_Simpanan Sukarela': 'Cr Sukarela',
            'CREDIT_Simpanan Wajib': 'Cr Wajib', 'CREDIT_Simpanan Qurban': 'Cr Qurban',
            'CREDIT_Simpanan Sipadan': 'Cr SIPADAN', 'CREDIT_Simpanan Khusus': 'Cr Khusus',
            'CREDIT_TOTAL': 'Cr Total'
        }
        desired_order_tlp = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE',
            'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara',
            'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok', 'Db SIPADAN', 'Cr SIPADAN',
            'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total',
            'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB',
            'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
        ]

        df_tlp = process_dataframe(df_tlp, new_columns_tlp, rename_dict_tlp, desired_order_tlp)
        st.write("TLP FINAL:")
        st.write(df_tlp)
        combined_df_list.append(df_tlp)

    if 'KDP.xlsx' in dfs:
        df_kdp = dfs['KDP.xlsx']
        new_columns_kdp = [
            'DEBIT_Simpanan Pensiun', 'DEBIT_Simpanan Pokok', 'DEBIT_Simpanan Sukarela',
            'DEBIT_Simpanan Wajib', 'DEBIT_Simpanan Hari Raya', 'DEBIT_Simpanan Qurban',
            'DEBIT_Simpanan Sipadan', 'DEBIT_Simpanan Khusus', 'CREDIT_Simpanan Pensiun',
            'CREDIT_Simpanan Pokok', 'CREDIT_Simpanan Sukarela', 'CREDIT_Simpanan Wajib',
            'CREDIT_Simpanan Hari Raya', 'CREDIT_Simpanan Qurban', 'CREDIT_Simpanan Sipadan',
            'CREDIT_Simpanan Khusus'
        ]
        rename_dict_kdp = {
            'KELOMPOK': 'KEL', 'DEBIT_Simpanan Hari Raya': 'Db Sihara',
            'DEBIT_Simpanan Pensiun': 'Db Pensiun', 'DEBIT_Simpanan Pokok': 'Db Pokok',
            'DEBIT_Simpanan Sukarela': 'Db Sukarela', 'DEBIT_Simpanan Wajib': 'Db Wajib',
            'DEBIT_Simpanan Qurban': 'Db Qurban', 'DEBIT_Simpanan Sipadan': 'Db SIPADAN',
            'DEBIT_Simpanan Khusus': 'Db Khusus', 'DEBIT_TOTAL': 'Db Total',
            'CREDIT_Simpanan Hari Raya': 'Cr Sihara', 'CREDIT_Simpanan Pensiun': 'Cr Pensiun',
            'CREDIT_Simpanan Pokok': 'Cr Pokok', 'CREDIT_Simpanan Sukarela': 'Cr Sukarela',
            'CREDIT_Simpanan Wajib': 'Cr Wajib', 'CREDIT_Simpanan Qurban': 'Cr Qurban',
            'CREDIT_Simpanan Sipadan': 'Cr SIPADAN', 'CREDIT_Simpanan Khusus': 'Cr Khusus',
            'CREDIT_TOTAL': 'Cr Total'
        }
        desired_order_kdp = [
            'ID ANGGOTA', 'DUMMY', 'NAMA', 'CENTER', 'KEL', 'HARI', 'JAM', 'SL', 'TRANS. DATE',
            'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara',
            'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok', 'Db SIPADAN', 'Cr SIPADAN',
            'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total',
            'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB',
            'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
        ]

        df_kdp = process_dataframe(df_kdp, new_columns_kdp, rename_dict_kdp, desired_order_kdp)
        st.write("KDP FINAL:")
        st.write(df_kdp)
        combined_df_list.append(df_kdp)

    columns_to_replace = [
    'Db Qurban', 'Cr Qurban', 'Db Khusus', 'Cr Khusus', 'Db Sihara', 'Cr Sihara',
    'Db Pensiun', 'Cr Pensiun', 'Db Pokok', 'Cr Pokok', 'Db SIPADAN', 'Cr SIPADAN',
    'Db Sukarela', 'Cr Sukarela', 'Db Wajib', 'Cr Wajib', 'Db Total', 'Cr Total',
    'Db PTN', 'Cr PTN', 'Db PRT', 'Cr PRT', 'Db DTP', 'Cr DTP', 'Db PMB', 'Cr PMB',
    'Db PRR', 'Cr PRR', 'Db PSA', 'Cr PSA', 'Db PU', 'Cr PU', 'Db Total2', 'Cr Total2'
    ]

if 'combined_df_list' not in locals():
    st.error("combined_df_list belum didefinisikan.")
elif not combined_df_list:
    st.error("combined_df_list kosong.")
else:
    # Hapus DataFrame kosong dari daftar
    combined_df_list = [df for df in combined_df_list if not df.empty]

    if not combined_df_list:
        st.error("Semua DataFrame dalam daftar kosong.")
    else:
        try: # Menggabungkan semua DataFrame
            combined_df = pd.concat(combined_df_list, ignore_index=True)

            # Fungsi untuk membersihkan dan mengkonversi kolom
            def clean_and_convert(value):
                if pd.isna(value):
                    return value
                value = str(value).replace(',', '').replace('.', '')
                try:
                    return pd.to_numeric(value)
                except ValueError:
                    return value

# Membersihkan dan mengkonversi kolom-kolom yang ditentukan
            for col in columns_to_replace:
                if col in combined_df.columns:
                    combined_df[col] = combined_df[col].apply(clean_and_convert)

            st.write("Combined DataFrame:")
            st.write(combined_df)

# Download links for pivot tables
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                combined_df.to_excel(writer, index=False, sheet_name='Sheet1')
            buffer.seek(0)

            st.download_button(
                label="Unduh Format data THC gabungan.xlsx",
                data=buffer.getvalue(),
                file_name='Format data THC gabungan.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
