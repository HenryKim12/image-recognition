import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import torch
import torchvision

from torch import nn
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor
from pathlib import Path

import matplotlib.pyplot as plt

class DatasetController():
    def __init__(self):
        pass

    def get_data(self):
        train_data = datasets.Food101(
            root="data", 
            split="train",
            download=True,
            transform=torchvision.transforms.ToTensor(),
            target_transform=None
        )

        test_data = datasets.Food101(
            root="data",
            split="test",
            download=True,
            transform=ToTensor(),
            target_transform=None
        )

    def playground(self):
        print(len(train_data), len(test_data))