import gradio as gr
import pandas as pd

# Load the CSV
df = pd.read_csv('emergency_sounds_demo_with_urls.csv')
# Filter for high-confidence matches
df = df[(df['confidence'] > 0.5) & (df['yamnet_prediction'] == df['category'])]
df = df.sort_values('confidence', ascending=False)

# Gradio interface function
def display_detections():
    output_html = "<h1>SoundGuard: Emergency Sound Detection</h1>"
    output_html += "<p>Below are recent emergency sound detections with high confidence.</p>"
    for index, row in df.iterrows():
        output_html += f"<h3>🚨 {row['category']} Detected</h3>"
        output_html += f"<p><b>File:</b> {row['filename']}</p>"
        output_html += f"<p><b>Predicted:</b> {row['yamnet_prediction']} (Confidence: {row['confidence']:.2f})</p>"
        if 'audio_url' in row and row['audio_url']:
            output_html += f'<audio controls><source src="{row["audio_url"]}" type="audio/wav"></audio>'
        output_html += "<hr>"
    return output_html

# Launch Gradio interface
gr.Interface(
    fn=display_detections,
    inputs=None,
    outputs="html",
    title="SoundGuard Demo",
    description="A prototype for SoundGuard, an emergency sound detection app.",
    allow_flagging="never"
).launch()
