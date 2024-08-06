# ActionConceptLearning
Code for Action Concept Learning using LLMs


# Project Description

Objective: Generate action specific commonsense in natural language over given images

Input: Image (currently limited to actions/objects typically found in kitchen/cooking setting)\
Output: Text describing
- actions that are happening in the image and objects that participate in action (e.g. boiling egg)
- pre-conditions for the action happening in the image (e.g. water is a pre-condition for boiling)
- most likely before and after (effects) scenarios (e.g. egg will become solid)

The demo requires using two python notebooks:\
(i) Detectron_demo.ipynb: Takes user specified image, detect objects and extract features from it\
(ii) ActionComet_demo.ipynb: Takes image features and generate inference described above

# Step 1: Detectron_demo.ipynb

- GPU is required to run this script.

- Run cells 1-9 to set up proper environment and define necessary functions.

- Use any sample images from action-comet/action_images/ or upload any image of your choice under this directory and provide appropriate path under 'filename' variable in cell 10

- Run cell 10 to obtain following for your uploaded image (i) detected objects in the image (ii) extracted image features (iii) .json and .pkl files containing image metadata, which are required by the inference module.

# Step 2: ActionCommonsense_demo notebook

- GPU is not required but highly recommended to run this script.

- Run cells 1-4 to set up proper environment.

- Run cell 5 to obtain inference.

# Additional Notes:

- This development is an extension of visualcomet and build upon the code https://github.com/jamespark3922/visual-comet, specifically from the action understanding point of view.   

- For batch experiments, you must download the entire codebase at https://drive.google.com/drive/folders/1xP7IX1CSAzJnj9lbP5-rkNeZYpJ8jM_4?usp=share_link including full feature.zip (5.5GB compressed). Extract the feature.zip inside this folder. Then run:
<code>python scripts/run_generation.py --data_dir /path/to/visualcomet_data/ --model_name_or_path experiments/image_inference-80000-ckpt/ --split train/test/val</code>

- If you are interested in accessing scraped video or audio corresponding to YouCook2 dataset, refer to https://drive.google.com/drive/folders/18JtchtOLM5L3HlA0dkhnTMxY-d9XaCcw?usp=share_link.
