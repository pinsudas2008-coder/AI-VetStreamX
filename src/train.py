import torch
from torch import nn, optim
from torchvision import models
from dataset import get_dataloaders

def train_model(data_dir, model_path='models/vet_model.pth', epochs=5, lr=1e-4):
    train_loader, val_loader, _ = get_dataloaders(data_dir, batch_size=16)  # ใช้ DataLoader จาก dataset.py เลย

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    model.fc = nn.Linear(model.fc.in_features, 4)  # 4 classes
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        running_loss = 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")

    torch.save(model.state_dict(), model_path)
    print("Training complete and model saved!")

if __name__ == "__main__":
    train_model('data')