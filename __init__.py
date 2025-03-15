from flask import Flask
from blog import blog_bp  # Import module blog

def create_app():
    app = Flask(__name__)
    
    # Đăng ký blueprint của blog
    app.register_blueprint(blog_bp)

    return app
