# Ear Therapy - AI model

이 프로젝트는 Python 3.6.8, TensorFlow 1.14, Keras 2.2.4, OpenCV를 사용하여 구성되었습니다. 머신러닝 및 이미지 처리 기능을 포함하고 있습니다.

## 설치 방법

필요한 패키지를 설치하려면 `requirements.txt` 파일을 사용하여 `pip`로 설치할 수 있습니다.

### 설치 단계:


1. 가상 환경을 생성합니다 (선택 사항):

    ```bash
    python -m venv venv python==3.6.8
    source venv/bin/activate  # Linux/macOS용
    venv\Scripts\activate  # Windows용
    ```

2. 의존성 패키지를 설치합니다:

    ```bash
    pip install -r requirements.txt
    ```

`conda`를 사용하는 경우, OpenCV를 다음 명령어로 설치할 수 있습니다:

```bash
conda install -c conda-forge opencv



3. 실행 방법

python results.py --single_img=True --img_path="<입력 이미지 경로>" --out_path="<출력 이미지 경로>" --symptom="<증상>"

예시 
python results.py --single_img=True --img_path="D:/Kmong/ear/ear-landmark-detection-with-CNN/images/test_13.png" --out_path="D:/Kmong/ear/ear-landmark-detection-with-CNN/images/result_13.png" --symptom="빈뇨"

4. 증상 소개 
감기
스트레스
열
어지럼증
두통
집중력
코피
생리통
빈뇨
