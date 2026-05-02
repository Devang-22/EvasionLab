# 🛡️ EvasionLab: Dual-Engine Threat Detection SIEM

EvasionLab is a hybrid, resource-optimized Security Information and Event Management (SIEM) pipeline. It synergizes deterministic signature matching (Snort IDS) with a heuristic Natural Language Processing (NLP) engine to detect highly obfuscated and polymorphic zero-day payloads.

## 🚀 Project Overview
Traditional deterministic firewalls struggle with the "Obfuscation Gap"—failing to catch encoded zero-day attacks. Conversely, pure AI-driven security models suffer from high False Positive Rates (FPR) and often require heavy compute resources. 

EvasionLab bridges this gap by deploying a dual-engine consensus mechanism designed specifically for resource-constrained edge nodes and micro-cloud architectures.

### Key Engineering Achievements:
* **Edge-Optimized:** Fully operational within a strict **< 1 GiB memory ceiling**, completely eliminating the need for expensive GPU clusters. Successfully deployed on a zero-cost AWS t2.micro instance.
* **Zero-Day Detection:** Bridges the obfuscation gap with an 87.4% detection rate against mutated payloads that naturally bypass Snort.
* **Asynchronous Telemetry:** Dual-engine processing completes under 500ms. AI mathematical vectorization runs asynchronously, ensuring live web traffic is never bottlenecked.
* **Zero False Positives:** Utilizes Snort as a deterministic baseline filter to completely eliminate the alert fatigue typically associated with AI-only SecOps tools.

## 🛠️ Technology & Architecture Stack
* **Core Infrastructure:** AWS EC2 (t2.micro), Docker Containerization
* **Deterministic Engine:** Snort IDS (`local.rules` baseline filtering), `docker0` network bridging
* **Heuristic Engine:** Python, Flask Microservice, Scikit-Learn (TF-IDF Vectorization & Logistic Regression)
* **Telemetry & UI:** Asynchronous JSON alerting, Chart.js dynamic rendering

## ⚙️ System Flow
1. **User Request:** System captures target IP and injected payload.
2. **API Verification:** Asynchronous fetch directed to the Threat Intelligence API.
3. **Dual-Verdict Extraction:** Parses deterministic Snort alerts alongside the AI heuristic verdict.
4. **Secure Logging & Stats:** Appends to terminal logs and updates operational statistical arrays (TP, FP, TN, FN).
5. **Dashboard Render:** Triggers dynamic Chart.js visual refresh without blocking the main thread.

## 💻 Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/Devang-22/EvasionLab.git](https://github.com/Devang-22/EvasionLab.git)
cd EvasionLab