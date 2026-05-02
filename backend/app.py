from flask import Flask
from routes.analyze import analyze_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(analyze_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)