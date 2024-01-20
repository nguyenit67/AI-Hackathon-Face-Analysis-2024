from deepface import DeepFace

# Face recognition models
DeepFace.stream(
    db_path="private/database",
    model_name="VGG-Face",
    distance_metric="euclidean_l2",
    enable_face_analysis=True,
    source=0,
    detector_backend="opencv",
    frame_threshold=3,
    time_threshold=3,
)
