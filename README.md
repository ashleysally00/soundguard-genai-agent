# SoundGuard: Emergency Sound Detection with GenAI

[![Hugging Face Space](https://img.shields.io/badge/Demo-HuggingFace_Space-orange?logo=huggingface)](https://huggingface.co/spaces/ashleysally00/soundguard-genai-agent)
![Google Cloud](https://img.shields.io/badge/Powered%20by-Google%20Cloud-blue?logo=googlecloud)
![Python](https://img.shields.io/badge/Python-3.10-blue)

---

## 🎧 Live Demo: SoundGuard Smart Agent

You can interact with the SoundGuard smart home agent on Hugging Face Spaces.

The agent analyzes real emergency sound clips (like sirens, glass breaking, and baby cries), explains what it hears, and simulates an intelligent response.

👉 [Launch the SoundGuard Agent Demo](https://huggingface.co/spaces/ashleysally00/soundguard-genai-agent)

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Documentation](#documentation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Work](#future-work)
- [Acknowledgments](#acknowledgments)
- [Author](#author)


## Overview

SoundGuard is a capstone project for the **Gen AI Intensive Course Capstone 2025Q1**, a 5-day GenAI training program with Google. It uses generative AI to detect emergency-related sounds (e.g., glass breaking, sirens) and generate actionable responses for smart home safety.

The project demonstrates three core GenAI capabilities:
- **Audio Understanding**
- **Few-Shot Prompting**
- **Function Calling / Agents**

It creates a pipeline that detects sounds, generates alerts, and simulates intelligent agent responses.

As part of the deployment, the project integrates with **Google Cloud Storage (GCS)** to host a CSV file containing metadata and public URLs for emergency audio clips. These clips are streamed directly into the Hugging Face demo, enabling realistic interactions with the AI agent.

The implementation is hosted in a Kaggle notebook and leverages the ESC-50 dataset for audio classification using YAMNet. The goal is to explore how GenAI can enhance safety in smart homes, public safety systems, and disaster response scenarios.

📘 **View the Kaggle Notebook**  
_(Link will be available post-competition, April 20, 2025)_

---

## Features

- **Audio Understanding**: Classifies emergency sounds (e.g., glass breaking, sirens) using YAMNet and ESC-50  
- **Few-Shot Prompting**: Generates natural-language alerts like:  
  _“Glass breaking was detected in a smart home at 2 AM. This could indicate a potential break-in…”_  
- **Function Calling & Agents**: Simulates a smart home assistant that responds to detected emergencies (e.g., locking doors, alerting authorities)  
- **End-to-End Pipeline**: Detects sounds → generates alerts → triggers contextual responses, demonstrating a real-world GenAI use case  
- **Google Cloud Storage Integration**: Uses GCS to serve metadata and URLs for streaming real audio into the Hugging Face demo


## How to Run
1. **Access the Kaggle Notebook**:
   - The notebook will be available after the competition ends (April 20, 2025). Check back for the link in the "Overview" section.
   - It is set to public for capstone evaluation and will be fully accessible after the competition concludes.
2. **Run the Notebook**:
   - Click “Run All” to execute the notebook end-to-end.
   - The notebook includes all steps: data loading, audio classification, alert generation, and agent responses.
3. **Dependencies**:
   - The notebook runs on Kaggle with all dependencies pre-installed (e.g., `librosa`, `tensorflow`, `tensorflow_hub`).
   - Internet must be enabled in Kaggle settings to load YAMNet and the ESC-50 dataset.

## Project Structure
- **Step 1: Introduction** - Introduces the project and its goals.
- **Step 2: Dataset Loading** - Loads the ESC-50 dataset for audio classification.
- **Step 3: Audio Understanding** - Uses YAMNet to classify emergency sounds, with a ground truth fallback for reliability.
- **Step 4: Few-Shot Prompting** - Generates natural-language alerts based on detected sounds.
- **Step 5: Function Calling/Agents** - Simulates a smart home agent that responds to emergencies with actions like locking doors and calling authorities.
  

## Challenges and Solutions
YAMNet struggled to classify ESC-50 emergency sounds accurately, sometimes labeling sounds like glass breaking as “Silence” or sirens as unrelated noises. This happened because YAMNet was trained on AudioSet’s noisy YouTube clips, which differ from ESC-50’s clean, short recordings, and its confidence scores are often low (e.g., 0.01) even for correct predictions, as noted in the [YAMNet documentation](https://github.com/tensorflow/models/tree/master/research/audioset/yamnet). To fix this, we added a fallback in Step 3: if YAMNet’s confidence is below 0.02, we use ESC-50’s known labels (e.g., siren) to flag emergencies reliably. This ensured the Hugging Face demo worked smoothly. See the Kaggle notebook’s “Notes on YAMNet Classification Challenges” in Step 3 for details.


## Future Work
- Fine-tune YAMNet on ESC-50 to improve classification accuracy.
- Enhance audio preprocessing (e.g., denoising, padding) to better match YAMNet’s expectations.
- Integrate with real smart home systems (e.g., via APIs) to execute actual actions like locking doors or sending notifications.
- Explore alternative models better suited for ESC-50, or use YAMNet embeddings to train a shallow classifier.

## Acknowledgments
- **Gen AI Intensive Course 2025Q1**: For providing the framework and inspiration for this project.
- **Kaggle**: For hosting the notebook and providing the ESC-50 dataset.
- **YAMNet Team**: For the pretrained audio classification model.

## Author
- **ashleysally00** - Creator of SoundGuard, participant in the Gen AI Intensive Course Capstone 2025Q1.📚🎤
