# YOGA_POSE_DETECTION

This project implements a **Yoga Pose Detection and Classification System** using deep learning, MediaPipe pose estimation, and a custom-trained classifier model. It can detect common yoga postures from images or video frames and classify them into predefined categories.

## 🚀 Features
- Real-time pose detection using **MediaPipe Pose**.
- Yoga pose classification using a trained **ML/DL model**.
- Dataset organized by pose categories (Chair, Cobra, Dog, Tree, Warrior, etc.).
- CSV keypoint extraction for each pose.
- Model training notebooks and Python scripts included.
- Support for image and video input.

## 📁 Project Structure
```
yoga_pose_detector_main/
├── classification model/
│   ├── csv_per_pose/        # Extracted pose landmark CSVs
│   ├── yoga_poses/          # Full dataset (train/test per pose)
│   ├── data.py              # Landmark extraction
│   ├── model.py             # Model training script
│   ├── predict.py           # Prediction script
│   ├── pose_classifier.joblib
│   └── notebooks (.ipynb)   # Experiments and training
└── utils/, checkpoints/, etc.
```

## 🧠 Model Workflow
1. MediaPipe detects 33 pose landmarks.
2. Landmarks are saved as CSV per pose.
3. A classifier (e.g., SVM / RandomForest / Neural Network) is trained on CSV data.
4. The trained model predicts the yoga pose from live or offline images.

## 📦 Requirements
Install dependencies:
```bash
pip install mediapipe opencv-python numpy pandas scikit-learn joblib
```

## 📊 Dataset
The dataset includes multiple yoga poses with augmented variations (flipped, rotated). Stored under:
```
classification model/yoga_poses/
```
Each pose has:
- Train and test folders
- Hundreds of labeled images

```

## 🤝 Contributions
Feel free to contribute improvements or new yoga pose classes.

## 📝 License
This project is for academic and research purposes.
