import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def get_dataloaders(data_dir, batch_size=32, img_size=224):
    # --- Augmentation สำหรับ Train ---
    train_transforms = transforms.Compose([
        transforms.Resize((img_size,img_size)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor()
    ])

    # --- สำหรับ Validation / Test ---
    val_transforms = transforms.Compose([
        transforms.Resize((img_size,img_size)),
        transforms.ToTensor()
    ])

    # --- โหลด Dataset ---
    train_dataset = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=train_transforms)
    val_dataset   = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=val_transforms)
    test_dataset  = datasets.ImageFolder(os.path.join(data_dir, "test"), transform=val_transforms)

    # --- DataLoader ---
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader   = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    test_loader  = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, val_loader, test_loader

# --- ทดสอบ Loader ---
if __name__ == "__main":
    train_loader, val_loader, test_loader = get_dataloaders("data", batch_size=16)
    print(f"Train batches: {len(train_loader)}")
    print(f"Validation batches: {len(val_loader)}")
    print(f"Test batches: {len(test_loader)}")