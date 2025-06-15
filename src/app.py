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

datos_globales = {
        "nombre": "David",
        "apellido": "Quintela",
        "titulo": "Estudiante de Ciencia de Datos",
        "edad": 31,
        "email": "HlOyP@example.com",	
        "lenguajes": ["Python", "Java", "JavaScript"],
        "materia": "Programación Web"
        }
@app.route('/')
def index():
    title="Bienvenido a mi sitio web"
    return render_template('index.html', title=title, datos=datos_globales)

@app.route('/demo')
def demo():
    return render_template("demo.html")

@app.route('/resumen')
def resumen():
    return render_template("resumen.html")

@app.route('/galeria')
def galeria():
    return render_template("galeria.html")

@app.route('/perfil')
def perfil():
    return render_template("perfil.html", datos=datos_globales)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)