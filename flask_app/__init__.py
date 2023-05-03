from flask import Flask

app = Flask(__name__)
app.secret_key = "LFTP"
DATABASE = "gymbud_schema"
