import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Trang Chủ",
    page_icon="👋",
)


logo = Image.open('images\logo.png')
st.image(logo, width=800)

st.title("Website Machine Learning")
st.caption("Thực hiện bởi: Nguyễn Huỳnh Tuấn Anh và Trần Bình An")
st.caption("Giảng viên hướng dẫn: ThS. Bùi Tiến Đức")
st.caption("Lớp Học máy và ứng dụng : ")




st.markdown(
    """
    ### Thông tin liên hệ
    - Email: 2100010703@nttu.edu.vn hoặc 2100011226@nttu.edu.vn
    - Lấy source code tại [đây](https://discuss.streamlit.io)
    """
)
