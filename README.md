# SoundGuard: Emergency Sound Detection with GenAI

[![Hugging Face Space](https://img.shields.io/badge/Demo-HuggingFace_Space-orange?logo=huggingface)](https://huggingface.co/spaces/ashleysally00/soundguard-genai-agent)
![Google Cloud](https://img.shields.io/badge/Powered%20by-Google%20Cloud-blue?logo=googlecloud)
![Python](https://img.shields.io/badge/Python-3.10-blue)

---
<a id="live-demo"></a>
## 🎧 Live Demo: SoundGuard Smart Agent

You can interact with the SoundGuard smart home agent on Hugging Face Spaces.

The agent analyzes real emergency sound clips (like sirens, glass breaking, and baby cries), explains what it hears, and simulates an intelligent response.

👉 [Launch the SoundGuard Agent Demo](https://huggingface.co/spaces/ashleysally00/soundguard-genai-agent) </br>

📝 [Read about the Kaggle GenAI Agent Project](https://ashleysally00.github.io/2025/04/16/soundguard-emergency-sound-detection.html)

---

  ## Table of Contents
- [Live Demo](#live-demo)
- [Overview](#overview)
- [Features](#features)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [ML Pipeline](#ml-pipeline-overview)
- [Evaluation & Monitoring](#evaluation-monitoring)
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

<a id="ml-pipeline-overview"></a>
## 🔁 ML Pipeline Overview

SoundGuard follows a real-world machine learning pipeline to detect emergency sounds and simulate agent responses. The pipeline consists of:

1. **Data Ingestion**  
   - Load the ESC-50 dataset (CSV metadata and `.wav` audio files)
   - Filter and sample emergency-related classes (e.g., siren, glass breaking)

2. **Audio Preprocessing**  
   - Resample audio to 16kHz mono (YAMNet requirement)
   - Trim silence, normalize amplitude, and extract MFCCs (optional)

3. **Audio Classification**  
   - Use Google’s YAMNet (from TensorFlow Hub) to classify each audio clip
   - Apply a fallback to ground-truth labels if confidence is too low

4. **Post-Processing & Labeling**  
   - Select high-confidence emergency predictions
   - Export metadata with public GCS audio URLs for integration

5. **Conversational Agent Simulation**  
   - Use few-shot prompting to simulate reasoning and actions
   - Trigger conversational outputs based on classification (e.g., "I heard a siren...")

6. **Frontend Interface (Gradio + Hugging Face)**  
   - Serve a live chatbot demo on Hugging Face Spaces
   - Audio clips stream from Google Cloud Storage and agent responds to user queries in real time


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
  
## 🧠 Audio Classification with YAMNet

To identify emergency sounds, we used **YAMNet**, a pretrained audio event classifier developed by Google and available on [TensorFlow Hub](https://tfhub.dev/google/yamnet/1).

YAMNet was trained on **AudioSet**, a large dataset of labeled YouTube audio clips, and can detect 521 audio classes. In our pipeline, it receives 16kHz mono waveforms and returns:

- **Predicted Class Labels**
- **Class Scores**
- **Embeddings** (for advanced use)

### Why YAMNet?

YAMNet is lightweight and fast — making it well-suited for near real-time sound classification. It’s ideal for edge cases like detecting:

- 👶 Crying baby
- 🚨 Siren
- 💥 Glass breaking

If YAMNet's prediction confidence is too low, we use a **ground truth fallback** based on ESC-50 labels to ensure emergency events are reliably flagged.

This step powers the core detection logic behind the Gradio demo interface.


## Challenges and Solutions
YAMNet struggled to classify ESC-50 emergency sounds accurately, sometimes labeling sounds like glass breaking as “Silence” or sirens as unrelated noises. This happened because YAMNet was trained on AudioSet’s noisy YouTube clips, which differ from ESC-50’s clean, short recordings, and its confidence scores are often low (e.g., 0.01) even for correct predictions, as noted in the [YAMNet documentation](https://github.com/tensorflow/models/tree/master/research/audioset/yamnet). To fix this, we added a fallback in Step 3: if YAMNet’s confidence is below 0.02, we use ESC-50’s known labels (e.g., siren) to flag emergencies reliably. This ensured the Hugging Face demo worked smoothly. See the Kaggle notebook’s “Notes on YAMNet Classification Challenges” in Step 3 for details.

### 🔗 GitHub Integration with Hugging Face

To ensure the demo reflects the full logic and emergency response pipeline built in the Kaggle notebook, we connected our **GitHub repo** to the Hugging Face Space. This allowed us to:

- Reuse the same `app.py` and CSV files generated from the Kaggle notebook
- Maintain the core logic from our original classification and response system
- Push updates from GitHub to Hugging Face without duplicating code

The Hugging Face Space pulls the `app.py` and `emergency_sounds_demo_with_urls.csv` directly from the GitHub repository. This setup ensures that any updates to the agent logic, audio sources, or interface design remain in sync between platforms.


## 🔗 Hugging Face Audio Integration

To demonstrate how our agent responds to real emergencies, we built an **interactive GUI demo** using Gradio on Hugging Face Spaces. The goal was to let users experience the system as if it were deployed in the real world. When a sound occurs, and an AI agent hears it, the agent explains what it was, and responds helpfully.

But Hugging Face Spaces can’t store thousands of audio files. So, to keep the demo lightweight and responsive, we used **Google Cloud Storage (GCS)** to host a subset of emergency sounds.

Here’s how we did it:

1. **Created a Filtered Emergency Subset**  
   Selected ~50 emergency-labeled audio clips from the ESC-50 dataset (e.g., `siren`, `glass_breaking`, `crying_baby`) to simulate a range of urgent scenarios.

2. **Exported Metadata as CSV**  
   Saved metadata for these filtered samples (filename, category, etc.) to a CSV file:  
   `emergency_sounds_demo.csv`

3. **Uploaded Audio to GCS**  
   Zipped the selected `.wav` files and uploaded them to a **Google Cloud Storage bucket**.  
   We made them publicly accessible so they could be streamed in real time.

4. **Generated a New CSV with Public URLs**  
   Added a column (`audio_url`) to point each row to the correct file in the GCS bucket.  
   Final file used in the Gradio demo:  
   `emergency_sounds_demo_with_urls.csv`

5. **Integrated with Gradio Chatbot**  
   The `app.py` file in our Hugging Face Space reads from the CSV and streams audio into the interface.  
   It selects a random emergency sound, plays it, and the chatbot agent **analyzes the sound, explains what it hears, and offers an emergency response** — just like a smart home assistant.

---

> 📂 See full cloud integration steps in [Cloud Integration Details](cloud_integration.md)

> 🎧 Try it live: [SoundGuard Agent on Hugging Face Spaces](https://huggingface.co/spaces/ashleysally00/soundguard-genai-agent)


<a id="evaluation-monitoring"></a>
## 📊 Evaluation & Monitoring

While SoundGuard is a prototype, it includes foundational elements for evaluation and observability:

- **Confidence Thresholding**  
  YAMNet predictions are evaluated by their confidence scores. Predictions with low confidence (< 0.02) trigger a fallback to ground-truth labels, improving reliability in demo scenarios.

- **Manual Review of Top-5 Predictions**  
  Each prediction is logged with its top 5 labels and scores to identify edge cases where emergency sounds may be misclassified.

- **Sample Visualization**  
  MFCC plots and waveform visualizations are used during development to inspect audio quality, clipping, and signal characteristics.

- **Demo-Level Monitoring**  
  For the Hugging Face interface, sound classifications and agent responses are displayed in real time to simulate interactive observability.

Future iterations may include formal metrics (e.g., precision/recall), user feedback logging, and integration with alerting dashboards for real-time monitoring.


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
