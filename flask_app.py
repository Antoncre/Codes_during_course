from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

liv = {
    0: {
        "id": 0,
        "Title": "Random",
        "Content": "Content"
    }
}


@app.route('/')
def home():
    return render_template('home.jinja2', posts=liv)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = liv.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f"A post with id: {post_id} was not found")
    else:
        return render_template('page.jinja2', liv=liv.get(post_id))


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            title = int(request.form.get('title'))
            content = int(request.form.get('content'))
            post_id = len(liv)
            result = calcul(title, content)
            liv[post_id] = {'post_id': post_id, 'Title': title, 'Content': content, "Result": result}
            return redirect(url_for('post', post_id=post_id))
        except ValueError:
            title = (request.form.get('title'))
            content = (request.form.get('content'))
            post_id = len(liv)
            liv[post_id] = {'post_id': post_id, 'Title': title, 'Content': content}
            return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')


def calcul(a, b):
    z = a**b
    return z


if __name__ == '__main__':
    app.run(debug=True)
