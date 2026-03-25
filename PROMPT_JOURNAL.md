# AI Prompt Journal – Quant Learning Assistant

This journal contains reusable prompts for building, improving, debugging, and expanding the Quant Learning Assistant project.

Use these prompts with ChatGPT or another AI assistant whenever you want help writing code, generating content, improving structure, or fixing errors.

---

## Project Context Prompt

Use this prompt first when starting a new AI conversation so the model understands the project.

```text
I am building a project called Quant Learning Assistant.

It is a Python and Streamlit-based educational app for learning quantitative finance topics. The app loads content from a JSON file and displays structured information for each topic, including:
- explanation
- example
- common_mistake
- quiz

The goal is to help beginners and intermediate learners study quant finance concepts in a simple, interactive format. It is also meant to support preparation for WorldQuant Brain and broader quant learning.

The project currently uses:
- Python
- Streamlit
- JSON

Please keep all suggestions beginner-friendly, practical, and well-structured. When writing code, use clean Python conventions, helpful comments, and explanations.
```

---

## 1. Prompt for Generating New Quant Topics

```text
Generate [number] new quant finance topics for my Quant Learning Assistant project.

Each topic must follow this JSON structure exactly:

{
  "topic name": {
    "explanation": "A detailed but easy-to-understand explanation",
    "example": "At least 3 relevant examples",
    "common_mistake": "Common mistakes learners make",
    "quiz": [
      "Question 1",
      "Question 2"
    ]
  }
}

Requirements:
- Keep the explanations beginner-friendly
- Make the examples practical and finance-related
- Make the common mistakes realistic
- Make the quiz questions suitable for revision
- Return valid JSON only
```

---

## 2. Prompt for WorldQuant Brain-Specific Topics

```text
Generate [number] WorldQuant Brain-focused topics for my Quant Learning Assistant project.

Use this JSON structure:

{
  "topic name": {
    "explanation": "Detailed but simple explanation",
    "example": "At least 3 practical examples",
    "common_mistake": "Common mistakes learners make",
    "quiz": [
      "Question 1",
      "Question 2"
    ]
  }
}

Focus on concepts such as:
- delay
- decay
- turnover
- fitness
- Sharpe ratio
- neutralization
- alpha design
- overfitting
- ranking operators
- backtesting

Return valid JSON only.
```

---

## 3. Prompt for Simplifying Topic Explanations

```text
I have quant finance learning content for my project. Please simplify the explanation so that it is easier for a beginner to understand and memorize.

Keep the same topic meaning, but:
- use simpler English
- keep it accurate
- avoid unnecessary jargon
- make it sound like a study note
- preserve the JSON structure if provided
```

---

## 4. Prompt for Improving JSON Formatting

```text
Please review this JSON for my Quant Learning Assistant project.

Tasks:
- fix formatting issues
- ensure valid JSON syntax
- keep all topic content intact
- make sure every topic includes:
  - explanation
  - example
  - common_mistake
  - quiz
- return only the corrected JSON
```

---

## 5. Prompt for Writing Streamlit Code

```text
Create Streamlit code for my Quant Learning Assistant project.

Project details:
- The app loads quant topics from a JSON file
- Users should be able to select a topic
- The app should display:
  - topic title
  - explanation
  - examples
  - common mistakes
  - quiz questions

Requirements:
- Use clean Python code
- Follow beginner-friendly Streamlit conventions
- Add comments where useful
- Keep the UI simple and neat
- Separate logic cleanly if possible
```

---

## 6. Prompt for Debugging Python Errors

```text
I am working on a Python/Streamlit project called Quant Learning Assistant.

Please help me debug this error.

When responding:
- explain the cause of the error in simple terms
- show me how to fix it
- give corrected code if needed
- mention any related edge cases
- keep the explanation beginner-friendly

Here is the error:
[paste error here]

Here is the code:
[paste code here]
```

---

## 7. Prompt for Writing Function Docstrings

```text
Please write comprehensive Python docstrings for the following function(s).

Requirements:
- follow Python conventions
- include a clear description
- document all parameters with types and meanings
- document return values
- mention exceptions that may be raised
- include example usage
- include notes or edge cases if relevant

Here is the code:
[paste function here]
```

---

## 8. Prompt for README Generation

```text
Create a professional README.md file for my project.

Project name: Quant Learning Assistant

Project description:
A Python and Streamlit app that helps users learn quant finance topics using JSON-based structured content such as explanations, examples, common mistakes, and quizzes.

Include:
- project title
- overview
- features
- technologies used
- installation instructions
- usage examples
- project structure
- configuration options
- troubleshooting
- contribution guidelines
- license section

Keep it clean, professional, and beginner-friendly.
```

---

## 9. Prompt for Code Refactoring

