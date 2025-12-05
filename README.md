# Text to Math Problem Solver  
A simple Streamlit application that converts plain English math problems into detailed, step-by-step solutions using **LangChain**, **Groq LLM**

---

## 🚀 Features
- Convert any text-based math problem into a structured, point-wise solution  
- Uses **ChatGroq** with **Llama-3.1-8B-Instant** (fast + accurate)  
- Clean UI built with Streamlit  
- Simple chain architecture: **Prompt → LLM → Output Parser**  

---

## Tech Stack
- **Python 3.10+**
- **Streamlit**
- **LangChain**
- **LangChain-Groq**
- **Llama-3.1-8B-Instant Model**

---

## 🔑 Groq API Key
This app uses the Groq API for running LLM model.
---
## ▶️ How to Run the App

### 1. Clone this repository
```bash
git clone https://github.com/sush-sp777/Text-to-Math-Problem-Solver.git
cd Text-to-Math-Problem-Solver
```
### 2.Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit app
```bash
streamlit run app.py
```
---
## How It Works:
- The app uses a simple but powerful LangChain pipeline:
- PromptTemplate → ChatGroq Model → StrOutputParser
- The prompt guides the model to:
1. Understand the math problem
2. Solve it logically
3. Explain the steps clearly
4. Provide a final answer
