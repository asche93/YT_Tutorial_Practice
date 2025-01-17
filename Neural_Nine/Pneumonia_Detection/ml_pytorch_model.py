"""
Title: Full Machine Learning Project: Train & Deploy a Pneumonia Classifier in PyTorch
Source: NeuralNine YouTube Channel
Author (Original Tutorial): NeuralNine
URL: https://www.youtube.com/watch?v=Gx_I2y3L8is
Date of Implementation: 2025-01-15
Description:
    In this video, we go through a full machine learning project. We train a large PyTorch model on GPUs in the cloud (step 1). Then we deploy it as a serverless endpoint using Docker (step 2) and finally we build a Flask application to interact with it (step 3).

This script is focusing on step 1:
    - Download Kaggle Dataset
    - Setup ML Pytorch model
    - Train preset RESNET18 Deep CNN
"""
import os

from PIL import Image # Python imaging library, for displaying x-ray images

import torch
import torch.nn as nn
import torch.optim as optim # Various optimization algorithms
from torch.utils.data import Dataset, DataLoader 
from torchvision import transforms, models # popular datasets, model architectures, and common image transformations for computer vision

from sklearn.metrics import accuracy_score # Score functions, performance metrics, pairwise metrics and distance computations

# Make the code device-agnostic
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}") # run nvtop in terminal for graphics usages analysis while running

print("Torch available:", torch.cuda.is_available())  
print("GPU name:", torch.cuda.get_device_name(0))  

class PneumoniaDataset(Dataset):

    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths= []
        self.labels = [] 

        # Image sets identified as normal and as pneumonia respectivly, the results we want to predict
        for label in ['NORMAL', 'PNEUMONIA']:
            class_dir = os.path.join(root_dir, label)
            for image_name in os.listdir(class_dir):
                image_path = os.path.join(class_dir, image_name)
                if os.path.isfile(image_path): # avoid .ipynb_checkpoints subfolders
                    self.image_paths.append(image_path)
                    self.labels.append(0 if label == 'NORMAL' else 1)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label

transform = transforms.Compose([
    transforms.Resize((224, 224)), # Input shape defined by RESNET18
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # Preset weights for training
])

train_dataset = PneumoniaDataset(root_dir='data/train/', transform=transform)
test_dataset = PneumoniaDataset(root_dir='data/test/', transform=transform)
val_dataset = PneumoniaDataset(root_dir='data/val/', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, pin_memory=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, pin_memory=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False, pin_memory=True)

# use pretrained model
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)  
# adjust the fully connected layer
model.fc = nn.Linear(model.fc.in_features, 2) # 'NORMAL' or 'PNEUMONIA'
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

num_epochs = 5

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0

    for i, (images, labels) in enumerate(train_loader): # we get 32 at once
        images = images.to(device)
        labels = labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)

        loss = criterion(outputs, labels)
        loss.backward()

        optimizer.step()

        running_loss += loss

        if (i + 1) % 10 == 0:
            print(f"Epoch: {epoch + 1}/{num_epochs}, Step: {i + 1}/{len(train_loader)}, Loss: {loss.item()}")

    print(f"Epoch {epoch + 1}/{num_epochs}, Average Loss: {running_loss / len(train_loader)}")
    
    model.eval()
    val_labels = []
    val_preds = []

    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            val_labels.extend(labels.cpu().numpy())
            val_preds.extend(preds.cpu().numpy())

    val_accuracy = accuracy_score(val_labels, val_preds)
    print("Validation accuracy:", val_accuracy)


model.eval()
test_labels = []
test_preds = []

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, preds = torch.max(outputs, 1)

        test_labels.extend(labels.cpu().numpy())
        test_preds.extend(preds.cpu().numpy())

test_accuracy = accuracy_score(test_labels, test_preds)

print("Test accuracy:", test_accuracy)
print(f"Memory allocated: {torch.cuda.memory_allocated(device) / 1024 ** 2:.2f} MB")
print(f"Memory reserved: {torch.cuda.memory_reserved(device) / 1024 ** 2:.2f} MB")



torch.save(model.state_dict(), 'pneumonia_classifier.pth')







        
        
        