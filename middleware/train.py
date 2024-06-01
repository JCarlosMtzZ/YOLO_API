from ultralytics import YOLO

def main():
    # Cargar el modelo preentrenado
    model = YOLO("yolov8s.pt")  # .pt te da acceso a un modelo preentrenado

    # Entrenar el modelo con el dataset personalizado (OIDv7)
    model.train(data='oidv4.yaml', imgsz=720, epochs=50, batch=-1, plots=True, device=0)

if __name__ == '__main__':
    main()