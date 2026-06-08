import gradio as gr
import os
import csv
from datetime import datetime

# --- Configuration ---
MASTER_CSV = "results/master_mos_results.csv"
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Star display choices and their numeric mapping
STAR_CHOICES = ["⭐️", "⭐️⭐️", "⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️", "⭐️⭐️⭐️⭐️⭐️"]
STAR_TO_NUM = {
    "⭐️": 1,
    "⭐️⭐️": 2,
    "⭐️⭐️⭐️": 3,
    "⭐️⭐️⭐️⭐️": 4,
    "⭐️⭐️⭐️⭐️⭐️": 5,
}

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

DATA = {
    1: [
        "9e7a2b3c-4d5e-4f6a-8b9c-0d1e2f3a4b5c.wav",
        "a1b2c3d4-e5f6-4789-80b1-c2d3e4f5a6b7.wav",
        "b2c3d4e5-f6a7-4890-91c2-d3e4f5a6b7c8.wav",
        "c3d4e5f6-a7b8-4901-a2d3-e4f5a6b7c8d9.wav",
        "line_0001.wav"
    ],
    2: [
        "e5f6a7b8-c9d0-4b23-c4e5-f6a7b8c9d0e1.wav",
        "f6a7b8c9-d0e1-4c34-d5f6-a7b8c9d0e1f2.wav",
        "a7b8c9d0-e1f2-4d45-e6a7-b8c9d0e1f2a3.wav",
        "b8c9d0e1-f2a3-4e56-f7b8-c9d0e1f2a3b4.wav",
        "line_0002.wav"
    ],
    3: [
        "d0e1f2a3-b4c5-4a78-b9d0-e1f2a3b4c5d6.wav",
        "e1f2a3b4-c5d6-4b89-c0e1-f2a3b4c5d6e7.wav",
        "f2a3b4c5-d6e7-4c90-d1f2-a3b4c5d6e7f8.wav",
        "a3b4c5d6-e7f8-4d01-e2a3-b4c5d6e7f8a9.wav",
        "line_0003.wav"
    ],
    4: [
        "c5d6e7f8-a9b0-4f23-a4c5-d6e7f8a9b0c1.wav",
        "d6e7f8a9-b0c1-4034-b5d6-e7f8a9b0c1d2.wav",
        "e7f8a9b0-c1d2-4145-c6e7-f8a9b0c1d2e3.wav",
        "f8a9b0c1-d2e3-4256-d7f8-a9b0c1d2e3f4.wav",
        "line_0004.wav"
    ],
    5: [
        "b0c1d2e3-f4a5-4478-f9b0-c1d2e3f4a5b6.wav",
        "c1d2e3f4-a5b6-4589-a0c1-d2e3f4a5b6c7.wav",
        "d2e3f4a5-b6c7-4690-b1d2-e3f4a5b6c7d8.wav",
        "e3f4a5b6-c7d8-4701-c2e3-f4a5b6c7d8e9.wav",
        "line_0005.wav"
    ],
    6: [
        "a5b6c7d8-e9f0-4923-e4a5-b6c7d8e9f0a1.wav",
        "b6c7d8e9-f0a1-4a34-f5b6-c7d8e9f0a1b2.wav",
        "c7d8e9f0-a1b2-4b45-a6c7-d8e9f0a1b2c3.wav",
        "d8e9f0a1-b2c3-4c56-b7d8-e9f0a1b2c3d4.wav",
        "line_0006.wav"
    ],
    7: [
        "f0a1b2c3-d4e5-4e78-d9f0-a1b2c3d4e5f6.wav",
        "a1b2c3d4-e5f6-4f89-e0a1-b2c3d4e5f6a7.wav",
        "b2c3d4e5-f6a7-4090-f1b2-c3d4e5f6a7b8.wav",
        "c3d4e5f6-a7b8-4101-a2c3-d4e5f6a7b8c9.wav",
        "line_0007.wav"
    ],
    8: [
        "e5f6a7b8-c9d0-4323-c4e5-f6a7b8c9d0e1.wav",
        "f6a7b8c9-d0e1-4434-d5f6-a7b8c9d0e1f2.wav",
        "a7b8c9d0-e1f2-4545-e6a7-b8c9d0e1f2a3.wav",
        "b8c9d0e1-f2a3-4656-f7b8-c9d0e1f2a3b4.wav",
        "line_0008.wav"
    ],
    9: [
        "d0e1f2a3-b4c5-4878-b9d0-e1f2a3b4c5d6.wav",
        "e1f2a3b4-c5d6-4989-c0e1-f2a3b4c5d6e7.wav",
        "f2a3b4c5-d6e7-4a90-d1f2-a3b4c5d6e7f8.wav",
        "a3b4c5d6-e7f8-4b01-e2a3-b4c5d6e7f8a9.wav",
        "line_0009.wav"
    ],
    10: [
        "c5d6e7f8-a9b0-4d23-a4c5-d6e7f8a9b0c1.wav",
        "d6e7f8a9-b0c1-4e34-b5d6-e7f8a9b0c1d2.wav",
        "e7f8a9b0-c1d2-4f45-c6e7-f8a9b0c1d2e3.wav",
        "f8a9b0c1-d2e3-4056-d7f8-a9b0c1d2e3f4.wav",
        "line_0010.wav"
    ]
}

