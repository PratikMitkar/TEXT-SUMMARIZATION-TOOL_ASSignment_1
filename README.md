# TEXT-SUMMARIZATION-TOOL_Assignment_1

**COMPANY**: CODTECH IT Solutions

**NAME**: Pratik Mitkar

**INTERN ID**: CT08GJB

**DOMAIN**: Artificial Intelligence

**BATCH DURATION**: January 5st, 2025 to February 5th, 2025

**MENTOR NAME**: NEELA SANTHOSH

**ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS**:

The Text Summarization Tool is a project aimed at simplifying and condensing lengthy pieces of text into concise summaries using state-of-the-art natural language processing techniques. The project employs a pre-trained model from Hugging Face's Transformers library, specifically the `sshleifer/distilbart-cnn-12-6` model, to ensure accurate and meaningful summaries.

As part of this project, a web-based interface was developed using Streamlit, a Python framework for creating user-friendly web applications. The interface allows users to input large bodies of text and generate summaries in real-time. Key features include adjustable parameters for maximum and minimum lengths of the summary, ensuring flexibility and customization for various use cases.

The development process involved several key tasks:
1. **Understanding Summarization Models**: Studied the architecture and working of the DistilBART model, a distilled version of the BART transformer, optimized for summarization tasks.
2. **Model Integration**: Integrated the summarization pipeline from the Hugging Face library into the backend of the tool.
3. **Building the User Interface**: Designed and implemented an interactive UI using Streamlit, enabling users to input text, adjust parameters, and view summaries.
4. **Error Handling and Testing**: Implemented robust error-handling mechanisms to manage edge cases such as empty inputs or excessively long texts. Rigorous testing was conducted to ensure the tool's reliability and accuracy.

The tool's capabilities extend beyond basic summarization. It offers:
- Seamless integration of NLP technologies for real-world applications.
- A responsive and intuitive interface for users with minimal technical expertise.
- Scalability for handling texts of varying lengths and complexities.

This project provided hands-on experience with modern NLP tools and frameworks. It enhanced my understanding of transformer-based models and their practical applications. Additionally, it improved my skills in Python programming, web development using Streamlit, and working with machine learning models in production environments.

Future enhancements for this tool include:
- Incorporating support for multiple languages to broaden its usability.
- Adding advanced features such as sentiment analysis and keyword extraction.
- Optimizing performance for faster processing of large datasets.

Overall, the Text Summarization Tool demonstrates the potential of NLP technologies in automating and streamlining text processing tasks, making it a valuable asset for individuals and organizations alike.

---

## Installation Details

To run the Text Summarization Tool, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/PratikMitkar/TEXT-SUMMARIZATION-TOOL_Assignment_1.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd TEXT-SUMMARIZATION-TOOL_Assignment_1
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit Application**:
   ```bash
   streamlit run task1.py
   ```

6. **Access the Application**:
   Open the provided URL (e.g., `http://localhost:8501`) in your web browser.

By following these steps, you will have the Text Summarization Tool up and running on your local machine.
