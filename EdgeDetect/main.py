import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not found or not accessible.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_frame, threshold1=100, threshold2=200)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        combined = np.hstack((frame, edges_bgr))
        cv2.imshow("Orijinal Goruntu (sag) / Ayiklanmis Goruntu (sol)", combined)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
