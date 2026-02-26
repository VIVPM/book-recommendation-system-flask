from flask import Flask,render_template, request
import joblib
import numpy as np

app = Flask(__name__)

popular_df = joblib.load(open('popular.joblib','rb'))
pt = joblib.load(open('pt.joblib','rb'))
books = joblib.load(open('books.joblib','rb'))
similarity_scores = joblib.load(open('similarity_scores.joblib','rb'))

@app.route('/')
def index():
    return render_template('index.html',
        book_name = popular_df['Book-Title'].tolist(),
        author = popular_df['Book-Author'].tolist(),
        image = popular_df['Image-URL-M'].tolist(),
        rating = popular_df['num_ratings'].tolist(),
        votes = popular_df['avg_ratings'].tolist()
    )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    try:
        index = np.where(pt.index == user_input)[0][0]
    except IndexError:
        return render_template('recommend.html', error="Book not found. Please provide the full name of the book.")
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)