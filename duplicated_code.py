def index():
    url = random.choice(images)
    return render_template('index.html', url=url)
