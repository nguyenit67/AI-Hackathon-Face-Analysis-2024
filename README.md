About Dataset

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

Masked:

    - https://medium.com/cloudnloud/building-a-face-mask-detector-using-python-and-opencv-2654e28d8d76

Skintone:

- https://medium.com/@chiragsaraogi1990/tonesense-discovering-diversity-in-skin-tones-through-ai-91f3a20565ad
- Code: https://github.com/chiragsaraogi15/Skin-Tone-Detection/blob/main/2_Skin_Tone_Classification.ipynb
- Google dataset (extra): https://skintone.google/mste-dataset
