"""ML environment and CUDA test script"""

import torch
import torch.nn as nn
import torch.optim as optim

# Debug-Ausgaben zur Überprüfung der GPU-Verwendung
print("Checking CUDA availability...")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Using device: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")

# Select device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Einfaches Modell
model = nn.Linear(10, 2).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Dummy-Daten
inputs = torch.randn(32, 10).to(device)  # Batch size 32, 10 Features
labels = torch.randint(0, 2, (32,)).to(device)  # Binary Labels

# Training Loop
print("Starting training loop...")
model.train()
for epoch in range(5):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

print("Training completed.")