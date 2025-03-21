from flask import Flask, render_template
import pandas as pd

class CSVApp:
    def __init__(self, csv_file='votre_fichier.csv'):
        self.csv_file = csv_file
        self.app = Flask(__name__)
        self.init_routes()

    def init_routes(self):
        @self.app.route('/')
        def index():
            try:
                df = pd.read_csv(self.csv_file)
                rows = df.values.tolist()
                columns = df.columns.tolist()
                return render_template('index.html', rows=rows, columns=columns)
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier CSV : {e}")
                return "Erreur lors de la lecture du fichier CSV"

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    app = CSVApp(
        csv_file='votre_fichier.csv'
    )
    app.run()