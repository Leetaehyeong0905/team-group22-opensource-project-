# 이미지 워터마크 프로그램 (OpenCV 사용)

import cv2  # OpenCV 라이브러리를 가져온다 (이미지 읽기/쓰기, 그리기 등)

def add_text_watermark(image, text, alpha=0.5):
    """
    이미지에 텍스트 워터마크를 넣는 함수
    image : 원본 이미지 (numpy 배열)
    text  : 넣고 싶은 문자열
    alpha : 워터마크 투명도 (0.0 ~ 1.0, 클수록 진하게)
    """
    overlay = image.copy()  # 원본 이미지를 복사해서 overlay(겹칠 이미지)를 만든다
    output = image.copy()   # 결과를 저장할 output 이미지도 하나 더 복사한다

    h, w, _ = image.shape   # 이미지의 세로(h), 가로(w), 채널 수(_)를 가져온다

    font = cv2.FONT_HERSHEY_SIMPLEX  # 사용할 글꼴(폰트) 종류를 정한다
    scale = 1.0                      # 글자 크기 배율을 정한다
    color = (255, 255, 255)          # 글자 색을 정한다 (B, G, R → 흰색)
    thickness = 2                    # 글자 선 굵기를 정한다

    # 글자 크기와 박스 크기를 미리 계산해서 위치를 잡는다
    (text_w, text_h), baseline = cv2.getTextSize(text, font, scale, thickness)  # 글자의 폭/높이 계산
    x = w - text_w - 20  # 오른쪽 아래에 놓기 위해 x 좌표를 계산 (오른쪽에서 20픽셀 안쪽)
    y = h - baseline - 20  # 아래쪽에서 20픽셀 위쪽에 y 좌표를 계산한다

    # 먼저 검은색 반투명 박스를 그려서 글자가 잘 보이게 만든다
    box_padding = 10                                         # 글자 주변 여백을 얼마나 줄지 정한다
    box_x1 = x - box_padding                                 # 박스의 왼쪽 위 x 좌표
    box_y1 = y - text_h - box_padding                        # 박스의 왼쪽 위 y 좌표
    box_x2 = x + text_w + box_padding                        # 박스의 오른쪽 아래 x 좌표
    box_y2 = y + box_padding                                 # 박스의 오른쪽 아래 y 좌표
    cv2.rectangle(overlay, (box_x1, box_y1), (box_x2, box_y2), (0, 0, 0), -1)  # overlay에 검은색 채운 박스 그리기

    # 박스 위에 흰색 텍스트를 쓴다
    cv2.putText(overlay, text, (x, y), font, scale, color, thickness, cv2.LINE_AA)  # overlay에 글자를 그린다

    # overlay(박스+글자)와 원본 이미지를 섞어서 부드럽게 만든다
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)  # alpha 비율로 두 이미지를 합친다

    return output  # 워터마크가 들어간 이미지를 반환한다


def main():
    input_path = "fall.jpg"  # 워터마크를 넣고 싶은 원본 이미지 파일 이름
    output_path = "output_watermarked.jpg"  # 결과 이미지를 저장할 파일 이름

    # 이미지 파일을 읽어온다
    image = cv2.imread(input_path)  # 파일에서 이미지를 읽는다
    if image is None:  # 이미지 읽기에 실패하면
        print(f"이미지를 찾을 수 없습니다: {input_path}")  # 에러 메시지를 출력하고
        return  # 프로그램을 종료한다
    
    scale = 0.3     #사진의 크기가 너무 커서 줄인다
    image = cv2.resize(image, None, fx=scale, fy=scale) 

    # 워터마크에 사용할 텍스트를 정한다
    watermark_text = "Taehyeong's OSS Project"  # 이미지에 넣을 문구

    # 워터마크를 적용한다
    result = add_text_watermark(image, watermark_text, alpha=0.6)  # 함수 호출해서 새 이미지 생성

    # 결과 이미지를 파일로 저장한다
    cv2.imwrite(output_path, result)  # 결과 이미지를 지정한 파일 이름으로 저장한다

    # 화면에도 결과를 보여준다
    cv2.imshow("Watermarked Image", result)  # 윈도우 창에 결과 이미지를 띄운다
    cv2.waitKey(0)  # 아무 키나 누를 때까지 기다린다
    cv2.destroyAllWindows()  # 모든 이미지 창을 닫는다

    print(f"워터마크 이미지가 저장되었습니다: {output_path}")  # 완료 메시지를 출력한다

if __name__ == "__main__":  # 이 파일을 직접 실행했을 때만 main()을 실행하도록 한다
    main()  # main 함수를 호출해서 프로그램을 시작한다
