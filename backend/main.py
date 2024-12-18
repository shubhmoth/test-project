from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Create an instance of the FastAPI application
app = FastAPI()

# Define a root endpoint that serves an HTML response
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Welcome Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #5a67d8;
            }
            p {
                font-size: 18px;
                margin-top: 20px;
            }
            a {
                text-decoration: none;
                color: #5a67d8;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to FastAPI</h1>
        <p>Your FastAPI application is running successfully!</p>
        <p>Visit the <a href="/docs">API Documentation</a> to explore your endpoints.</p>
    </body>
    </html>
    """
    return html_content

# Define another endpoint for JSON response
@app.get("/ping")
def ping():
    return {"message": "Pong!"}

# Optional: Main function to initialize and start the server programmatically
def main():
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# Run the main function when executed directly
if __name__ == "__main__":
    main()
