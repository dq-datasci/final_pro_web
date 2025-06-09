from flask import Flask, render_template
import os

# Obtiene la ruta del directorio base del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Define la ruta de la carpeta de plantillas
template_dir = os.path.join(project_root, 'templates')

# Define la ruta de la carpeta de archivos estáticos
static_dir = os.path.join(project_root, 'static')

# Inicializa la aplicación Flask, especificando ambas rutas
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def index():
    title="Bienvenido a mi sitio web"
    datos = {
        "nombre": "David",
        "apellido": "Quintela",
        "edad": 31,
        "lenguajes": ["Python", "Java", "JavaScript"],
        "lenguajes2": ["PHP", "C++", "C#"]
    }
    return render_template('index.html', title=title, datos=datos)

@app.route('/demo')
def demo():
    return render_template("demo.html")

@app.route('/resumen')
def resumen():
    return render_template("resumen.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)