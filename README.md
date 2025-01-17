# FaceCraft

## Project Description

FaceCraft is a Python-based web application that generates random face images using the StyleGAN2 model. The application is built using FastAPI and serves the generated face images through a web interface.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Yash-Kavaiya/FaceCraft.git
   cd FaceCraft
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install torch fastapi uvicorn python-multipart pillow
   ```

## Usage Instructions

1. Run the server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Open your web browser and navigate to `http://localhost:8000` to access the Random Face Generator web application.

3. Click the "Generate New Face" button to generate and display a new random face image.
