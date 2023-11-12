import streamlit as st
import sqlite3

# ติดต่อฐานข้อมูล SQL
conn = sqlite3.connect('tong.db')
cursor = conn.cursor()  # สร้าง cursor

# ปฏิบัติการ SQL 
cursor.execute("SELECT IDproduct, NameProduct, PricePerUnit, Image FROM ProduceInfo")
data = cursor.fetchall()

# Create a dictionary to store product information in the shopping cart
st.write(data)





        






