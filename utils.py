import json

def get_posts_all():
    with open('data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        return json_data


def get_posts_by_user(username):
    posts = get_posts_all()
    user_posts = []
    for post in posts:
        if post['poster_name'] == username:
            user_posts.append(post)
    return user_posts


def search_for_posts(query):
    posts = get_posts_all()
    matching_posts = []
    for post in posts:
        post_words = post['content'].split(" ")
        for word in post_words:
            if str(query) == word.rstrip("!") or str(query) == word.rstrip(",") or str(query) == word.rstrip("."):
                matching_posts.append(post)
    return matching_posts[:9]


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


def get_comment(post_id):
    comments_to_post = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        comments = json.load(file)
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_to_post.append(comment)
        return comments_to_post




