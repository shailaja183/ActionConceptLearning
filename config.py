import os
USE_IMAGENET_PRETRAINED = False # otherwise use detectron, but that doesnt seem to work?!?

# Change these to match where your annotations and images are
VCR_IMAGES_DIR = '/content/drive/MyDrive/action-commonsense/action_images'# os.environ['VCR_PARENT_DIR']
if not os.path.exists(VCR_IMAGES_DIR):
    raise ValueError("Update config.py with where you saved images to.")

VCR_FEATURES_DIR = '/content/drive/MyDrive/action-commonsense/action_features'