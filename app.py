import gradio as gr
import os
import csv
from datetime import datetime
import random
import string

# Sentences from text.txt
SENTENCES = {
    1: "يا هلا والله، كيف حالك وكيف العيال؟",
    2: "تصدق إني رحت للسوق ولقيته مقفل عشان الصلاة.",
    3: "لو سمحت، وين ألقى أقرب صيدلية تكون فاتحة دحين؟",
    4: "أحس إني تعبان شوي ومالي خلق أطلع من البيت.",
    5: "أبشر من عيوني، كل اللي تبي بيصير إن شاء الله.",
    6: "والله ما قصرت، بيض الله وجهك وكثر الله خيرك.",
    7: "يا حليلهم الصغار، جالسين يلعبون بالحوش من العصر.",
    8: "سبحان الله، الدنيا ذي غريبة وكل يوم نشوف فيها عجب.",
    9: "السلام عليكم، أنا فهد من قسم خدمة العملاء، وش أقدر أساعدك فيه اليوم؟",
    10: "يعني لازم اجلس شهر اقسط على حسابي الجاري عشان ترجع الفلوس كامله للبطاقة؟ مهب منطق كذا"
}

# Audio files mapping
DATA = {
    1: [
        "9e7a2b3c-4d5e-4f6a-8b9c-0d1e2f3a4b5c.wav",
        "a1b2c3d4-e5f6-4789-80b1-c2d3e4f5a6b7.wav",
        "b2c3d4e5-f6a7-4890-91c2-d3e4f5a6b7c8.wav",
        "c3d4e5f6-a7b8-4901-a2d3-e4f5a6b7c8d9.wav",
        "d4e5f6a7-b8c9-4a12-b3e4-f5a6b7c8d9e0.wav"
    ],
    2: [
        "e5f6a7b8-c9d0-4b23-c4e5-f6a7b8c9d0e1.wav",
        "f6a7b8c9-d0e1-4c34-d5f6-a7b8c9d0e1f2.wav",
        "a7b8c9d0-e1f2-4d45-e6a7-b8c9d0e1f2a3.wav",
        "b8c9d0e1-f2a3-4e56-f7b8-c9d0e1f2a3b4.wav",
        "c9d0e1f2-a3b4-4f67-a8c9-d0e1f2a3b4c5.wav"
    ],
    3: [
        "d0e1f2a3-b4c5-4a78-b9d0-e1f2a3b4c5d6.wav",
        "e1f2a3b4-c5d6-4b89-c0e1-f2a3b4c5d6e7.wav",
        "f2a3b4c5-d6e7-4c90-d1f2-a3b4c5d6e7f8.wav",
        "a3b4c5d6-e7f8-4d01-e2a3-b4c5d6e7f8a9.wav",
        "b4c5d6e7-f8a9-4e12-f3b4-c5d6e7f8a9b0.wav"
    ],
    4: [
        "c5d6e7f8-a9b0-4f23-a4c5-d6e7f8a9b0c1.wav",
        "d6e7f8a9-b0c1-4034-b5d6-e7f8a9b0c1d2.wav",
        "e7f8a9b0-c1d2-4145-c6e7-f8a9b0c1d2e3.wav",
        "f8a9b0c1-d2e3-4256-d7f8-a9b0c1d2e3f4.wav",
        "a9b0c1d2-e3f4-4367-e8a9-b0c1d2e3f4a5.wav"
    ],
    5: [
        "b0c1d2e3-f4a5-4478-f9b0-c1d2e3f4a5b6.wav",
        "c1d2e3f4-a5b6-4589-a0c1-d2e3f4a5b6c7.wav",
        "d2e3f4a5-b6c7-4690-b1d2-e3f4a5b6c7d8.wav",
        "e3f4a5b6-c7d8-4701-c2e3-f4a5b6c7d8e9.wav",
        "f4a5b6c7-d8e9-4812-d3f4-a5b6c7d8e9f0.wav"
    ],
    6: [
        "a5b6c7d8-e9f0-4923-e4a5-b6c7d8e9f0a1.wav",
        "b6c7d8e9-f0a1-4a34-f5b6-c7d8e9f0a1b2.wav",
        "c7d8e9f0-a1b2-4b45-a6c7-d8e9f0a1b2c3.wav",
        "d8e9f0a1-b2c3-4c56-b7d8-e9f0a1b2c3d4.wav",
        "e9f0a1b2-c3d4-4d67-c8e9-f0a1b2c3d4e5.wav"
    ],
    7: [
        "f0a1b2c3-d4e5-4e78-d9f0-a1b2c3d4e5f6.wav",
        "a1b2c3d4-e5f6-4f89-e0a1-b2c3d4e5f6a7.wav",
        "b2c3d4e5-f6a7-4090-f1b2-c3d4e5f6a7b8.wav",
        "c3d4e5f6-a7b8-4101-a2c3-d4e5f6a7b8c9.wav",
        "d4e5f6a7-b8c9-4212-b3d4-e5f6a7b8c9d0.wav"
    ],
    8: [
        "e5f6a7b8-c9d0-4323-c4e5-f6a7b8c9d0e1.wav",
        "f6a7b8c9-d0e1-4434-d5f6-a7b8c9d0e1f2.wav",
        "a7b8c9d0-e1f2-4545-e6a7-b8c9d0e1f2a3.wav",
        "b8c9d0e1-f2a3-4656-f7b8-c9d0e1f2a3b4.wav",
        "c9d0e1f2-a3b4-4767-a8c9-d0e1f2a3b4c5.wav"
    ],
    9: [
        "d0e1f2a3-b4c5-4878-b9d0-e1f2a3b4c5d6.wav",
        "e1f2a3b4-c5d6-4989-c0e1-f2a3b4c5d6e7.wav",
        "f2a3b4c5-d6e7-4a90-d1f2-a3b4c5d6e7f8.wav",
        "a3b4c5d6-e7f8-4b01-e2a3-b4c5d6e7f8a9.wav",
        "b4c5d6e7-f8a9-4c12-f3b4-c5d6e7f8a9b0.wav"
    ],
    10: [
        "c5d6e7f8-a9b0-4d23-a4c5-d6e7f8a9b0c1.wav",
        "d6e7f8a9-b0c1-4e34-b5d6-e7f8a9b0c1d2.wav",
        "e7f8a9b0-c1d2-4f45-c6e7-f8a9b0c1d2e3.wav",
        "f8a9b0c1-d2e3-4056-d7f8-a9b0c1d2e3f4.wav",
        "a9b0c1d2-e3f4-4167-e8a9-b0c1d2e3f4a5.wav"
    ]
}

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def generate_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def save_results(*ratings):
    # Basic Validation: Check if any rating is None
    if any(r is None for r in ratings):
        return "⚠️ **Warning:** It looks like you missed some ratings. Please go back through the tabs and ensure every sample has a Naturalness and Clarity score."

    user_id = generate_user_id()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{RESULTS_DIR}/mos_results_{timestamp}_{user_id}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'timestamp', 'sentence_id', 'audio_idx', 'naturalness', 'clarity'])
        
        idx = 0
        for s_id in range(1, 11):
            for a_idx in range(1, 6):
                naturalness = ratings[idx]
                clarity = ratings[idx + 1]
                writer.writerow([user_id, timestamp, s_id, a_idx, naturalness, clarity])
                idx += 2
    
    return f"## ✅ Success!\n**Submission ID:** `{user_id}`. Your results are saved."

