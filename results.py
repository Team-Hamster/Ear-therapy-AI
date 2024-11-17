import argparse
from my_CNN_model import load_current_model
from utilities import load_data
from landmarks import put_landmarks
from keras.models import load_model
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# 증상에 따른 랜드마크 인덱스
symptom_landmarks = {
    '감기': [35, 36, 54],
    '스트레스': [47, 49],
    '열': [4, 5, 6],
    '어지럼증': [41, 15],
    '두통': [41, 42],
    '집중력': [41, 34],
    '코피': [36, 41, 44],
    '생리통': [25, 26],
    '빈뇨': [47, 48, 49, 42]
}

def main(single_img, img_path, symptom,img_out_path):

    model = load_model('my_model.h5')

    X, Y = load_data(single_img=single_img, single_img_path=img_path)  
  
    for i in range(len(X)):
        temp = X[i]
        temp = temp[None, :]  # 모델 입력에 맞게 차원 조정
        prediction = model.predict(temp)  # 예측

        # 예측 값을 이미지 크기(224)에 맞게 조정
        for p in range(len(prediction[0])):     
            prediction[0][p] = int(prediction[0][p] * 224)

        # 랜드마크를 이미지에 추가
        put_landmarks(i, prediction[0], img_path, symptom_landmarks[symptom],img_out_path)

if __name__ == "__main__":
    # argparse 설정
    parser = argparse.ArgumentParser(description='Ear Landmark Detection')

    # 명령줄 인자 추가
    parser.add_argument('--single_img', type=bool, default=True, help='단일 이미지를 처리할지 여부 (True/False)')
    # 본인의 이미지 파일이 존재하는 위치 img_path, 결과물이 나올 위치 out_path
    parser.add_argument('--img_path', type=str, default=r'D:\Kmong\ear\ear-landmark-detection-with-CNN\images\test_12.png', help='이미지 파일 경로')
    parser.add_argument('--out_path', type=str, default=r'D:\Kmong\ear\ear-landmark-detection-with-CNN\images\result_12.png', help='이미지 파일 경로')
    parser.add_argument('--symptom', type=str, choices=symptom_landmarks.keys(), default='빈뇨', help='증상에 따른 랜드마크 (감기, 스트레스, 열, 어지럼증, 두통 등)')

    # 명령줄 인자를 파싱
    args = parser.parse_args()

    # 파싱된 인자를 main 함수로 전달
    main(args.single_img, args.img_path, args.symptom,args.out_path)
