from ultralytics import YOLO


def predictImage(Source):
    model = YOLO('middleware/visianario_v3.pt')

    results = model.predict(Source, save=False, conf=0.2)

    output = []
    for box in results[0].boxes:
        class_id = box.cls[0].item()
        output.append(results[0].names[class_id])

    return output