from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gifSearch():
    imgData = {
        "dog" : "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT8X4g9wqNeIy4-6G8V5uz737-HqkPYA7weLIYrRzTXBllntF2nyLZpEbRljI6moUAy99u3DmY_uFyNn6K7LuwJ4qwwFIHHMz8XTCFUJw",
        "Kevin Gates" : "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjNyOG5scWxwZGxqZ2NwbnZkNTg1MG5tazdkcnRrMDlkYXBqZG12MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kEQIxNd2i2SSsQ6S2U/giphy.webp",
    }
    

    if request.method == "POST":
        query = request.form['query']
        if query not in imgData:
            return f"No data found for {query}"

        return render_template('input.html', imgData = imgData[query])

    return render_template('input.html', url=url_for('gifSearch'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

