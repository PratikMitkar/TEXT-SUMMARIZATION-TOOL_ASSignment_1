import streamlit as st
from transformers import pipeline

# Function to summarize text
def summarize_text(input_text, max_length=130, min_length=30):
    """Summarizes the input text using a pre-trained NLP model."""
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    # Generate summary
    summary = summarizer(
        input_text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]['summary_text']

# Streamlit app
st.title("Text Summarization Tool")
st.write("Enter your text below, and the tool will generate a summary.")

# User input
def main():
    input_text = st.text_area("Input Text:", height=200)

    # Parameters for summarization
    max_length = st.slider("Max Length:", min_value=50, max_value=300, value=130, step=10)
    min_length = st.slider("Min Length:", min_value=10, max_value=100, value=30, step=5)

    # Button to generate summary
    if st.button("Summarize"):
        if len(input_text.strip()) == 0:
            st.error("Please enter some text to summarize.")
        else:
            st.write("Generating summary...")
            try:
                # Summarize the text
                summary = summarize_text(input_text, max_length=max_length, min_length=min_length)
                st.subheader("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")

if __name__ == "__main__":
    main()