custom_css = """
    .gradio-container { background-color: #0b0e14; color: #ffffff; }
    .container { max-width: 1000px; margin: auto; padding-bottom: 50px; }
    .sentence-card { 
        background: rgba(255, 255, 255, 0.03); 
        border-radius: 12px; 
        padding: 20px; 
        border: 1px solid #334155;
    }
    .arabic-text { 
        font-size: 24px !important; 
        direction: rtl; 
        text-align: center; 
        padding: 20px;
        background: #1e293b;
        border-radius: 8px;
        margin-bottom: 20px;
        border-right: 5px solid #8b5cf6;
    }
    .audio-block {
        background: rgba(0,0,0,0.3);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 1px solid #1e293b;
    }
    .submit-area {
        margin-top: 30px;
        padding: 20px;
        border-top: 1px solid #334155;
        text-align: center;
    }
"""

def create_interface():
    with gr.Blocks(css=custom_css, theme=gr.themes.Soft(primary_hue="purple")) as demo:
        with gr.Column(elem_classes="container"):
            gr.Markdown("# 🎙️ Voice Quality Evaluation")
            gr.Markdown("### Instructions: \n1. Work through **Sentences 1 to 10** using the tabs. \n2. Rate all **50 audio samples**. \n3. Click the **Submit** button at the very bottom when finished.")
            
            rating_components = []

            # Organized Tabs
            with gr.Tabs():
                for i in range(1, 11, 2):  # Grouping by 2s for better organization
                    with gr.Tab(f"Sentences {i}-{i+1}"):
                        for s_id in [i, i+1]:
                            if s_id > 10: break
                            
                            with gr.Column(elem_classes="sentence-card"):
                                gr.Markdown(f"## Sentence {s_id}")
                                gr.HTML(f"<div class='arabic-text'>{SENTENCES[s_id]}</div>")
                                
                                for a_idx, audio_file in enumerate(DATA[s_id], 1):
                                    with gr.Column(elem_classes="audio-block"):
                                        gr.Markdown(f"**Sample {s_id}.{a_idx}**")
                                        gr.Audio(f"audio/{s_id}/{audio_file}", show_label=False)
                                        with gr.Row():
                                            nat = gr.Radio(["1", "2", "3", "4", "5"], label="Naturalness")
                                            clar = gr.Radio(["1", "2", "3", "4", "5"], label="Clarity")
                                            rating_components.extend([nat, clar])

            # SUBMIT AREA - Moved "Down there" (Outside the tabs)
            with gr.Column(elem_classes="submit-area"):
                gr.Markdown("---")
                gr.Markdown("### Final Step")
                gr.Markdown("Ensure you have visited all tabs above before submitting.")
                submit_btn = gr.Button("🚀 SUBMIT ALL RATINGS", variant="primary", size="lg")
                output_msg = gr.Markdown()

            submit_btn.click(
                fn=save_results,
                inputs=rating_components,
                outputs=output_msg
            )
            
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True)