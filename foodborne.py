from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(256))
    location = db.Column(db.String(128))

@app.route('/report', methods=['POST'])
def report_illness():
    title = request.json.get('title')
    description = request.json.get('description')
    location = request.json.get('location')

    new_report = Report(title=title, description=description, location=location)
    db.session.add(new_report)
    db.session.commit()

    # This is where you would add code to notify the relevant parties.
    # It could be an email, an API call to a government service, etc.
    # For simplicity, this step has been omitted from this example.

    return jsonify({"message": "Report created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
