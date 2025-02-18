import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps  # Install pillow instead of PIL

# Streamlit 페이지 설정
st.set_page_config(page_title="고양이 품종 예측", layout="centered")

st.title("🐱 고양이 품종 예측")

# 모델 & 라벨 로드
model = load_model('keras_model.h5', compile=False)
class_names = [line.strip() for line in open('labels.txt', 'r').readlines()]

# 사용자 입력 방식 선택 (카메라 or 파일 업로드)
input_method = st.radio("이미지 입력 방식 선택", ["카메라 사용", "파일 업로드"])

if input_method == "카메라 사용":
    img_file_buffer = st.camera_input("📸 정중앙에 사물을 위치하고 사진을 찍으세요!")
else:
    img_file_buffer = st.file_uploader("📂 이미지 파일 업로드", type=["png", "jpg", "jpeg"])

# 이미지 입력이 있을 경우
if img_file_buffer is not None:
    # 이미지 불러오기 및 전처리
    image = Image.open(img_file_buffer).convert('RGB')
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

    # 이미지 → Numpy 변환 및 정규화
    image_array = np.asarray(image).astype(np.float32)
    normalized_image_array = (image_array / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # 모델 예측 수행
    prediction = model.predict(data)[0]
    
    # 예측 결과 정렬 (확률 높은 순서)
    results = sorted(zip(class_names, prediction), key=lambda x: x[1], reverse=True)

    # 🏆 가장 높은 확률의 품종 출력
    best_class, best_prob = results[0]
    st.subheader(f"🏆 가장 높은 확률: **{best_class}** ({best_prob * 100:.2f}%)")

    # 📊 전체 품종별 확률 표시 (Progress Bar)
    st.subheader("📊 전체 예측 결과")
    for class_name, prob in results:
        st.markdown(f"**{class_name}**: {prob * 100:.2f}%")
        st.progress(int(prob * 100))  # 확률을 퍼센트 바 형태로 출력