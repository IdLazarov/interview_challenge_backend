from flask import Flask
from views.user import user_views
from views.hoa import hoa_views


app = Flask(__name__)
app.debug = True


app.register_blueprint(user_views)
app.register_blueprint(hoa_views)


@app.route('/')
def index():
    return '<h2>Hello InspectHOA</h2>'


if __name__ == '__main__':
    app.run(debug=True)
