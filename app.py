from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)

@app.route('/')
def hello():
    redis.incr('hits')
    return F"Hello World! I have been seen { redis.get('hits') } times." 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)