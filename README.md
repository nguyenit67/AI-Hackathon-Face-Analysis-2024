# Guideline

This repo includes 3 main parts: using deepface to output age, gender, race, emotion and 2 models training from scratch are masked detection model and skintone detection model. All code are trained and evaluated on Kaggle with all provided data uploaded there.

## DeepFace
Running `experiment.ipynb` notebook on Kaggle with public and private test data to get multiple backend detectors output for age, gender, race, emotion.

## Skintone detection
In folder `skinton_detection`, run the `skintone_analysis.ipynb` notebook to train and predict skintone feature for public and private test data. A model `skin_classify_150epoch.keras` will be saved to Kaggle working directory `/kaggle/working` after training, which can be used for inference and fine-tuning later.

## Masked detection
In folder `masked_detection`, run the `masked_model_training.ipynb` to train the masked detection model. A model named `my_model.keras` will be saved to Kaggle working directory `/kaggle/working`.

## About Dataset

- Total images: 15000 images (jpg format) including real images and synthetic images
- Number of images with more than 1 face: 109 images (0.7%)
- File annotation format:
- CSV file
- 15310 rows
- Main attributes:
  - bbox: face bounding box of format (x, y, w, h) IOU (AVG precision IOU threshold từ 0.5 - 0.95)
  - age: 20-30s, 40-50s, Kid, Senior, Baby, Teenager - accuracy (\*)
  - race: Caucasian, Mongoloid, Negroid - accuracy (\*)
  - masked: Unmasked, Masked - accuracy
  - skintone: Mid-light, Light, Mid-dark, Dark - accuracy (\*)
  - emotion: Neutral, Happiness, Anger, Surprise, Fear, Sadness, Disgust - accuracy (\*)
  - gender: Male, Female - accuracy
- Các thuộc tính khó: Độ tuổi, Cảm xúc, Tông màu da, Chủng tộc sẽ được đánh giá cao hơn các thuộc tính
  khác

## Reference

Masked detection:

    - https://medium.com/cloudnloud/building-a-face-mask-detector-using-python-and-opencv-2654e28d8d76

Skintone detection:

- https://medium.com/@chiragsaraogi1990/tonesense-discovering-diversity-in-skin-tones-through-ai-91f3a20565ad
- Code: https://github.com/chiragsaraogi15/Skin-Tone-Detection/blob/main/2_Skin_Tone_Classification.ipynb
- Google dataset (extra): https://skintone.google/mste-dataset
