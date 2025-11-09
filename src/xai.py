import torch
import torch.nn.functional as F

def predict_image(tensor_image, device):
    model = torch.load("models/vet_model.pth", map_location=device)
    model.eval()
    tensor_image = tensor_image.to(device)
    
    with torch.no_grad():
        outputs = model(tensor_image)
        _, pred_class_idx = torch.max(outputs, 1)
    
    classes = ["Dog_Ringworm", "Dog_Mange", "Cat_Ringworm", "Cat_Mange"]
    prediction = classes[pred_class_idx.item()]
    
    return prediction, pred_class_idx.item(), model