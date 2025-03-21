from flask import Flask, render_template
import mariadb

class DatabaseApp:
    def __init__(self, host='127.0.0.1', port=3306, user='root', password='votre_mot_de_passe', database='votre_base_de_donnees'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.app = Flask(__name__)
        self.config = {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'database': self.database
        }
        self.init_routes()

    def init_routes(self):
        @self.app.route('/')
        def index():
            try:
                rows = self.get_data_from_db()
                return render_template('index.html', rows=rows)
            except mariadb.Error as e:
                print(f"Erreur lors de la connexion à la base de données : {e}")
                return "Erreur lors de la connexion à la base de données"

    def get_data_from_db(self):
        try:
            conn = mariadb.connect(**self.config)
            cur = conn.cursor()
            cur.execute("SELECT * FROM votre_table")
            rows = cur.fetchall()
            conn.close()
            return rows
        except mariadb.Error as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return []

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    app = DatabaseApp(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='votre_mot_de_passe',
        database='votre_base_de_donnees'
    )
    app.run()
