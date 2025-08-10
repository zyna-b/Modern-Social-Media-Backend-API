# 🚀 SocialFeed API - Modern Social Media Backend

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg?style=flat&logo=FastAPI)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-3776ab.svg?style=flat&logo=python)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192.svg?style=flat&logo=postgresql)](https://www.postgresql.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.42-red.svg?style=flat)](https://www.sqlalchemy.org)
[![Alembic](https://img.shields.io/badge/Alembic-1.16.4-orange.svg?style=flat)](https://alembic.sqlalchemy.org)

A high-performance, production-ready social media backend API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. Features user authentication, post management, real-time voting system, and comprehensive API documentation.

## ✨ Key Features`

- 🔐 **JWT Authentication** - Secure user registration and login
- 📝 **Post Management** - Create, read, update, delete posts with rich content
- 👥 **User System** - User profiles and relationship management
- ⬆️⬇️ **Voting System** - Upvote/downvote posts with conflict prevention
- 🔍 **Advanced Search** - Search posts by title with pagination
- 📊 **Vote Aggregation** - Real-time vote counting with SQL joins
- 🗄️ **Database Migrations** - Version-controlled schema changes with Alembic
- 📖 **Auto-Generated Docs** - Interactive Swagger/OpenAPI documentation
- 🌐 **CORS Support** - Cross-origin resource sharing for web applications
- 🛡️ **Data Validation** - Robust input validation with Pydantic
- 🏗️ **Modular Architecture** - Clean separation of concerns with routers

## 🏗️ Architecture Overview

```
app/
├── routers/           # API route handlers
│   ├── auth.py       # Authentication endpoints
│   ├── post.py       # Post CRUD operations
│   ├── user.py       # User management
│   └── vote.py       # Voting system
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic data validation schemas
├── database.py       # Database connection and session management
├── oauth2.py         # JWT token creation and validation
├── utils.py          # Password hashing utilities
├── config.py         # Environment configuration
└── main.py          # FastAPI application setup
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/zyna-b/Modern-Social-Media-Backend-API.git
cd Modern-Social-Media-Backend-API
```

### 2. Set Up Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=socialfeed_db
DATABASE_USERNAME=your_username
SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Database Setup

```bash
# Create database tables
alembic upgrade head
```

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Core Endpoints

#### 🔐 Authentication
- `POST /login` - User login with email/password
- `POST /users` - User registration

#### 📝 Posts
- `GET /posts` - Get all posts (with pagination, search, vote counts)
- `POST /posts` - Create new post (authenticated)
- `GET /posts/{id}` - Get specific post
- `PUT /posts/{id}` - Update post (owner only)
- `DELETE /posts/{id}` - Delete post (owner only)

#### 👥 Users
- `GET /users/{id}` - Get user profile
- `POST /users` - Create new user account

#### ⬆️⬇️ Voting
- `POST /vote` - Vote on posts (upvote: dir=1, downvote: dir=0)

### Example API Calls

#### Register a New User
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

#### Login
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

#### Create a Post
```bash
curl -X POST "http://localhost:8000/posts" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my post",
    "published": true
  }'
```

#### Vote on a Post
```bash
curl -X POST "http://localhost:8000/vote" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "post_id": 1,
    "dir": 1
  }'
```

## 🗄️ Database Schema

### Models Overview

- **Users**: User accounts with email, hashed passwords, timestamps
- **Posts**: User-generated content with title, content, publication status
- **Votes**: Many-to-many relationship between users and posts for voting

### Relationships

- `User` → `Post` (One-to-Many): Users can create multiple posts
- `User` → `Vote` (One-to-Many): Users can vote on multiple posts
- `Post` → `Vote` (One-to-Many): Posts can receive multiple votes
- Composite primary key on `Vote` prevents duplicate votes

## 🛠️ Development

### Running Tests

```bash
pytest
```

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Code Formatting

```bash
# Format code
black app/

# Sort imports
isort app/
```

## 🚀 Deployment

### Production Considerations

1. **Environment Variables**: Use production database credentials
2. **CORS Configuration**: Restrict origins to your frontend domain
3. **HTTPS**: Enable SSL/TLS in production
4. **Rate Limiting**: Implement rate limiting for API endpoints
5. **Monitoring**: Add logging and monitoring solutions

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🧪 Testing

### Manual Testing with Browser

```javascript
// Test API endpoint
fetch('http://localhost:8000/')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🔧 Configuration

### Key Configuration Options

- **Database**: PostgreSQL connection settings
- **JWT**: Secret key and token expiration
- **CORS**: Cross-origin settings for web apps
- **Pagination**: Default limits for post queries

## 📋 API Response Examples

### Get Posts Response
```json
[
  {
    "Post": {
      "id": 1,
      "title": "Sample Post",
      "content": "This is a sample post content",
      "published": true,
      "created_at": "2024-01-15T10:30:00Z",
      "owner_id": 1,
      "owner": {
        "id": 1,
        "email": "user@example.com",
        "created_at": "2024-01-15T09:00:00Z"
      }
    },
    "votes": 5
  }
]
```

### Authentication Response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [PostgreSQL](https://www.postgresql.org/) - Database system

## 📞 Support

- 📧 Email: zainabhamid2468@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/zyna-b/Modern-Social-Media-Backend-API/issues)
- 📖 Documentation: [API Docs](http://localhost:8000/docs)

---

⭐ **Star this repository if you found it helpful!**

![API Architecture](https://via.placeholder.com/800x400/009688/ffffff?text=SocialFeed+API+Architecture)
