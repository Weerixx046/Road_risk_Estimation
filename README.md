# Road Risk Estimation Dataset

**Created:** September 2026
**Institution:** Kasetsart University (Kamphaeng Saen Campus)
**Team:** UMA 

---

## 1. Dataset Overview

The **Road Risk Estimation Dataset** is a collection of road surface images designed for developing and evaluating an AI model for road risk estimation.

The dataset is used to train a **ResNet-50** deep learning model to predict a continuous **road risk score from 0–100** using a regression approach.

The images represent various road conditions and levels of visible road damage, providing diverse examples for model training and evaluation.

### Dataset Information

| Property           | Description                  |
| ------------------ | ---------------------------- |
| Created            | September 2026               |
| Institution        | Kasetsart University         |
| Campus             | Kamphaeng Saen Campus        |
| Number of Images   | 9,173                        |
| Image Format       | JPG / PNG                    |
| Image Resolution   | 224 × 224 pixels             |
| Color Format       | RGB                          |
| Task               | Regression                   |
| Risk Score         | 0–100                        |
| Model Architecture | ResNet-50                    |

---

## 2. Data Source

Images were collected from two main sources:

* **Local images:** Collected within the Kasetsart University Kamphaeng Saen Campus.
* **Online images:** Collected from various online platforms.

Combining these sources helps increase the diversity of the dataset in terms of:

* Lighting conditions
* Road types
* Road surface conditions
* Damage characteristics
* Damage severity

This diversity is intended to improve the model's ability to generalize to different road environments.

---

## 3. Dataset Structure

The dataset consists of road surface images accompanied by their corresponding road risk scores.

Each image represents a road condition that is assigned a continuous risk score between **0 and 100**.

The dataset is intended for a **regression problem**, where the model predicts a numerical risk score rather than a discrete class.
dataset/
├── test_data/
├── train_data/
├── val_data/
├── test_split.csv
├── train_dataset_final.csv
├── train_split.csv
└── val_split.csv

---

## 4. Annotation

Ground truth risk scores ranging from **0–100** were manually annotated by project group members.

The scoring process is based on standard **Road Safety Assessment (RSA)** guidelines and considers visible characteristics of the road surface and its potential safety risks.

Because the scores are manually assigned, minor differences in judgment may occur between annotators.

---

## 5. Recommended Data Split

The dataset is recommended to be divided into three subsets:

| Subset     | Percentage |
| ---------- | ---------: |
| Training   |        80% |
| Validation |        10% |
| Testing    |        10% |

This split provides sufficient data for model training while reserving separate data for validation and final performance evaluation.

---

## 6. Model

The dataset is designed to support a **ResNet-50** architecture for road risk estimation.

Instead of performing image classification, the model is configured as a **regression model** that outputs a single continuous value representing the estimated road risk score.

**Output range:** `0–100`

---

## 7. Data Preprocessing & Normalization

To ensure compatibility with the ResNet-50 architecture and improve training stability, the following preprocessing steps are applied.

### Resizing

All images are resized to:

**224 × 224 pixels**

This resolution is compatible with the standard ResNet-50 input size.

### Normalization

Images are normalized using the standard **ImageNet** mean and standard deviation values:

```text
Mean = [0.485, 0.456, 0.406]
Std  = [0.229, 0.224, 0.225]
```

These values are commonly used when working with ResNet models pretrained on ImageNet.

---

## 8. Dataset Limitations

### Human Subjectivity

The ground truth risk scores were manually annotated by project team members.

Since evaluating visual road damage involves human judgment, there may be minor inconsistencies or differences in scoring between annotators.

### Annotation Outliers

Some images may receive scores that differ from the general scoring pattern due to subjective judgment or unusual road conditions.

To help reduce the impact of annotation variance and outliers during training, the model training pipeline uses:

**Smooth L1 Loss (Huber Loss)**

Smooth L1 Loss is less sensitive to large errors than standard Mean Squared Error (MSE), making it suitable for regression tasks where occasional annotation outliers may exist.

---

## 9. Intended Use

This dataset is intended for:

* Road risk estimation research
* Computer vision research
* Deep learning and regression experiments
* Road surface condition analysis

The dataset is primarily developed as part of the **Road Risk Estimation** project at Kasetsart University, Kamphaeng Saen Campus.

---

## 10. Contact

For inquiries, feedback, or further information regarding this dataset, please contact the project team:

| Name                | Email                |
| ------------------- | -------------------  |
| Kawee Saithong      | Kawee.sai@ku.th      |
| Techin Khongyai     | Techin.kh@ku.th      |
| Chayanggoon Klahan  | chayanggoon.k@ku.th  |
| Akenaras Boonraksa  | akenaras.b@ku.th     |

**Team:** UMA 
**Institution:** Kasetsart University (Kamphaeng Saen Campus)
**GitHub Repository:** `Weerixx046/Road_risk_Estimation`
