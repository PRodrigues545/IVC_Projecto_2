import cv2
import object_detection

#captura da camara
cap = cv2.VideoCapture()

#loop da camara
def camara_loop():
    if not cap.isOpened():
        cap.open(0)
        _, image = cap.read()
    else:
        ret, image = cap.read()
        if not ret:
            print("Error")
        else:
            image = image[:, ::-1, :]  #inverter camara
            cv2.imshow("Image", image)
            window_size = cv2.getWindowImageRect("Image")

            center = object_detection.object_detection(image)

            image_out = image.copy()

            if center is not None:
                center_x = center[0]
                cv2.circle(image_out, center=center, radius=3, color=(0, 255, 0), thickness=-1)
                cv2.imshow("Result", image_out)
                return center_x
