```python
import torch

class PyTorchModel:
    def __init__(self):
        self.model = None
    
    def build_model(self):
        # Code to build the PyTorch model
        self.model = torch.nn.Sequential(
            torch.nn.Linear(10, 20),
            torch.nn.ReLU(),
            torch.nn.Linear(20, 1)
        )
    
    def train_model(self, data):
        # Code to train the PyTorch model
        pass
    
    def predict(self, input):
        # Code to make predictions using the PyTorch model
        pass
```
