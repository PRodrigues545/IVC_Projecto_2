from ultralytics import YOLO
import cv2


model = YOLO("yolov8n.pt")

def object_detection(image):
    results = model(image, verbose=False)

    image_objects = image.copy()
    center = None
    objects = results[0]
    for object in objects:
        box = object.boxes.data[0]
        pt1 = (int(box[0]), int(box[1]))
        pt2 = (int(box[2]), int(box[3]))
        confidence = box[4]
        class_id = int(box[5])
        if class_id == 67 and confidence > 0.5:
            cv2.rectangle(img=image_objects, pt1=pt1, pt2=pt2, color=(255, 0, 0), thickness=2)
            center_x = int((pt1[0] + pt2[0]) / 2)
            center_y = int((pt1[1] + pt2[1]) / 2)
            center = (center_x, center_y)

    cv2.imshow(winname="Image", mat=image_objects)
    return center
