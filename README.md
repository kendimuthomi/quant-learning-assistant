# Quant Learning Assistant

A beginner-friendly learning application for studying quantitative finance concepts through structured topic content, practical examples, common mistakes, and quiz questions.

The Quant Learning Assistant is designed to help learners build a strong foundation in quant finance by organizing important topics into an easy-to-use format. It is especially useful for self-study, revision, and building domain familiarity for platforms such as WorldQuant Brain.

---

## Overview

Quantitative finance can feel overwhelming because it combines mathematics, statistics, finance, and programming. This project simplifies that process by presenting quant topics in a structured and interactive format.

The application loads topic content from a JSON file and displays detailed explanations, examples, common mistakes, and quiz questions. This makes it useful both as a study tool and as a lightweight educational app.

---

## Features

- Structured quant learning topics stored in JSON format
- Detailed explanations for each topic
- Multiple examples per topic
- Common mistakes section for better conceptual clarity
- Quiz questions for self-testing
- Simple topic lookup functionality
- Lightweight Python-based architecture
- Streamlit-friendly design for interactive UI integration
- Easy to expand by adding new topics to the JSON file
- Suitable for quant beginners and intermediate learners

---

## Example Topics

The project can include topics such as:

- Probability and Random Variables
- Statistics and Data Analysis
- Time Series Analysis
- Linear Algebra for Quant Finance
- Calculus and Optimization
- Risk and Return
- Portfolio Theory
- Factor Models
- Alpha Signals and Backtesting
- Market Microstructure
- Delay
- Decay
- Neutralization
- Turnover
- Fitness
- Sharpe Ratio
- Rank Operators
- Winsorization and Outlier Control
- Correlation Between Alphas
- Overfitting in Alpha Research

---

## Technologies Used

This project is built using:

- **Python**
- **Streamlit**
- **JSON**
- Standard Python libraries such as:
  - `json`
  - `os` (optional, depending on your implementation)
  - `pathlib` (optional, recommended for cleaner file handling)

---

## Installation Requirements

Before running the project, make sure you have the following installed:

- Python 3.10 or newer
- `pip` package manager
- Streamlit

Optional but recommended:

- A virtual environment tool such as `venv`

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/quant-learning-assistant.git
cd quant-learning-assistant
```

### 2. Create and activate a virtual environment

#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit
```

If you later add a `requirements.txt` file, install with:

```bash
pip install -r requirements.txt
```

---

## Project Structure

A possible project structure for this app looks like this:

```text
quant-learning-assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── data/
│   └── topics.json
├── utils/
│   └── topic_loader.py
└── assets/
    └── optional_images_or_styles/
```

### Structure Explanation

- **`app.py`**  
  Main Streamlit application file. Handles UI rendering and user interaction.

- **`data/topics.json`**  
  Stores structured learning content for all quant topics.

- **`utils/topic_loader.py`**  
  Contains helper functions such as:
  - `load_topics()`
  - `get_topic_data()`

- **`requirements.txt`**  
  Lists project dependencies.

- **`README.md`**  
  Project documentation.

---

## JSON Topic Format

The application expects topic data in a structure like this:

```json
{
  "probability and random variables": {
    "explanation": "Detailed explanation of the topic.",
    "example": "1. Example one\n2. Example two\n3. Example three",
    "common_mistake": "Common mistakes learners make.",
    "quiz": [
      "Question 1?",
      "Question 2?"
    ]
  }
}
```

### Important Notes

- Topic keys should ideally be stored in **lowercase** if your lookup function uses `.lower()`.
- Each topic should contain:
  - `explanation`
  - `example`
  - `common_mistake`
  - `quiz`

---

## Basic Usage

### Run the Streamlit app

```bash
streamlit run app.py
```

After running the command, Streamlit will open the application in your browser, usually at:

```text
http://localhost:8501
```

---

## Example Python Usage

If you are using helper functions like the ones you shared earlier:

```python
import json


def load_topics(file_path="data/topics.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_topic_data(topic, file_path="data/topics.json"):
    if not topic or not topic.strip():
        return None

    topics = load_topics(file_path)
    return topics.get(topic.strip().lower())
```

### Example

```python
topics = load_topics()
print(topics.keys())

topic_data = get_topic_data("sharpe ratio")
print(topic_data)
```

---

## Streamlit Usage Example

A simple Streamlit integration may look like this:

