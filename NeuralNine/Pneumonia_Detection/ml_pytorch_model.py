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
from torchvision import transforms, model # popular datasets, model architectures, and common image transformations for computer vision

from sklearn.metrics import accuarcy_score # Score functions, performance metrics, pairwise metrics and distance computations

# Make the code device-agnostic
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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
                self.image_paths.append(os.path.join(class_dir, image_name))
                self.labels.append(0 if label == 'NORMAL' else 1)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_path[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label

transform = transforms.Compose([
    transforms.Resize((224),(224)), # Input shape defined by RESNET18
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]) # Preset weights for training
])





        
        