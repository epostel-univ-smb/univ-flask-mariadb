from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

class DatabaseApp:
    def __init__(self, host='127.0.0.1', user='votre_utilisateur', password='votre_mot_de_passe', database='votre_base_de_donnees'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
        self.init_models()
        self.init_routes()

    def init_models(self):
        class VotreTable(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            colonne1 = self.db.Column(self.db.String(100), nullable=False)
            colonne2 = self.db.Column(self.db.String(100), nullable=False)

            def __repr__(self):
                return f'<VotreTable {self.colonne1}>'
        self.VotreTable = VotreTable

    def init_routes(self):
        @self.app.route('/')
        def index():
            with self.app.app_context():
                self.db.create_all()
                rows = self.VotreTable.query.all()
                return render_template('index.html', rows=rows)

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    app = DatabaseApp(
        host='127.0.0.1',
        user='votre_utilisateur',
        password='votre_mot_de_passe',
        database='votre_base_de_donnees'
    )
    app.run()