# ☁️ Cloud Integration with Google Cloud Storage (GCS)

To enable realistic, audio-driven interaction in the Hugging Face demo, we needed a way to serve emergency `.wav` files on demand. Uploading the full ESC-50 dataset (~2,000 files) to Hugging Face or streaming all of them was impractical. Instead, we created a lightweight pipeline using Google Cloud Storage (GCS).

---

## Goal

Simulate a real-time interaction where a user hears an emergency sound (e.g., siren, glass breaking), and the AI agent detects and responds conversationally — all within a Hugging Face Spaces interface.

---

## 🛠Steps Taken

1. **Create an Emergency Subset**  
   We filtered the ESC-50 dataset to extract 50 labeled emergency sounds (e.g., siren, crying_baby, glass_breaking).

2. **Export a Target CSV**  
   The filtered samples were saved as `emergency_sounds_demo.csv` with metadata like filename, category, and confidence scores.

3. **Package Audio Files**  
   Using the filenames from the filtered CSV:
   - Full file paths were resolved.
   - Files were zipped into a single archive for easy download.
   - The `.zip` was downloaded locally from Kaggle.

4. **Upload to GCS Bucket**  
   - A new GCS bucket was created (`small-soundguard-audio-demo-2025`).
   - Audio files were extracted and uploaded individually.
   - Each file was made publicly accessible.

5. **Generate Public URLs CSV**  
   A new CSV (`emergency_sounds_demo_with_urls.csv`) was created with public GCS URLs for each audio file.  
   Example URL format:
```
https://storage.googleapis.com/small-soundguard-audio-demo-2025/1-100032-A-0.wav
```


6. **Stream Audio into Hugging Face Demo**  
The Gradio app on Hugging Face loads `emergency_sounds_demo_with_urls.csv` and dynamically streams audio using `<audio>` HTML tags.

---

##  Why It Matters

- **Efficiency**: We only upload the audio files we actually use in the demo.
- **Scalability**: The setup can be easily extended with more files or alternative datasets.
- **Reusability**: The GCS links can be reused across environments (Gradio, Colab, etc.).

---

## 🧩 Notes

- Ensure your GCS bucket allows public access to the `.wav` files.
- Check the Kaggle notebook’s Step 9 for the zip export and URL generation code.
