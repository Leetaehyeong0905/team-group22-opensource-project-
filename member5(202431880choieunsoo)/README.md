# Shape Detection Dashboard

이미지 속에서 원(Circles)과 선(Lines)을 자동으로 검출하고 시각화하는 OpenCV 기반 웹 애플리케이션입니다.  
Flask 웹 프레임워크를 사용하여 브라우저에서 간편하게 테스트할 수 있도록 구현했습니다.

본 프로젝트는 수업 시간에 배운 엣지 검출(Canny), 허프 변환(Hough Transform) 등을 실제 이미지 분석에 적용해보고,  
이를 웹 UI로 확장하여 사용자 친화적인 대시보드를 만든 확장 과제입니다.

---

# 프로젝트 개요

사용자가 이미지를 업로드하면 다음 과정을 수행합니다:

1. Grayscale 변환
2. Gaussian Blur(노이즈 제거)
3. Canny Edge Detection
4. HoughLinesP(선 검출) & HoughCircles(원 검출) 적용
5. 검출된 도형을 원본 이미지 위에 색상으로 표시
6. 검출된 원/선의 개수를 대시보드에서 숫자로 표시

또한, 업로드된 이미지의 크기가 너무 클 경우 자동으로 축소하여  
OpenCV 처리 속도를 크게 개선하는 기능도 포함되어 있습니다.

---

# 데모 영상

> https://drive.google.com/file/d/1Jcaj_pnw_KKCmTm7DPbUz8BKnpQn681z/view?usp=drive_link

# 검출 예시 이미지

입력 이미지

> https://drive.google.com/file/d/1vb5eIXZYv-Sq2rhHB5OVOL0Q46yRfnfy/view?usp=drive_link

결과 이미지

> https://drive.google.com/file/d/1kcXUpIJiKG1_bow0J7S2FLkZ82yXwBQ9/view?usp=drive_link

---

# 사용한 패키지 & 버전

아래는 `requirements.txt` 내용과 동일하도록 작성되어 있습니다.

```txt
flask==3.1.2
opencv-python==4.12.0.88
numpy==2.2.0
```

-설치 명령어
pip install -r requirements.txt

# 실행 방법

1. 가상환경 생성 및 활성화 (선택 사항)
   python -m venv venv
   source venv/bin/activate # Mac / Linux
   venv\Scripts\activate # Windows

2. 필요한 패키지 설치
   pip install -r requirements.txt

3. Flask 웹 서버 실행
   python main.py

4. 브라우저에서 접속
   http://127.0.0.1:5000

# 참고 자료

본 프로젝트는 아래 자료들을 참고하여 구현되었습니다.

OpenCV 공식 문서
https://docs.opencv.org/

Flask 공식 문서
https://flask.palletsprojects.com/

Hough Transform 참고 블로그
https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html

UI/UX 디자인 참고
Dribbble / Pinterest 디자인 레이아웃
