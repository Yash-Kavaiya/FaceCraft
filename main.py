from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import io
from face_generator import FaceGenerator

app = FastAPI()
generator = FaceGenerator()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Random Face Generator</h1>
            <img src="/generate" id="face">
            <button onclick="refresh()">Generate New Face</button>
            <script>
                function refresh() {
                    document.getElementById('face').src = '/generate?' + Date.now()
                }
            </script>
        </body>
    </html>
    """

@app.get("/generate")
def generate_face():
    # Generate face image
    image = generator.generate_face()
    # Convert to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return Response(content=img_byte_arr, media_type="image/png")

# Start server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
