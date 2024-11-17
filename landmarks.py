import matplotlib.pyplot as plt
import cv2

def put_landmarks(i, pred, img_path, part, img_out_path):

    img_original = plt.imread(img_path)

    plt.imshow(img_original)
    plt.axis('off') 

    for j in part:  
        plt.scatter([pred[j]], [pred[j+55]], c='red', s=10)  

    plt.savefig(img_out_path, bbox_inches='tight', pad_inches=0)
    plt.close()

# landmarks.py
이 코드는 이미지에 랜드마크를 시각적으로 표시하는 함수입니다. 이미지에 예측된 랜드마크 점들을 그려서 저장하는 기능을 수행하며, 이 과정을 통해 랜드마크 예측 결과를 시각적으로 확인할 수 있습니다.

코드 설명:
1. 필요한 라이브러리 임포트
import matplotlib.pyplot as plt: Matplotlib을 사용하여 이미지를 불러오고, 랜드마크 점을 이미지에 표시합니다.
import cv2: OpenCV를 사용해 이미지를 처리할 수 있지만, 이 코드에서는 OpenCV 대신 Matplotlib을 주로 사용하여 이미지를 시각화하고 있습니다.
2. 함수 정의: put_landmarks
이 함수는 이미지에 랜드마크를 표시하고, 결과 이미지를 파일로 저장하는 역할을 합니다.

매개변수:
i: 특정 이미지의 인덱스 또는 번호를 나타낼 수 있는 값입니다. 현재 코드에서는 사용되지 않고 있지만, 함수 호출 시 사용자의 요구에 맞게 전달됩니다.
pred: 예측된 랜드마크 좌표 배열입니다. 이 배열에는 110개의 값이 있을 것으로 예상됩니다. 첫 55개는 X 좌표, 그 다음 55개는 Y 좌표입니다.
img_path: 원본 이미지 파일 경로입니다. 이 경로에서 이미지를 불러옵니다.
part: 랜드마크를 그릴 때 사용할 랜드마크 포인트들의 인덱스를 포함하는 리스트입니다. 예를 들어, [0, 1, 2, ...]와 같이 일부 또는 모든 랜드마크 점을 나타냅니다.
img_out_path: 처리 후 이미지를 저장할 경로입니다.
3. 원본 이미지 불러오기:
python
코드 복사
img_original = plt.imread(img_path)
img_path 경로에 있는 이미지를 불러옵니다. 이 이미지는 원본 귀 이미지입니다.
4. 이미지 표시 및 축 제거:
python
코드 복사
plt.imshow(img_original)
plt.axis('off')
불러온 이미지를 Matplotlib을 사용해 화면에 표시합니다.
plt.axis('off')는 이미지 주위에 불필요한 축과 눈금을 제거하여, 오로지 이미지만 보이도록 설정합니다.
5. 랜드마크 점 표시:
python
코드 복사
for j in part:
    plt.scatter([pred[j]], [pred[j+55]], c='red', s=10)
part 리스트에 포함된 랜드마크 포인트 인덱스를 사용하여, 해당 위치에 점을 찍습니다.
pred[j]: 예측된 X 좌표를 나타냅니다.
pred[j + 55]: 예측된 Y 좌표를 나타냅니다. Y 좌표는 배열에서 X 좌표 뒤에 위치해 있으므로, 인덱스 55를 더해 줍니다.
plt.scatter: 각 랜드마크 포인트를 이미지에 빨간색 점(c='red')으로 표시합니다. 점의 크기는 s=10으로 설정되었습니다.
6. 결과 이미지 저장:
python
코드 복사
plt.savefig(img_out_path, bbox_inches='tight', pad_inches=0)
img_out_path 경로에 결과 이미지를 저장합니다.
bbox_inches='tight': 이미지에 불필요한 여백을 제거하여 깔끔하게 저장합니다.
pad_inches=0: 이미지 주위에 패딩(여백)을 추가하지 않도록 설정합니다.
7. 그래프 닫기:
python
코드 복사
plt.close()
plt.close()를 통해 현재 사용한 플롯(그래프)을 닫습니다. 이는 메모리 누수를 방지하고, 여러 번 반복할 때 불필요한 리소스 사용을 줄여줍니다.
요약:
이 함수는 주어진 이미지를 불러와, 그 위에 예측된 랜드마크를 빨간색 점으로 표시한 후, 결과 이미지를 저장하는 역할을 합니다. 귀 랜드마크 예측 모델을 평가할 때, 시각적으로 결과를 확인하기 위한 용도로 사용할 수 있습니다.