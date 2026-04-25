from flask import Flask, render_template, Response
import cv2
import time

app = Flask(__name__, template_folder='.')
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # read camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Optional: resize frame to reduce load (e.g., 640x480)
            frame = cv2.resize(frame, (640, 480))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            # Limit to ~30 FPS to prevent CPU overload
            time.sleep(0.033)


@app.route('/')
def index():
    # return render_template('index.html')
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        camera.release()
    
    