# 고양이 품종 예측 (Cat Breed Prediction)  /ᐠ. ｡.ᐟ\ᵐᵉᵒʷˎˊ˗

## https://meowmeowcat.streamlit.app/

![Image](https://github.com/user-attachments/assets/a1b069a7-0530-49dd-bbbc-1a2d70e9eebb)

*** 

이 프로젝트는 사용자가 입력한 고양이 사진을 기반으로 고양이 품종을 예측하는 웹 애플리케이션입니다. 사용자는 카메라 또는 이미지 파일을 업로드하여 모델을 통해 고양이 품종을 예측할 수 있습니다.

*** 

## 기능 💻

- 사용자가 고양이 사진을 카메라로 찍거나 파일로 업로드하여 모델을 통해 고양이 품종을 예측
- 예측된 품종의 확률을 시각적으로 표시 (가장 높은 확률을 가진 품종, 전체 품종별 확률)
- 품종 예측 결과를 Progress Bar 형태로 표시

|테스트 사진|작동 예시|
|----|----|
|![Image](https://github.com/user-attachments/assets/d1ec1f8d-8bd7-4a82-9be4-f410c32aa005)|![Image](https://github.com/user-attachments/assets/a1b069a7-0530-49dd-bbbc-1a2d70e9eebb)|

***

## 사용 기술 🔧

![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)  ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)	![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

***

## 파일 구조 📂

        .
        ├── keras_model.h5             # 고양이 품종 예측을 위한 학습된 모델 파일
        ├── labels.txt                # 고양이 품종 레이블 (각각의 품종 이름이 한 줄씩 적혀 있음)
        ├── app.py                    # Streamlit 웹 애플리케이션 코드 (이 파일)
        └── requirements.txt           # 필요한 라이브러리 목록

***

## 참고 사항 🔊

- 이미지를 업로드하거나 카메라로 촬영할 때, 품종 예측의 정확도는 모델의 학습 상태에 따라 달라질 수 있습니다.
