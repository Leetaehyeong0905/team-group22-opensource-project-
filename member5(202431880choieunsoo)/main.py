import os
import uuid

import cv2
import numpy as np
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join("static", "uploads")
RESULT_FOLDER = os.path.join("static", "results")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            return render_template("index.html", error="이미지 파일을 선택해주세요.")

        ext = os.path.splitext(file.filename)[1]
        img_id = uuid.uuid4().hex
        upload_filename = f"{img_id}{ext}"
        upload_path = os.path.join(UPLOAD_FOLDER, upload_filename)

        file.save(upload_path)

        img = cv2.imread(upload_path)
        if img is None:
            return render_template("index.html", error="이미지를 읽는 데 실패했습니다.")
       
        max_size = 600  
        h, w = img.shape[:2]
        scale = min(max_size / h, max_size / w, 1.0)

        if scale < 1.0:
            new_w = int(w * scale)
            new_h = int(h * scale)
            img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 50, 150, apertureSize=3)

        # 1. HoughLinesP
        line_count = 0
        linesP = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi / 180,
            threshold=100,
            minLineLength=50,
            maxLineGap=10,
        )

        if linesP is not None:
            for line in linesP:
                x1, y1, x2, y2 = line[0]
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                line_count += 1

        # 2. HoughCircles
        circle_count = 0
        h, w = blur.shape[:2]
        min_dist = min(h, w) // 8  

        circles = cv2.HoughCircles(
            blur,
            cv2.HOUGH_GRADIENT,
            dp=1.2,          
            minDist=min_dist, 
            param1=120,      
            param2=100,       
            minRadius=50,     
            maxRadius=0,    
        )
    
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for c in circles[0, :]:
                x, y, r = c
                cv2.circle(img, (x, y), r, (255, 0, 0), 2)
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
                circle_count += 1

        result_filename = f"{img_id}_result{ext}"
        result_path = os.path.join(RESULT_FOLDER, result_filename)
        cv2.imwrite(result_path, img)

        result_url = url_for("static", filename=f"results/{result_filename}")
        original_url = url_for("static", filename=f"uploads/{upload_filename}")

        return render_template(
            "index.html",
            result_image=result_url,
            original_image=original_url,
            circle_count=circle_count,
            line_count=line_count,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