def save_results(user_name, read_guidelines, *ratings):
    if not user_name or user_name.strip() == "":
        return "⚠️ **Submission Denied:** Evaluator name is required."
    if not read_guidelines:
        return "⚠️ **Submission Denied:** Please acknowledge the guidelines."
    if any(r is None for r in ratings):
        missing = ratings.count(None)
        return f"⚠️ **Incomplete:** {missing} rating(s) missing. Please check all 10 tabs."

    # Convert star strings → integers (1–5) for CSV storage
    numeric_ratings = [STAR_TO_NUM[r] for r in ratings]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(MASTER_CSV)

    try:
        with open(MASTER_CSV, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['timestamp', 'user_name', 'sentence_id', 'audio_idx', 'wav_filename', 'naturalness', 'clarity'])

            idx = 0
            for s_id in range(1, 11):
                for a_idx in range(1, 6):
                    orig_filename = DATA[s_id][a_idx - 1]
                    writer.writerow([
                        timestamp, user_name, s_id, a_idx, orig_filename,
                        numeric_ratings[idx], numeric_ratings[idx + 1]
                    ])
                    idx += 2
        return f"### ✅ Success\nRatings logged for **{user_name}**."
    except Exception as e:
        return f"❌ **Error:** {str(e)}"

INSTRUCTIONS_HTML = """
<div dir="rtl" style="font-family: 'Segoe UI', Tahoma, sans-serif; color: #f1f5f9; padding: 10px 0;">
  <h3 style="color: #c084fc; margin-bottom: 16px;">📋 التعليمات</h3>
  <p style="margin-bottom: 20px;">فضلاً قم بتقييم المقاطع بناءً على معيارين:</p>

  <!-- Naturalness Table -->
  <h4 style="color: #a855f7; margin-bottom: 10px;">١. الطبيعية (Naturalness)</h4>
  <p style="margin-bottom: 10px; color: #cbd5e1;">قد ايش الصوت بشري ومش روبوتي في إيقاع الصوت، ونبرة الكلام، والإحساس العاطفي</p>
  <table style="width:100%; border-collapse: collapse; margin-bottom: 24px; direction: rtl;">
    <thead>
      <tr style="background: #1e1b4b; color: #a855f7;">
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">الدرجة</th>
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">التقييم</th>
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">الوصف</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #a3e635;">ممتاز</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">طبيعي تمامًا؛ لا يمكن تمييزه عن متحدث سعودي أصلي.</td>
      </tr>
      <tr style="background: #111827;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #86efac;">جيد</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">طبيعي جدًا، لكن يبدو واضحًا أنه ذكاء اصطناعي عالي الجودة.</td>
      </tr>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #fde68a;">مقبول</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">مفهوم لكن فيه إيقاع آلي واضح.</td>
      </tr>
      <tr style="background: #111827;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #fb923c;">ضعيف</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">آلي جدًا؛ اللهجة أو "الإحساس السعودي" مفقود أو مشوه.</td>
      </tr>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #f87171;">سيء</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">غير طبيعي تمامًا؛ يبدو كآلة معطلة.</td>
      </tr>
    </tbody>
  </table>

  <!-- Clarity Table -->
  <h4 style="color: #38bdf8; margin-bottom: 10px;">٢. الوضوح (Clarity)</h4>
  <p style="margin-bottom: 10px; color: #cbd5e1;">هل كل الحروف والكلمات مفهومة وواضحة وصحيحة بدون تقطع</p>
  <table style="width:100%; border-collapse: collapse; direction: rtl;">
    <thead>
      <tr style="background: #0c1a2e; color: #38bdf8;">
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">الدرجة</th>
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">التقييم</th>
        <th style="padding: 10px 14px; border: 1px solid #312e81; text-align: right;">الوصف</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #a3e635;">ممتاز</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">كل كلمة واضحة تمامًا؛ لا يحتاج أي جهد للفهم.</td>
      </tr>
      <tr style="background: #111827;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #86efac;">جيد</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">معظم الكلمات واضحة؛ ربما مقطع واحد طفيف غير واضح.</td>
      </tr>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #fde68a;">مقبول</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">يمكن فهم الجملة لكن تحتاج تركيزًا.</td>
      </tr>
      <tr style="background: #111827;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #fb923c;">ضعيف</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">كثير من الكلمات غير واضحة أو منطوقة بشكل خاطئ؛ صعب المتابعة.</td>
      </tr>
      <tr style="background: #0f172a;">
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">⭐️</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right; color: #f87171;">سيء</td>
        <td style="padding: 9px 14px; border: 1px solid #1e293b; text-align: right;">غير مفهوم تمامًا؛ لا يمكن معرفة ما يُقال.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

# Custom CSS for Black, Blue, and Purple aesthetic
custom_css = """
    .gradio-container { background-color: #020617 !important; color: #f8fafc; }
    .container { max-width: 1100px; margin: auto; }
    .sentence-card {
        background: #0f172a;
        border-radius: 12px;
        padding: 25px;
        border: 1px solid #1e293b;
    }
    .arabic-text {
        font-size: 28px !important;
        direction: rtl;
        text-align: center;
        padding: 30px;
        background: #1e1b4b;
        border-radius: 10px;
        margin-bottom: 25px;
        border-right: 6px solid #a855f7;
        color: #f1f5f9;
    }
    .audio-block {
        background: #111827;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 4px solid #7c3aed;
    }
    .submit-area {
        margin-top: 40px;
        padding: 30px;
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 12px;
        text-align: center;
    }
    /* Navigation bar */
    .nav-bar { align-items: center; margin-top: 20px; background: #0f172a; padding: 12px 16px; border-radius: 10px; border: 1px solid #1e293b; }
    .sentence-counter { text-align: center; font-size: 16px; color: #c084fc; }
    /* Hide the tab nav bar — we drive navigation with our own buttons */
    .sentence-tabs > div:first-child { display: none !important; }
    /* Radio columns — label sits inside the box */
    .nat-radio, .clar-radio { padding: 12px !important; border-radius: 8px !important; background: #111827 !important; border: 1px solid #1e293b !important; }
    .nat-radio .gr-prose, .clar-radio .gr-prose { margin: 0 !important; padding: 0 !important; background: transparent !important; border: none !important; }
"""

def create_interface():
    # PURPLE THEME CONFIG
    theme = gr.themes.Default(
        primary_hue="purple",
        secondary_hue="violet",
        neutral_hue="slate"
    ).set(
        body_background_fill="#020617",
        block_background_fill="#0f172a",
        block_border_color="#1e293b",
        button_primary_background_fill="#7c3aed",
        button_primary_background_fill_hover="#6d28d9",
        button_primary_text_color="white",
        checkbox_label_background_fill_selected="#7c3aed",
        checkbox_border_color_selected="#7c3aed"
    )

    with gr.Blocks(css=custom_css, theme=theme) as demo:
        with gr.Column(elem_classes="container"):

            # Header
            with gr.Row():
                with gr.Column(scale=4):
                    gr.Markdown("# 🎙️ Arabic Voice Quality Evaluation")
                    gr.HTML(INSTRUCTIONS_HTML)

            with gr.Group():
                with gr.Row():
                    user_name = gr.Textbox(label="Evaluator Name", placeholder="Enter your full name", scale=2)
                    read_guidelines = gr.Checkbox(label="I have read the guidelines", scale=1)

            rating_components = []
            current_idx = gr.State(value=0)

            # Hidden-tab approach: Gradio pre-renders all tabs so audio/radio
            # components are properly mounted even before the user navigates to them.
            with gr.Tabs(selected=0, elem_classes="sentence-tabs") as tabs:
                for s_id in range(1, 11):
                    with gr.Tab(label=f"Sentence {s_id}", id=s_id - 1, elem_classes="sentence-card"):
                        gr.HTML(f"<div class='arabic-text'>{SENTENCES[s_id]}</div>")
                        for a_idx, audio_file in enumerate(DATA[s_id], 1):
                            with gr.Column(elem_classes="audio-block"):
                                gr.Markdown(f"**Sample {s_id}.{a_idx}**")
                                gr.Audio(f"audio/{s_id}/{audio_file}", show_label=False, container=False)
                                with gr.Row():
                                    with gr.Column(elem_classes="nat-radio"):
                                        gr.HTML("<label style='color:#a855f7; font-weight:bold; font-size:15px; display:block; margin-bottom:6px; direction:rtl;'>الطبيعية</label>")
                                        nat = gr.Radio(choices=STAR_CHOICES, label="", show_label=False)
                                    with gr.Column(elem_classes="clar-radio"):
                                        gr.HTML("<label style='color:#38bdf8; font-weight:bold; font-size:15px; display:block; margin-bottom:6px; direction:rtl;'>الوضوح</label>")
                                        clar = gr.Radio(choices=STAR_CHOICES, label="", show_label=False)
                                    rating_components.extend([nat, clar])

            # Navigation — below sentence content
            with gr.Row(elem_classes="nav-bar"):
                back_btn         = gr.Button("◀ السابق", size="sm", interactive=False)
                sentence_counter = gr.Markdown("**الجملة 1 من 10**", elem_classes="sentence-counter")
                next_btn         = gr.Button("التالي ▶", size="sm", variant="primary")

            # Submit — always visible
            with gr.Column(elem_classes="submit-area"):
                submit_btn = gr.Button("🚀 إرسال جميع التقييمات", variant="primary", size="lg")
                output_msg = gr.Markdown()

            def navigate(idx, direction):
                new_idx = max(0, min(9, idx + direction))
                is_first = new_idx == 0
                is_last  = new_idx == 9
                return (
                    new_idx,
                    f"**الجملة {new_idx + 1} من 10**",
                    gr.update(interactive=not is_first),
                    gr.update(interactive=not is_last),
                    gr.update(selected=new_idx),
                )

            nav_out = [current_idx, sentence_counter, back_btn, next_btn, tabs]
            back_btn.click(fn=lambda idx: navigate(idx, -1), inputs=[current_idx], outputs=nav_out)
            next_btn.click(fn=lambda idx: navigate(idx,  1), inputs=[current_idx], outputs=nav_out)

            submit_btn.click(
                fn=save_results,
                inputs=[user_name, read_guidelines] + rating_components,
                outputs=output_msg
            )

    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True)