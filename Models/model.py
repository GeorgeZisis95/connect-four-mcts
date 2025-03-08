import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvModel(nn.Module):

    def __init__(self, input_channels, kernels, total_actions):
        super(ConvModel, self).__init__()
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=kernels, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=kernels, padding=1)

        self.fc1 = nn.Linear(64 * 4 * 4, 128)
        self.fc2 = nn.Linear(128, total_actions)
        self.fc3 = nn.Linear(128, 1)
    
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = torch.flatten(x, start_dim=1)
        x = F.relu(self.fc1(x))
        policy = torch.softmax(self.fc2(x), axis=1)
        value = torch.tanh(self.fc3(x))
        return policy, value