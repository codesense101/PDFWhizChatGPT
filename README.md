# PDFWhizChatGPT

PDFWhizChatGPT is a Language Model (LLM) powered chat application designed for interacting with PDF documents. It leverages the Langchain framework and Streamlit for a seamless and user-friendly experience.

## Features

- **Upload PDFs:** Easily upload your PDF documents through the user-friendly interface.
- **Automatic Text Extraction:** PDF content is automatically extracted, making it ready for interaction.
- **Vector Store:** Efficiently manages and stores document embeddings using Langchain's FAISS and OpenAI Embeddings.
- **Question and Answer:** Users can input questions related to the PDF content, and the chatbot powered by OpenAI's gpt-3.5-turbo provides accurate responses.
- **Persistent Storage:** Embeddings are computed and stored locally for faster access in subsequent interactions.

## How to Use

1. Upload a PDF file.
2. Ask questions related to the content of the PDF.
3. Receive accurate and contextually relevant answers.

## Dependencies

- Streamlit
- Langchain
- PyPDF2
- OpenAI GPT-3.5-turbo ## Any desired LLM model
- Streamlit Extras
- Python-dotenv

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure your LLM model. [Optional, Default: gpt-3.5-turbo]
4. Set up your OpenAI API key in a `.env` file.

## Run the Application

```bash
streamlit run your_app_filename.py
```

## Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.

## Credits
Streamlit: [Streamlit](https://streamlit.io/)
Langchain: [Langchain](https://langchat.github.io/)
OpenAI: [OpenAI](https://openai.com/)

## Author
This project is developed with :heart: by Codesense101.

## License
This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE).

## Acknowledgments
Special thanks to [PromptEngineering](https://www.youtube.com/@engineerprompt) for their tutorials.
