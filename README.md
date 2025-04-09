# SoundGuard: Emergency Sound Detection with GenAI

Live Dashboard: Link to the Airtable dashboard will be available post-competition, April 20, 2025.

## Overview
SoundGuard is a capstone project for the **Gen AI Intensive Course Capstone 2025Q1**, a 5-day Gen AI Intensive Course with Google. It uses generative AI to detect emergency-related sounds (e.g., glass breaking, sirens) and generate actionable responses for smart home safety. The project demonstrates three GenAI capabilities: **Audio Understanding**, **Few-Shot Prompting**, and **Function Calling/Agents**, creating a pipeline that detects sounds, generates alerts, and triggers smart home responses.

The project is implemented in a Kaggle notebook, leveraging the ESC-50 dataset for audio classification and YAMNet for audio understanding. The goal is to explore how GenAI can enhance safety in smart homes, public safety systems, or disaster response by understanding sounds and reacting appropriately.

**View the Kaggle Notebook**: Link will be available post-competition, April 20, 2025.

## Features
- **Audio Understanding**: Classifies emergency sounds (e.g., glass breaking, sirens) using YAMNet and the ESC-50 dataset.
- **Few-Shot Prompting**: Generates natural-language alerts (e.g., "Glass breaking was detected in a smart home at 2 AM. This could indicate a potential break-in…").
- **Function Calling/Agents**: Simulates a smart home agent that responds to emergencies (e.g., locking doors, calling authorities, sending notifications).
- **Comprehensive Pipeline**: Detects sounds → generates alerts → triggers actions, demonstrating a practical GenAI application for smart home safety.

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
YAMNet’s classification performance on ESC-50 was limited due to a domain mismatch (AudioSet vs. ESC-50) and uncalibrated scores, as noted in the [YAMNet documentation](https://tfhub.dev/google/yamnet/1). To address this, we implemented a ground truth fallback in Step 3, using ESC-50 labels to flag emergencies when YAMNet’s confidence is low (< 0.02). This ensures the pipeline works for the demo, as detailed in the notebook’s “Notes on YAMNet Classification Challenges” section.

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
