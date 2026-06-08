# 🇸🇦 Wittify-MOS-Collector: Saudi TTS Benchmarking Framework

An enterprise-grade evaluation suite for the **Subjective Quality Assessment** of Saudi Arabic Text-to-Speech (TTS) architectures. This framework facilitates a standardized **Mean Opinion Score (MOS)** collection process to benchmark the **Wittify Saudi TTS** model against leading regional competitors.

---

## 🎯 Benchmarking Objective

The primary objective of this study is to quantify human-perceived naturalness and dialectal accuracy across the most prominent Saudi-specific TTS models. By employing a controlled, blind-test environment, the framework eliminates brand bias and focuses strictly on phonetic precision, prosodic fluidity, and regional authenticity.

### 🤖 Evaluated Architectures
The benchmark evaluates five distinct state-of-the-art systems:
* **Fasee7 TTS** (Proprietary Candidate)
* **Habibi TTS**
* **Namaa TTS**
* **Hamsa TTS**
* **Silma TTS (Large)**

---

## 🧪 Experimental Methodology

The collector utilizes a **Grouped Comparative Design** with rigorous controls to ensure statistical integrity:

* **Standardized Stimuli:** 10 Saudi Arabic sentences covering diverse phonetic and syntactic contexts.
* **Blind Protocol (Double-Blind):** To eliminate cognitive bias, evaluators are not informed of the model identities. All samples are presented as anonymous options.
* **Dynamic Randomization:** The mapping of models to audio slots (e.g., Audio 1, Audio 2) is **randomized per sentence**. 
    > **Note:** Model A may appear as the first audio in Sentence 1, but may shift to the fourth audio in Sentence 2. This prevents "positional bias" and ensures the evaluator remains focused on audio quality rather than pattern recognition.
* **Target Demographic:** Evaluation is restricted to native Saudi Arabic speakers to ensure authentic validation of local nuances.

---

## 📂 Data Architecture

The system is designed to traverse a partitioned directory structure. Each sub-directory represents a single linguistic prompt containing five model-generated variations:

```text
/audios
├── 1/                  # Sentence ID #1
│   ├── model_1.wav     # Randomized internally
│   ├── model_2.wav     
│   ├── model_3.wav     
│   ├── model_4.wav     
│   └── model_5.wav     
├── ...
└── 10/                 # Sentence ID #10
```

---

## ✨ System Features

* **Comparative Playback Interface:** Allows evaluators to toggle seamlessly between model outputs for the same sentence to identify subtle prosodic variances.
* **Automated Scoring Pipeline:** Real-time data serialization into structured `.csv` format for immediate downstream statistical analysis.

---

## 🛠️ Deployment & Usage

### 1. Environment Configuration
```bash
# Clone the repository
git clone https://github.com/noursamy-cell/Wittify-MOS-Collector.git
cd Wittify-MOS-Collector

# Initialize virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Execution
```bash
python app.py
```

---

## 📈 Evaluation Framework

Evaluators rate each audio sample on two independent dimensions using a 1–5 star scale. Please read the criteria carefully before rating.

### 1. Naturalness (الطبيعية)
Does the voice sound human in its rhythm, tone, and emotional feel — or robotic?

| Stars | Rating | Description |
| :--- | :--- | :--- |
| ⭐⭐⭐⭐⭐ | **Excellent** | Completely natural; indistinguishable from a native Saudi speaker. |
| ⭐⭐⭐⭐ | **Good** | Very natural, but clearly high-quality AI. |
| ⭐⭐⭐ | **Acceptable** | Understandable, but the rhythm is not entirely clear. |
| ⭐⭐ | **Weak** | Very robotic; the Saudi dialect or emotional feel is missing or distorted. |
| ⭐ | **Bad** | Completely unnatural; sounds like a broken machine. |

### 2. Clarity (الوضوح)
Are all letters and words clear, correctly pronounced, and uninterrupted?

| Stars | Rating | Description |
| :--- | :--- | :--- |
| ⭐⭐⭐⭐⭐ | **Excellent** | Every word is perfectly clear; no effort needed to understand. |
| ⭐⭐⭐⭐ | **Good** | Most words are clear; perhaps one segment is slightly unclear. |
| ⭐⭐⭐ | **Acceptable** | The sentence can be understood but requires some focus. |
| ⭐⭐ | **Weak** | Many words are unclear or mispronounced; difficult to follow. |
| ⭐ | **Bad** | Completely incomprehensible; impossible to know what is being said. |

---

## 🛡️ Confidentiality & Rights
**Proprietary & Confidential.** This benchmarking tool is a product of **Wittify Ai**. All audio samples and collected datasets are intended for internal performance auditing and model optimization purposes.
