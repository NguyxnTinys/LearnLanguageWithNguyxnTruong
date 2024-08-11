import streamlit as st
import pandas as pd
from PIL import Image

# Thay đổi thông tin đăng nhập ở đây
USERNAME = '1'
PASSWORD = '1'

def load_data(file_path):
    """Tải dữ liệu từ file Excel"""
    return pd.read_excel(file_path)

def process_image(image_path, output_size=(300, 300)):
    """
    Xử lý ảnh bằng cách cắt một phần hình vuông từ tâm của ảnh.
    
    Args:
        image_path (str): Đường dẫn đến ảnh gốc.
        output_size (tuple): Kích thước của khung hình vuông cần cắt (width, height).
    
    Returns:
        Image: Ảnh đã xử lý dưới dạng Image để sử dụng trong Streamlit.
    """
    # Mở ảnh
    image = Image.open(image_path).convert('RGBA')
    width, height = image.size

    # Tính toán kích thước hình vuông và tọa độ để cắt
    square_size = min(width, height)
    left = (width - square_size) / 2
    top = (height - square_size) / 2
    right = (width + square_size) / 2
    bottom = (height + square_size) / 2

    # Cắt hình vuông từ tâm
    cropped_image = image.crop((left, top, right, bottom))

    # Resize ảnh để phù hợp với kích thước đầu ra
    cropped_image = cropped_image.resize(output_size, Image.LANCZOS)

    return cropped_image

def login():
    st.markdown("""
    <style>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .login-box {
        width: 400px;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Tạo hai cột cho logo và form đăng nhập
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Hiển thị logo người dùng
        logo_image = process_image('images/Logo_user/user.png')
        st.image(logo_image, use_column_width=False)
    
    with col2:
        # Tạo container cho phần đăng nhập và đặt màu nền xám
        with st.container():
            st.write("")
            st.markdown(
                """
                <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
                """,
                unsafe_allow_html=True
            )
            st.write("###")  # Khoảng cách trên cùng
            
            username = st.text_input("Tên người dùng", key="username")
            password = st.text_input("Mật khẩu", type="password", key="password")
            
            st.write("")  # Khoảng cách giữa các trường và nút
            
            if st.button("Đăng Nhập"):
                if username == USERNAME and password == PASSWORD:
                    st.session_state.logged_in = True
                else:
                    st.error("Tên người dùng hoặc mật khẩu không đúng")
            
            st.markdown("</div>", unsafe_allow_html=True)

def main_app():
    st.title("Ứng Dụng Xem Dữ Liệu Excel")
    
    # Đường dẫn đầy đủ đến file Excel
    file_path = 'access/Last Data/Data.xlsx'
    
    # Tải dữ liệu từ file Excel
    df = load_data(file_path)
    
    # Hiển thị bảng dữ liệu
    st.dataframe(df)
    
    # Thay đổi ngôn ngữ
    language = st.selectbox("Ngôn ngữ", ["Tiếng Việt", "English", "中文"])
    st.info(f"Ngôn ngữ đã thay đổi thành: {language}")

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()
    else:
        login()

if __name__ == "__main__":
    main()