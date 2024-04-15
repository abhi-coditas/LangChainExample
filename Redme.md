# Chatbot using Ollama Language Model

## Introduction

This project features a simple chatbot leveraging the Ollama language model and the StrOutputParser function to provide responses to user queries. It specializes in addressing common questions related to technical document writing, offering insights on crafting documentation for various programming languages and tools.

## How to Run the Project

1. Install the required dependencies by executing:
   ```
   pip install -r requirements.txt
   ```

2. Run the project with the command:
   ```
   python app.py
   ```

3. Input a question in the terminal, and the chatbot will generate a response based on its training data.

## Files and Folders

- **app.py**: This main file defines the chatbot's functionality, incorporating the language model instance, output parser function, chat prompt template, and pipe chain.

- **Ollama**: A library featuring a pre-trained language model for generating responses to user input.

- **StrOutputParser**: A library offering a simple function to parse the generated response from the language model and return it as a string.

- **langchain_core**: A package containing the ChatPromptTemplate class and other core components essential for building chatbots.

- **langchain_community**: A package comprising pre-trained language models and other community-contributed resources for chatbot development.

- **requirements.txt**: Specifies the dependencies required to execute the project, including Ollama and StrOutputParser.

## Technologies Used

- **Python 3.x**
- **Ollama**: Pre-trained language model for generating responses to user input.
- **StrOutputParser**: Function for parsing generated responses and converting them into strings.
- **langchain_core**: Package containing essential components for chatbot development.
- **langchain_community**: Package with pre-trained models and community-contributed resources.