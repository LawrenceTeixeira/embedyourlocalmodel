# Python code to Convert Text into an Embedding Using the Local Model

## Description
This Python script is designed to automate the process of updating text embeddings for articles stored in a Microsoft SQL database. It retrieves articles that lack embeddings, generates new embeddings using an external model through an API call, and then updates the database with these new embeddings. This process ensures that all articles have up-to-date embeddings for use in various text analysis and machine learning applications.

## Requirements
- **Python Version:** Python 3.7 or newer.
- **External Libraries:**
  - `pyodbc`: To connect and execute SQL commands in a Microsoft SQL database.
  - `requests`: To make HTTP requests to an external API.
  - `numpy`: For handling numerical operations on arrays.
  - `scikit-learn`: Specifically, the `normalize` function to normalize data.
  - `python-dotenv`: To load environment variables from a `.env` file.
  - `json`: For JSON parsing and output.
- **Additional Components:**
  - **SQL Database:** A Microsoft SQL database accessible via a connection string stored in an environment variable.
  - **API Endpoint:** An API capable of returning text embeddings, expected to be running at `http://localhost:11434/api/embeddings`.

## Setup Instructions
1. **Install Required Libraries:**
   Ensure all required Python libraries are installed. You can install these using pip:
   ```bash
   pip install pyodbc requests numpy scikit-learn python-dotenv
   ```
2. **Environment Setup:**
   Create a `.env` file in the root directory of your project with the following content:
   ```plaintext
   MSSQL=<Your Connection String Here>
   ```
   Replace `<Your Connection String Here>` with the actual connection string to your Microsoft SQL database.

3. **Database Preparation:**
   The SQL database should contain a table named `wikipedia_articles_embeddings` with at least the following columns: `id`, `title`, `text`, `title_vector`, and `content_vector`. Ensure that `title_vector` and `content_vector` can store large string values (e.g., `VARCHAR(MAX)`).

4. **API Configuration:**
   Ensure the embedding API is correctly configured and running on your local machine at the specified endpoint, capable of receiving POST requests with a model and prompt, and returning embeddings in JSON format.

5. **Execution:**
   Run the script using Python:
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>` with the actual name of your Python script.

## Usage
- **Embed and Update Functionality:**
  The main function, `embed_and_update`, takes a model name as a parameter, retrieves articles without embeddings, generates embeddings using the specified model, and updates the database.
- **Model Selection:**
  By default, the script uses the `nomic-embed-text` model. To use a different model, adjust the parameter in the `embed_and_update` function call at the bottom of the script.

## Notes
- Ensure the database connection string, API endpoint, and environment variables are correctly configured for your specific setup.
- This script assumes that the database and API are always available and functional.

# How to download and create a Ollama docker server

To run an Ollama model with your GPU, you can use the official Docker image provided by Ollama. The Docker image supports Nvidia GPUs and can be installed using the NVIDIA Container Toolkit. Here are the steps to get started:

1. Install Docker: Depending on your operating system, download and install either Docker Desktop or Docker Engine.
2. Select and Pull the Ollama Model: Choose a preferred model from the Ollama library, such as nomic-embed-text or mxbai-embed-large, and pull it using the following command: `docker pull ollama/ollama`..
3. Run the Ollama Docker Image: Execute Docker run commands to set up the Ollama 
container. You can configure it specifically for either CPU or Nvidia GPU environments. Run the Docker container with the following command: `docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`.
4. You can now run the Ollama model using the following command: `docker exec -it ollama ollama run nomic-embed-text ` or `docker exec -it ollama ollama run mxbai-embed-large `.
5. Access and Use the Model: Utilize the Ollama WebUI by navigating to the local address provided (typically http://localhost:11434) to start interacting with your model.


Please note that the above commands assume that you have already installed Docker on your system. If you haven't installed Docker yet, you can download it from the official Docker website.

I hope this helps! Let me know if you have any other questions.

Source: Conversation with Bing, 2/23/2024
(1) How to run Ollama only on a dedicated GPU? (Instead of all GPUs .... https://github.com/ollama/ollama/issues/1813.
(2) Ollama - Self-Hosted AI Chat with Llama 2, Code Llama and More in Docker. https://noted.lol/ollama/.
(3) Ollama is now available as an official Docker image. https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image.
(4) GitHub - ollama/ollama: Get up and running with Llama 2, Mistral, and .... https://github.com/ollama/ollama.
(5) Ollama Docker image. https://hub.docker.com/r/ollama/ollama.
(6) Running Ollama 2 on NVIDIA Jetson Nano with GPU using Docker. https://dev.to/ajeetraina/running-ollama-2-on-nvidia-jetson-nano-with-gpu-using-docker-hfi.
(7) How to Install and Run Ollama with Docker: A Beginner’s Guide. https://collabnix.com/getting-started-with-ollama-and-docker/.
(8) Open WebUI (Formerly Ollama WebUI) - GitHub. https://github.com/open-webui/open-webui.
(9) undefined. https://nvidia.github.io/libnvidia-container/gpgkey.
(10) undefined. https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list.
(11) undefined. https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo.
(12) undefined. https://github.com/jmorganca/ollama.# embedyourlocalmodel
