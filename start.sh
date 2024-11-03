#!/bin/bash

# Kích hoạt môi trường Conda
source activate venv

# Tạo thư mục model nếu chưa tồn tại
mkdir -p model

# Chạy recommendation.py
python recommendation.py

# Sau đó chạy ứng dụng Streamlit
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
