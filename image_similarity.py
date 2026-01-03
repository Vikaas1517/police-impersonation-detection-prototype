import imagehash
from PIL import Image
import os

def compute_image_similarity(img1_path: str, img2_path: str) -> float:
    """
    Computes perceptual hash similarity between two images.
    Returns score between 0 and 1.
    """
    if not os.path.exists(img1_path) or not os.path.exists(img2_path):
        return 0.0

    img1_path = os.path.abspath(img1_path)
    img2_path = os.path.abspath(img2_path)

    hash1 = imagehash.phash(Image.open(img1_path))
    hash2 = imagehash.phash(Image.open(img2_path))

    return 1 - (hash1 - hash2) / 64
