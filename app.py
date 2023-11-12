
import streamlit as st
import sqlite3
import ast

def delete_order(order_id):
    conn = sqlite3.connect('tong.db')
    cursor = conn.cursor()

    # Perform the deletion logic here
    cursor.execute('DELETE FROM Orders WHERE OrderCode=?', (order_id,))
    conn.commit()

with sqlite3.connect('tong.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT OrderCode, Product, TotalPrice, CustomerNote FROM Orders")
    data = cursor.fetchall()
    st.title('รายการคำสั่งซื้อทั้งหมด')
    for product in data:
        OrderCode, Product, TotalPrice, CustomerNote = product
        product_dict = ast.literal_eval(Product)
        with st.form(key=f'form_{OrderCode}'):
            st.write(OrderCode)
            st.write("**สินค้า:**")
            for item_name, item_quantity in product_dict.items():
                st.write(f"- {item_name} จำนวน {item_quantity}")
            st.write(f'**ราคารวม:** :red[{TotalPrice} ฿]')
            st.write(f'**โน้ตถึงร้านค้า:** {CustomerNote}')
            if st.form_submit_button(label='Finish', use_container_width=True):
                delete_order(OrderCode)
        






