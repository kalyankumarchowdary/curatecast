from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ott-platforms')
def ott_platforms():
    # Sample list of OTT platforms with logos and URLs
    platforms = [
        {"name": "Netflix", "description": "Stream movies, TV shows, and more.", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", "url": "https://www.netflix.com"},
        {"name": "Amazon Prime Video", "description": "Watch popular movies and TV shows.", "logo": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Prime_Video.png", "url": "https://www.primevideo.com"},
        {"name": "Disney+", "description": "Stream Disney, Marvel, Star Wars, and more.", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Disney%2B_logo.svg", "url": "https://www.disneyplus.com"},
        {"name": "Hulu", "description": "Watch TV shows, movies, and Hulu Originals.", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Hulu_Logo.svg", "url": "https://www.hulu.com"},
        {"name": "HBO Max", "description": "Stream all of HBO with new hits.", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/17/HBO_Max_Logo.svg", "url": "https://www.hbomax.com"}
    ]
    return render_template('ott_platforms.html', platforms=platforms)

if __name__ == '__main__':
    app.run(debug=True)