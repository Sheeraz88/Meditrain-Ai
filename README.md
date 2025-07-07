# MediTrain - Medical Chatbot

## Overview

MediTrain is an AI-powered medical assistant designed to provide users with accurate, empathetic, and clear answers to medical queries. Built using decision tree classifier models and flask, MediTrain emphasizes user-friendly interactions while ensuring that users are reminded to seek professional healthcare advice for proper diagnosis and treatment.

## Features

* **Conversational Context** : Retains the context of recent interactions to provide relevant and cohesive responses.
* **Medical Focus** : Tailored to assist with general medical questions while avoiding direct diagnoses.
* **Flask** : Intuitive and interactive web-based interface for seamless user interaction.
* **Empathetic Responses** : Ensures responses are clear, considerate, and accurate.

## Prerequisites

To run MediTrain locally, ensure you have the following:

* Python 3.8+
* Libraries specified in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Sheeraz88/Meditrain-Ai.git
   cd MediTrain-Chatbot
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Open the application in your browser 
3. Interact with MediTrain by typing your medical queries in the input box.

## Project Structure

* **`app.py`** : Main flask application script.
* **`requirements.txt`** : List of required Python packages.
* **`.env`** : Environment file containing sensitive API keys (not included in the repository).

## Key Libraries

* **Flask** : For building the user interface.
* **Python-dotenv** : For managing environment variables.

## Important Notes

* MediTrain is designed as a medical assistant but does not provide medical diagnoses or treatment plans.
* Always consult a certified healthcare professional for medical concerns.

## Future Enhancements

* Add support for multilingual queries.
* Enhance conversation memory to retain context over extended sessions.
* Introduce additional models for region-specific medical advice.

## License

This project is licensed under the MIT License.

---

Enjoy using MediTrain and let us know if you have suggestions or encounter issues!

