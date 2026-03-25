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

* **Standardized Stimuli:** 10 curated Saudi Arabic linguistic prompts covering diverse phonetic and syntactic contexts.
* **Blind Protocol (Double-Blind):** To eliminate cognitive bias, evaluators are not informed of the model identities. All samples are presented as anonymous "Options."
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

* **Non-Linear Randomization Engine:** Decouples file naming from playback order to maintain a strictly blind testing environment.
* **Comparative Playback Interface:** Allows evaluators to toggle seamlessly between model outputs for the same sentence to identify subtle prosodic variances.
* **Localized UX/UI:** Interface optimized for Right-to-Left (RTL) Arabic typography and Saudi-specific instructional sets.
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
**Access Endpoint:** `http://localhost:5000`

---

## 📈 Evaluation Framework

Evaluators rate samples on a 1–5 scale based on the **ITU-T P.800** standards:

| Score | Quality | Saudi Dialect Criteria |
| :--- | :--- | :--- |
| **5** | **Excellent** | Indistinguishable from a native Saudi speaker. |
| **4** | **Good** | Clear Saudi accent; minor artificial prosody or cadence. |
| **3** | **Fair** | Understandable; slightly "robotic" or generic MSA feel. |
| **2** | **Poor** | Significant mispronunciation of Saudi-specific phonemes. |
| **1** | **Bad** | Unintelligible or completely unnatural prosodic structure. |

---

## 🛡️ Confidentiality & Rights
**Proprietary & Confidential.** This benchmarking tool is a product of **Wittify Ai**. All audio samples and collected datasets are intended for internal performance auditing and model optimization purposes.
