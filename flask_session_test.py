from flask import Flask,Blueprint
from session_test_net.index import index_page


app = Flask(__name__)
# app.secret_key = "super secret key"
app.config['SECRET_KEY'] = '123456'
app.register_blueprint(index_page)




if __name__ == '__main__':
    app.run(debug=True)
