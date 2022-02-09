from flask import Flask, request, render_template
from utils import get_posts_all, get_posts_by_user, search_for_posts, get_post_by_pk, get_comment

app = Flask(__name__)


@app.route('/')
def feed_page():
    posts = get_posts_all()
    for post in posts:
        post['content'] = post['content'][:49]
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:pk>/')
def view_post_page(pk):
    post = get_post_by_pk(pk)
    comments = get_comment(pk)
    comments_number = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_number=comments_number)


@app.route('/users/<username>')
def user_page(username):
    posts = get_posts_by_user(username)
    for post in posts:
        post['content'] = post['content'][:49]
    return render_template('user-feed.html', posts=posts)


@app.route('/search')
def searching_page():
    key_word = request.args.get('s')
    posts = search_for_posts(key_word)
    number_of_posts = len(posts)
    for post in posts:
        post['content'] = post['content'][:49]
    return render_template('search.html', posts=posts, number_of_posts=number_of_posts, key_word=key_word)


if __name__ == "__main__":
    app.run()

