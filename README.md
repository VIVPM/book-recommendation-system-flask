# 📚 Book Recommendation System

A Flask-based web application that recommends books using collaborative filtering and popularity-based algorithms. Built with machine learning techniques to provide personalized book suggestions.

## ✨ Features

- **Popular Books**: Browse trending books based on ratings and user engagement
- **Personalized Recommendations**: Get book suggestions based on similarity scores
- **Interactive UI**: Clean and responsive web interface
- **Fast Performance**: Optimized with joblib for quick data loading

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **ML Libraries**: NumPy, Pandas, Scikit-learn
- **Data Storage**: Joblib (compressed pickle files)
- **Deployment**: Gunicorn-ready for production

## 📁 Project Structure

```
book-recommendation-system-flask/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── templates/                  # HTML templates
│   ├── index.html             # Popular books page
│   └── recommend.html         # Recommendation page
├── joblib/                    # Serialized ML models and data
│   ├── popular.joblib         # Popular books data
│   ├── pt.joblib              # Pivot table
│   ├── books.joblib           # Books dataset
│   └── similarity_scores.joblib # Similarity matrix
└── book-recommender-system.ipynb # Model training notebook
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/book-recommendation-system-flask.git
cd book-recommendation-system-flask
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📊 How It Works

### 1. Popularity-Based Recommendations
- Displays top-rated books based on user ratings and engagement
- Shown on the homepage for all users

### 2. Collaborative Filtering
- Uses cosine similarity to find books similar to user input
- Recommends 5 similar books based on user preferences
- Handles book not found errors gracefully

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage with popular books |
| `/recommend` | GET | Recommendation page UI |
| `/recommend_books` | POST | Get book recommendations |

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (default: 5000)

### Data Files

The application uses compressed joblib files for faster loading:
- `popular.joblib`: Pre-computed popular books
- `pt.joblib`: Pivot table for similarity calculations
- `books.joblib`: Complete books dataset
- `similarity_scores.joblib`: Pre-computed similarity matrix

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset: Book-Crossing Dataset
- Inspiration: Collaborative filtering techniques
- Framework: Flask web framework
