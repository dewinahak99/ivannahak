import streamlit as st
import pandas as pd
import numpy as np


# Judul aplikasi
st.title("Aplikasi Ivan Nahak")



# Teks pengantar
st.write("""
Ini adalah aplikasi sederhana untuk menampilkan data acak dalam bentuk grafik.
Pilih jumlah data dan jenis grafik yang ingin ditampilkan.
""")

# Input untuk memilih jumlah data
data_points = st.slider("Pilih jumlah data:", min_value=10, max_value=100, value=30)

# Menghasilkan data acak
data = pd.DataFrame(
    np.random.randn(data_points, 3),
    columns=["Kolom 1", "Kolom 2", "Kolom 3"]
)

# Pilih jenis grafik
chart_type = st.selectbox("Pilih jenis grafik:", ["Line Chart", "Bar Chart", "Area Chart"])

# Menampilkan grafik berdasarkan pilihan
st.write("### Grafik Data Acak")
if chart_type == "Line Chart":
    st.line_chart(data)
elif chart_type == "Bar Chart":
    st.bar_chart(data)
elif chart_type == "Area Chart":
    st.area_chart(data)

# Menampilkan tabel data
st.write("### Data Acak yang Ditampilkan")
st.dataframe(data)
