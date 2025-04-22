from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.PickleType, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category": self.category,
            "tags": self.tags,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not all(k in data for k in ('title', 'content', 'category', 'tags')):
        return jsonify({"error": "Missing fields"}), 400
    post = Post(**data)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    data = request.get_json()
    if not all(k in data for k in ('title', 'content', 'category', 'tags')):
        return jsonify({"error": "Missing fields"}), 400
    post.title = data['title']
    post.content = data['content']
    post.category = data['category']
    post.tags = data['tags']
    post.updatedAt = datetime.utcnow()
    db.session.commit()
    return jsonify(post.to_dict()), 200

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return '', 404
    db.session.delete(post)
    db.session.commit()
    return '', 204

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post.to_dict())

@app.route('/posts', methods=['GET'])
def get_all_posts():
    term = request.args.get('term', '').lower()
    query = Post.query
    if term:
        query = query.filter(
            db.or_(
                Post.title.ilike(f'%{term}%'),
                Post.content.ilike(f'%{term}%'),
                Post.category.ilike(f'%{term}%')
            )
        )
    posts = query.all()
    return jsonify([p.to_dict() for p in posts])

if __name__ == '__main__':
    app.run(debug=True)