```text
Please refactor this code from my Quant Learning Assistant project.

Goals:
- improve readability
- improve maintainability
- keep the logic the same
- follow Python best practices
- make it beginner-friendly
- add comments only where helpful

Here is the code:
[paste code here]
```

---

## 10. Prompt for Adding Search Functionality

```text
I want to add search functionality to my Streamlit-based Quant Learning Assistant.

Current app behavior:
- loads topics from a JSON file
- shows topic content after selection

Please help me add:
- a search box
- partial matching for topic names
- clean UI behavior
- beginner-friendly implementation

Provide full code and explain how it works.
```

---

## 11. Prompt for Building Quiz Features

```text
Help me add quiz functionality to my Quant Learning Assistant project.

Current structure:
- each topic contains a quiz list in JSON
- the app currently only displays the questions

I want to improve it by adding:
- a quiz section in Streamlit
- optional answer input
- score tracking
- feedback for correct or incorrect answers

Keep the code simple, clear, and beginner-friendly.
```

---

## 12. Prompt for Topic Recommendations

```text
I want my Quant Learning Assistant to recommend what topic a learner should study next.

Please suggest a simple recommendation system based on:
- beginner to advanced progression
- topic dependencies
- WorldQuant Brain relevance

Return:
- a suggested learning order
- logic for recommendations
- optional Python code implementation
```

---

## 13. Prompt for Creating Practice Plans

```text
Create a 2-week study plan using the topics from my Quant Learning Assistant project.

Requirements:
- beginner-friendly
- daily structure
- balance theory and review
- include quiz/revision checkpoints
- connect learning to quant finance and WorldQuant Brain where relevant
```

---

## 14. Prompt for Improving UI/UX

```text
Please suggest UI/UX improvements for my Streamlit project called Quant Learning Assistant.

Current app:
- loads quant topics from JSON
- displays explanations, examples, mistakes, and quizzes

I want suggestions for:
- better layout
- improved readability
- better navigation
- study-friendly design
- beginner-friendly interface

If possible, include sample Streamlit code.
```

---

## 15. Prompt for Creating Test Cases

```text
Help me create test cases for my Quant Learning Assistant project.

Important functions include:
- loading JSON topics
- retrieving a topic by name
- handling empty input
- handling missing files
- handling invalid JSON

Please provide:
- unit test ideas
- example pytest code
- explanation of what each test checks
```

---

## 16. Prompt for Generating Better Examples

```text
Please improve the examples for this quant topic.

Requirements:
- give at least 3 examples
- make them practical and finance-related
- make them easy for a beginner to understand
- avoid vague examples
- keep the tone educational

Here is the topic content:
[paste topic here]
```

---

## 17. Prompt for Common Mistakes Section

```text
For each quant topic I provide, generate a strong 'common_mistake' section.

Requirements:
- mention realistic beginner mistakes
- explain why each mistake matters
- make the writing clear and concise
- keep the explanation relevant to quant finance learning

Here is the topic:
[paste topic here]
```

---

## 18. Prompt for Turning Notes into JSON

```text
Convert my study notes into the JSON format used by my Quant Learning Assistant project.

Required format:

{
  "topic name": {
    "explanation": "...",
    "example": "...",
    "common_mistake": "...",
    "quiz": [
      "...",
      "..."
    ]
  }
}

Please:
- organize messy notes clearly
- improve clarity
- preserve important meaning
- return valid JSON only

Here are my notes:
[paste notes here]
```

---

## 19. Prompt for Git/GitHub Help

```text
I am working on my Quant Learning Assistant project and need help with Git/GitHub.

Please explain the issue in simple terms and tell me exactly what commands to run.

Current issue:
[paste issue here]

Please include:
- the cause
- the fix
- the exact commands
- any warnings about mistakes to avoid
```

---

## 20. Prompt for Production Improvement Ideas

```text
My project is currently a beginner-friendly Python/Streamlit app for learning quant finance topics from JSON.

Please suggest the best next improvements if I want to make it more polished and portfolio-ready.

Focus on:
- code quality
- UI improvements
- better project structure
- testing
- deployment
- user experience
- content quality
- GitHub presentation
```

---

## Best Practices for Using This Journal

- Reuse prompts instead of rewriting the same request every time
- Add your best prompts as the project grows
- Save prompts that gave especially useful outputs
- Keep prompts specific for better AI responses
- Ask for “valid JSON only” whenever generating JSON content
- Ask for “beginner-friendly” when you want simpler explanations
- Ask for “production-ready” when you want stronger coding practices

---

## Suggested File Name

Save this file as:

```text
PROMPT_JOURNAL.md
```

---

## Suggested Future Additions

As the project grows, you can add prompts for:

- deployment to Streamlit Cloud
- user authentication
- progress tracking
- flashcards
- spaced repetition
- note-taking features
- admin tools for editing topics
- topic tagging and filtering
- export to PDF
- analytics/dashboard features
