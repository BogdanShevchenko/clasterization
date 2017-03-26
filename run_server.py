import flask
from flask import send_file

app = flask.Flask(__name__)


@app.route("/")
def index():
    """
    When you request the root path, you'll get the index.html template.
    """
    return flask.render_template("index.html")


@app.route("/all_points_csv")
def data():
    return send_file('static/clusters.csv',
                     mimetype='text/csv',
                     attachment_filename='clusters.csv',
                     as_attachment=True)


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)


if __name__ == "__main__":
    import os

    port = 8000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}/".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string
    app.run(port=port)