```python
import streamlit as st
from utils.topic_loader import load_topics, get_topic_data

st.title("Quant Learning Assistant")

topics = load_topics()
topic_names = list(topics.keys())

selected_topic = st.selectbox("Choose a topic", topic_names)

if selected_topic:
    data = get_topic_data(selected_topic)
    if data:
        st.header(selected_topic.title())
        st.subheader("Explanation")
        st.write(data["explanation"])

        st.subheader("Examples")
        st.write(data["example"])

        st.subheader("Common Mistake")
        st.write(data["common_mistake"])

        st.subheader("Quiz")
        for i, question in enumerate(data["quiz"], start=1):
            st.write(f"{i}. {question}")
```

---

## Configuration Options

You can customize the project in several ways:

### 1. Change the data source path

By default, topic data is loaded from:

```python
data/topics.json
```

You can change this by passing a different file path:

```python
topics = load_topics("data/custom_topics.json")
```

### 2. Add new quant topics

Simply update `topics.json` with additional topic entries following the expected structure.

### 3. Customize topic matching

If needed, you can improve topic lookup by:

- supporting uppercase/lowercase automatically
- allowing aliases or synonyms
- adding fuzzy matching for misspelled topic names

### 4. Expand UI behavior

Possible enhancements include:

- search bar for topics
- quiz scoring
- topic categories
- progress tracking
- bookmarks/favorites
- dark mode styling
- export notes functionality

---

## Troubleshooting

### 1. `FileNotFoundError`

**Problem:**  
The app cannot find `data/topics.json`.

**Solution:**  
Make sure the file exists and the path is correct relative to your project root.

Example:
```bash
quant-learning-assistant/
└── data/
    └── topics.json
```

---

### 2. `json.JSONDecodeError`

**Problem:**  
The JSON file is not formatted correctly.

**Solution:**  
Validate your JSON using:
- an online JSON validator, or
- Python tools before running the app

Common issues include:
- missing commas
- trailing commas
- unclosed brackets
- invalid quotes

---

### 3. Topic lookup returns `None`

**Problem:**  
The topic exists in the JSON file but is not being found.

**Possible causes:**
- topic keys in the JSON are not lowercase
- extra spaces in the input
- mismatch between displayed names and stored keys

**Solution:**  
Store topic keys consistently, preferably in lowercase:
```json
"sharpe ratio": { ... }
```

---

### 4. Streamlit app does not start

**Problem:**  
Running `streamlit run app.py` fails.

**Solution:**  
Check that Streamlit is installed:

```bash
pip install streamlit
```

You can also verify installation:

```bash
streamlit --version
```

---

### 5. Import errors for helper modules

**Problem:**  
Python cannot import files from `utils/`.

**Solution:**  
Make sure:
- the folder structure is correct
- your current working directory is the project root
- filenames are correct

---

## Edge Cases and Developer Notes

- If `topic` is empty or contains only whitespace, `get_topic_data()` returns `None`.
- If `topic` is not a string, `.strip()` may raise an error unless type checks are added.
- If the JSON root object is not a dictionary, downstream logic may fail.
- If topic names in the UI are title-cased but stored in lowercase, normalize them before lookup.
- For production use, consider adding:
  - exception handling
  - schema validation for the JSON file
  - logging
  - unit tests

---

## Future Improvements

Some useful next steps for the project:

- Add topic categories such as math, statistics, portfolio theory, and WorldQuant Brain concepts
- Add quiz scoring and answer validation
- Add search and filtering
- Add progress tracking for learners
- Add support for flashcards
- Add user notes per topic
- Add downloadable study summaries
- Add separate beginner/intermediate/advanced levels
- Add topic recommendation logic based on learning goals

---

## Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your updates
5. Submit a pull request

### Suggested contribution areas

- Improve topic content quality
- Add new quant concepts
- Improve UI/UX in Streamlit
- Add tests
- Improve JSON validation
- Add better search and filtering
- Improve documentation

### Basic contribution guidelines

- Keep code readable and well-documented
- Follow Python naming conventions
- Write clear commit messages
- Test new features before submitting
- Maintain consistent JSON topic structure

---

## License

This project is licensed under the **MIT License** unless otherwise specified.

You can add a `LICENSE` file with the full MIT license text if you want to make this official.

Example:

```md
MIT License

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

If you prefer another license, such as Apache 2.0 or GPL, update this section accordingly.

---

## Who This Project Is For

This project is useful for:

- Students learning quant finance
- Beginners exploring WorldQuant Brain concepts
- Developers building educational finance apps
- Anyone who wants structured revision material for quant topics

---

## Summary

The Quant Learning Assistant is a simple but flexible project for learning quantitative finance concepts through structured JSON-based content and a lightweight Python/Streamlit interface. It is easy to extend, beginner-friendly, and a strong foundation for a larger educational tool.
