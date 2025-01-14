import google.generativeai as genai

# Configure the API key
api_key = "####"
genai.configure(api_key=api_key)

# Select the Gemini model to use
model = genai.GenerativeModel("gemini-1.5-flash")

# 1. Text Generation
def text_generation(prompt):
    print("\n### Text Generation ###")
    response = model.generate_content(prompt)
    print(f"Prompt: {prompt}\nResponse: {response.text}\n")

# 2. Text Summarization
def text_summarization(long_text):
    print("\n### Text Summarization ###")
    summarization_prompt = f"Summarize this: {long_text}"
    response = model.generate_content(summarization_prompt)
    print(f"Original Text: {long_text}\nSummary: {response.text}\n")

# 3. Question Answering
def question_answering(context, question):
    print("\n### Question Answering ###")
    qa_prompt = f"Context: {context}\nQuestion: {question}"
    response = model.generate_content(qa_prompt)
    print(f"Context: {context}\nQuestion: {question}\nAnswer: {response.text}\n")

# 4. Sentiment Analysis
def sentiment_analysis(text):
    print("\n### Sentiment Analysis ###")
    sentiment_prompt = f"Analyze the sentiment of this text: {text}"
    response = model.generate_content(sentiment_prompt)
    print(f"Text: {text}\nSentiment: {response.text}\n")

# Example Usage
if __name__ == "__main__":
    # Text Generation Example
    text_generation("Explain how AI works.")

    # Text Summarization Example
    long_text = (
        "Artificial Intelligence (AI) is the simulation of human intelligence processes "
        "by machines, especially computer systems. These processes include learning, reasoning, "
        "and self-correction. Applications of AI include expert systems, natural language processing, "
        "speech recognition, and machine vision."
    )
    text_summarization(long_text)

    # Question Answering Example
    context = (
        "Artificial Intelligence (AI) is a branch of computer science dealing with the creation of smart machines "
        "that can perform tasks typically requiring human intelligence. AI is used in various applications, such as "
        "autonomous vehicles, healthcare diagnostics, and financial trading."
    )
    question = "What is AI used for?"
    question_answering(context, question)

    # Sentiment Analysis Example
    sentiment_analysis("I absolutely love using this AI tool! It makes my work so much easier.")
