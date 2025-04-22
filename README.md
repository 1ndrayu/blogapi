# BlogAPI

BlogAPI is a RESTful service for managing personal blog posts. It provides endpoints for creating, reading, updating, deleting, and searching blog posts. This project is designed to demonstrate best practices in REST API design, HTTP methods, status codes, and basic persistence.

## Features

- Create a blog post
- Update an existing post
- Delete a post
- Retrieve a single post
- Retrieve all posts
- Filter posts by search term (in title, content, or category)
- JSON-based request/response format
- Follows RESTful conventions and HTTP standards

## API Endpoints

### Create Post

```
POST /posts
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"]
}
```

### Update Post

```
PUT /posts/1
{
  "title": "My Updated Blog Post",
  "content": "Updated content.",
  "category": "Technology",
  "tags": ["Tech"]
}
```

### Delete Post

```
DELETE /posts/1
```

### Get Single Post

```
GET /posts/1
```

### Get All Posts

```
GET /posts
```

### Search Posts

```
GET /posts?term=tech
```

## Data Model

```json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post.",
  "category": "Technology",
  "tags": ["Tech", "Programming"],
  "createdAt": "2025-04-22T10:00:00Z",
  "updatedAt": "2025-04-22T10:00:00Z"
}
```

## Tech Stack

- Language: Python
- Framework: Flask
- Database: SQLite (or any preferred lightweight relational DB)
- Dependencies: Only standard or minimal dependencies required for Flask and DB interaction

## Repository

https://github.com/your-username/blogapi
