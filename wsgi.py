from app import create_app
import os

app = create_app(os.getenv("FLASK_ENV"))
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
