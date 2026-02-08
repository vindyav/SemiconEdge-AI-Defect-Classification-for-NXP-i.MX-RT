# SemiconEdge-AI-Defect-Classification-for-NXP-i.MX-RT

An Edge-AI based semiconductor defect classification system designed for deployment on **NXP i.MX RT series microcontrollers** using the **NXP eIQ Toolkit**.  
This repository contains the **Phase-1 implementation** developed for the IESA DeepTech Hackathon 2026.

---

## 🚀 Phase 1 Highlights

- **Model Architecture:** MobileNetV3-Small (edge-optimized CNN)
- **Target Platform:** NXP i.MX RT series (ARM Cortex-M)
- **Model Format:** ONNX (Opset 13)
- **Model Size:** < 3 MB
- **Input Specification:** 128 × 128 × 1 (Grayscale)
- **Number of Classes:** 8

### Defect Classes
- Clean  
- Other  
- Scratch  
- Edge-Ring  
- Center  
- Donut  
- Location  
- Random  

---

## 📌 Problem Statement

Semiconductor fabrication generates large volumes of inspection data where wafer-level defects directly impact yield and reliability.  
Traditional centralized inspection pipelines introduce **latency, bandwidth bottlenecks, and scalability challenges**.

This project demonstrates a **lightweight, edge-deployable AI solution** capable of performing **real-time defect classification** directly on inspection hardware, reducing dependency on cloud-based processing.

---

## 🧠 Solution Overview

The proposed solution uses a **compact CNN architecture** optimized for:
- Low memory footprint
- Fast inference
- Edge portability

### High-Level Pipeline
Wafer Image (Grayscale)
          ↓
Preprocessing & Augmentation
          ↓
MobileNetV3-Small CNN
          ↓
Softmax Classifier
         ↓
Defect Category Output

---

## 📁 Repository Structure
.
├── src/ # Training and preprocessing scripts
├── models/ # Exported ONNX baseline model
├── notebooks/ # Jupyter notebooks for analysis & visualization
├── requirements.txt # Python dependencies
└── README.md


---

## 📊 Dataset Plan

### Dataset Used
- **WM-811K Silicon Wafer Map Dataset**
- Source: Kaggle  
  https://www.kaggle.com/datasets/muhammedjunayed/wm811k-silicon-wafer-map-dataset-image

### Dataset Details
- **Total Images (Planned):** 1,200
- **Image Type:** Grayscale
- **Train / Validation / Test Split:** 70% / 15% / 15%

### Data Augmentation
To address class imbalance, the following augmentations are applied to minority defect classes:
- Rotation
- Zoom
- Horizontal flipping

---

## 🧪 Model Training Details

- **Framework:** PyTorch
- **Training Approach:** Transfer Learning
- **Input Size:** 128 × 128 × 1
- **Loss Function:** Categorical Cross-Entropy
- **Optimizer:** Adam

### Baseline Performance (Internal Test Split)
- Accuracy: ~85% (Phase-1 baseline)
- Metrics reported:
  - Accuracy
  - Precision
  - Recall
  - Confusion Matrix

---

## 🛠️ Edge Porting (Phase-3 Preparation)

- Model exported to **ONNX (Opset 13)** for compatibility with:
  - NXP eIQ Toolkit
  - Neutron provider
  - GLOW compiler

### Planned Optimizations
- INT8 Post-Training Quantization
- Memory and latency optimization for:
  - i.MX RT1060
  - i.MX RT1170

*(Hardware deployment is not in scope for Phase-1.)*

---

## 🔗 Submission Artifacts

- **Dataset:**  
  https://www.kaggle.com/datasets/muhammedjunayed/wm811k-silicon-wafer-map-dataset-image

- **ONNX Model:**  
  Available in `/models`

- **Phase-1 Slides & Documentation:**  
  Included in submission package

---

## 📚 References

1. Howard et al., *MobileNetV3: Searching for MobileNetV3*, Google Research  
2. WM-811K Wafer Map Dataset, Kaggle  
3. NXP eIQ Toolkit Documentation  

---

## 🏁 Phase Status

✅ Phase-1: Dataset preparation & baseline model  
🔜 Phase-2: Evaluation on organizer-provided test dataset  
🔜 Phase-3: Edge optimization and NXP eIQ deployment artifacts

---

**Team Name:** EdgeYield AI  
**Tagline:** *Smarter Inspection. Higher Yield. At the Edge.*
