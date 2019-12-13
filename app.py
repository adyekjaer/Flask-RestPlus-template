from flask import Flask
from apiv1 import blueprint as apiv1
from apiv2 import blueprint as apiv2

app = Flask(__name__)
app.register_blueprint(apiv1)
app.register_blueprint(apiv2)
app.run(debug=True)
