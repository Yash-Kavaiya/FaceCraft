import torch
import numpy as np
from PIL import Image

class FaceGenerator:
    def __init__(self):
        # Initialize StyleGAN2 model
        self.model = torch.hub.load('nvidia/StyleGAN2-ADA-PyTorch', 'synthesize')
        
    def generate_face(self, seed=None):
        if seed is None:
            seed = np.random.randint(0, 999999)
        # Generate random latent vector
        z = torch.randn(1, 512).cuda()
        # Generate image
        image = self.model(z)
        return image[0]
