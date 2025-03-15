from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, template_folder='templates/blog')

# Danh sách bài viết có hình ảnh ngẫu nhiên
posts = [
    {"title": "Bài viết 1", "content": "Nội dung bài viết 1", "image": "https://picsum.photos/600/300"},
    {"title": "Bài viết 2", "content": "Nội dung bài viết 2", "image": "https://picsum.photos/600/300"},
    {"title": "Bài viết 3", "content": "Nội dung bài viết 3", "image": "https://picsum.photos/600/300"},
]

@blog_bp.route('/blog')
def blog():
    return render_template('blog/index.html', posts=posts)
