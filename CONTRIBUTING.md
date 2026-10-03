# Road Risk Estimation Dataset

**Version:** v1.0
**Created:** September 2026
**Institution:** Kasetsart University

---

## 1. Dataset Description

This dataset contains images of road surfaces used for the **Road Risk Estimation AI** project. The model (**ResNet-50**) analyzes these images to predict a risk score indicating the severity of road damage.

* **Number of images:** 9,173
* **Target Output:** Regression (Risk Score 0–100)
* **Image Format:** JPG / PNG
* **Image Size:** 224 × 224 pixels (RGB)

---

## 2. Risk Level Categories

Although the model predicts a continuous score from 0 to 100, the final results are grouped into the following risk levels for user display:

| Level |   Score Range  | Description                                  |
| :---: | :------------: | -------------------------------------------- |
| **A** |  0.00 – 14.00  | Very Low Risk (Normal road condition)        |
| **B** |  14.01 – 30.00 | Low Risk (Minor defects)                     |
| **C** |  30.01 – 40.00 | Moderate Risk (Visible damage)               |
| **D** |  40.01 – 50.00 | High Risk (Requires monitoring)              |
| **F** | 50.01 – 100.00 | Critical Risk (Severe damage, urgent repair) |

---

## 3. Dataset Structure

```text
dataset/
├── test_data/
├── train_data/
├── val_data/
├── test_split.csv
├── train_dataset_final.csv
├── train_split.csv
└── val_split.csv
```

---

## 4. Data Source

Images were collected from two main sources: locally within the **Kamphaeng Saen Campus** and from various online platforms.

This combination ensures diversity in lighting, road types, and damage severity.

---

## 5. Annotation

* Ground truth risk scores (0–100) were annotated by project group members.
* Scoring is based on standard **Road Safety Assessment (RSA)** guidelines.

---

## 6. Recommended Data Split

| Subset         | Percentage |
| :------------- | ---------: |
| **Training**   |        80% |
| **Validation** |        10% |
| **Testing**    |        10% |

---

## 7. Contact

**GitHub:** https://github.com/Weerixx046
