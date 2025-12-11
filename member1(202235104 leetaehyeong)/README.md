# 이미지 워터마크 프로그램 (Image Watermark Tool)

이 프로젝트는 OpenCV를 이용하여 **이미지에 텍스트 워터마크를 자동으로 삽입**하는 간단한 오픈소스 도구입니다.  
텍스트 투명도 조절, 위치 계산, 반투명 박스 생성 등 기본적인 워터마크 기능을 제공합니다.

---

## 데모 예시

워터마크 적용 전 이미지
![before](./fall.jpg)

워터마크 적용 후 이미지
![after](./output_watermarked.jpg)

---

## 사용한 패키지 및 버전

프로그램 실행에는 아래 패키지가 필요합니다:

- `opencv-python 4.x`
- `numpy 1.x` (OpenCV 내부적으로 사용)

> 설치가 필요하다면 아래 명령어를 실행하세요:

```bash
pip install -r requirements.txt

## 실행 방법

1. `member1` 폴더 안에 다음 파일을 준비합니다:
   - `watermark.py`
   - 워터마크를 넣고 싶은 이미지 파일 → **input.jpg**

2. 필요한 패키지를 설치합니다:

    pip install -r requirements.txt

3. 터미널 또는 VS Code에서 `member1` 폴더로 이동하여 실행합니다:

    python watermark.py

4. 실행 후 생성되는 파일:
   - `output_watermarked.jpg` : 워터마크가 적용된 최종 이미지

5. 실행 중 표시되는 이미지 창은
   **아무 키나 누르면 자동으로 닫히고 프로그램이 종료됩니다.**

---

##내부 동작 방식

이 워터마크 프로그램은 다음 단계로 실행됩니다:

1. **이미지 불러오기**
   - OpenCV를 사용해 `input.jpg` 파일을 읽음
   - 파일이 없으면 오류 출력 후 종료

2. **이미지 크기 축소**
   - 화면에 잘 보이도록 원본 크기의 30%로 resize
   - 너무 큰 이미지를 자동으로 줄여 처리 안정성 향상

3. **워터마크 텍스트 정보 계산**
   - 글자 크기, 너비, 높이, baseline 값을 계산
   - 텍스트가 이미지 오른쪽 아래에 자연스럽게 배치되도록 자동 위치 계산

4. **반투명 박스(Overlay) 생성**
   - 텍스트 가독성을 높이기 위해 검정색 반투명 박스를 생성
   - OpenCV `rectangle()` 사용

5. **텍스트 워터마크 삽입**
   - `cv2.putText()`로 overlay 위에 텍스트 삽입
   - 기본 글씨색: 흰색, 기본 글씨 굵기: 2

6. **이미지와 overlay 합성**
   - `cv2.addWeighted()`로 overlay와 원본 이미지 합성
   - `alpha` 값으로 투명도 조절 가능 (기본값: 0.6)

7. **결과 저장 및 출력**
   - 최종 이미지를 `output_watermarked.jpg`로 저장
   - 화면에 이미지 표시 후 키 입력 시 종료

---


```
