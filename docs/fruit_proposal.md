---
title: Deep Learning to Predict Fruit Quality
subtitle: Proposal
author: Rahul Jain (rjdharmc), Sahil Dhingra (sahdhin), Mark Green (margree)
date: Fall 2023
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
output: pdf_document
toc: true
---

# Introduction:

The food industry plays a critical role in ensuring public health and safety. Quality control in the food sector is vital to guarantee that products meet the necessary standards for consumption. With advancements in deep learning techniques, there is an opportunity to create an automated and efficient system for identifying fruits and assessing their condition before distribution. This system not only identifies fruits but also evaluates their condition, preventing the spoilage of entire lots due to a few bad fruits. By minimizing wastage, this technology stands to significantly impact food sustainability and resource utilization.


# Proposal: 

We present a comprehensive project to create an automated Fruit Quality Control System using a meticulously curated [dataset](https://data.mendeley.com/datasets/6ps7gtp2wg/1) of 16,000 labeled images, each containing 2,000 images of 8 diverse fruits, equally balanced between fresh and spoiled conditions. This rich dataset forms the foundation of our research, enabling rigorous training and validation.
Our primary focus is the implementation of state-of-the-art Convolutional Neural Network (CNN) architectures. In addition, we aim to explore the efficiency and accuracy of EfficientNet architectures, specifically tailored for low-computing environments. This dual approach ensures a thorough evaluation of models in varying computational scenarios.

# Responsibilities:

The roles and responsibilities will be shared across the team, but here are some key tasks and the associated stakeholders.

| Task                         | Mark | Rahul | Sahil |
|------------------------------|------|-------|-------|
| Data Pipeline                |   X  |       |       |
| Data Preprocessing           |   X  |       |   X   |
| CNN Architecture(s)          |   X  |   X   |   X   |
| Hyperparameter Tuning        |   X  |   X   |   X   |
| Model Deployment on Cloud    |   X  |       |   X   |
| Presentation Production      |      |       |   X   |
| Report Production            |   X  |       |       |

# Technical Approach and Goals:

- Employ industry-standard CNN architectures such as VGG16, ResNet, EfficientNet, and Inception, and compare their accuracies to identify the most suitable model. We will tone down the layers depending upon computing capacity, if required. 
- Significant reduction in training time through the application of transfer learning, optimizing the model for our specific dataset.
- Enhanced model performance achieved through systematic hyperparameter tuning, resulting in accurate and efficient fruit recognition.
- Accurate object detection and probability labeling, providing detailed insights into the model's confidence levels and enabling precise quality assessment.
- Successful implementation of EfficientNet and deploying the solution on low-computation architectures (e.g. Raspberry Pi), demonstrating the system's adaptability to diverse computing environments.

## Projected Timeline

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    title       Deep Learning Project - Proposed Project Timeline

    section Proposal
    Charter Team                     :done, p1, 2023-09-16, 2023-09-17
    Write Proposal                   :active, p2, after p1, 21d
    Research Topic and Tools         :active, p3, after p1, 21d
    Proposal DUE                     :crit, milestone, p4, 2023-10-08, 0d

    section Project Development
    Project Design                   :a1, after p4, 7d
    Build Data Pipeline              :a2, after p4, 14d
    Feature Engineering              :a3, 2023-10-15, 14d
    Design Neural Network            :a4, after a2, 21d
    Tune Hyperparameters             :a5, 2023-10-29, 21d
    Testing                          :a6, after a5, 7d
    Project Complete                 :crit, milestone, a7, after a6, 0d

    section Final Report
    Introduction                     :f1, 2023-10-29, 7d
    Methods                          :f2, after f1, 14d
    Results                          :f3, after a5, 14d
    Discussion                       :f4, after a5, 14d
    Review                           :f5, after f4, 8d
    Report DUE                       :crit, milestone, f6, 2023-12-11, 0d

    section Project Presentation
    Video Materials Prep             :v1, 2023-11-26, 7d
    Video Production                 :v2, after v1, 8d
    Presentation DUE                 :crit, milestone, v3, 2023-12-11, 0d

```

