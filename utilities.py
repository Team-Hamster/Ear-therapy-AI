import cv2
import numpy as np
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import os
def load_data(single_img=True, single_img_path='give a path please'):
    if single_img:
        print(f"이미지 경로: {os.path.abspath(single_img_path)}")

        # 절대 경로로 이미지 로드 시도
        img = cv2.imread(os.path.abspath(single_img_path))
    
        if img is None:
            print(f"이미지를 로드할 수 없습니다: {single_img_path}")
            return None, None

        # 이미지를 224x224로 리사이즈
        img = cv2.resize(img, (224, 224))

        # 리사이즈된 이미지를 저장 (필요시)
        cv2.imwrite(single_img_path, img)  # 리사이즈된 이미지 저장 경로

        # 리사이즈된 이미지를 불러와서 모델 입력 형식으로 변환
        img = image.load_img(single_img_path)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # 싱글 이미지에는 라벨이 없으므로 y=None 반환
        y = None
        return x, y

    # single_img=False일 때의 로직은 포함되지 않았음 (여기서는 싱글 이미지 처리만)
