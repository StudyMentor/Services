from flask import request, jsonify, Flask
import random

app = Flask(__name__)

tutorias = [
    {
        "id": 1,
        "duracion": 60,
        "grabacion": {"url": "http://example.com", "fecha_creacion": "2023-09-31"},
        "reunion": {"url": "http://example.com", "fecha_creacion": "2023-09-31"},
        "documentos": [
            {
                "formato": "pdf",
                "nombre_documento": "Material de clase",
                "autor": "Pablito",
            },
            {
                "formato": "ppt",
                "nombre_documento": "Campos matematicos",
                "autor": "Pablito",
            },
        ],
        "resenia": {
            "mensaje": "La tutoria cumple con las expectativas",
            "fecha_publicacion": "2023-10-01",
            "calificacion": 3,
        },
    },
    {
        "id": 2,
        "duracion": 60,
        "grabacion": {"url": "http://example.com", "fechaCreacion": "2023-09-31"},
        "reunion": {"url": "http://example.com", "fecha_creacion": "2023-09-31"},
        "documentos": [
            {
                "formato": "pdf",
                "nombre_documento": "Material de clase",
                "autor": "Pablito",
            }
        ],
        "resenia": {
            "mensaje": "La tutoria cumple con las expectativas",
            "fecha_publicacion": "2023-10-01",
            "calificacion": 2,
        },
    },
    {
        "id": 3,
        "duracion": 60,
        "grabacion": {"url": "http://example.com", "fecha_creacion": "2023-09-31"},
        "reunion": {"url": "http://example.com", "fecha_creacion": "2023-09-31"},
        "documentos": [
            {
                "formato": "pdf",
                "nombre_documento": "Material de clase",
                "autor": "Pablito",
            }
        ],
        "resenia": {
            "mensaje": "La tutoria cumple con las expectativas",
            "fecha_publicacion": "2023-10-01",
            "calificacion": 8.7,
        },
    },
]

usuarios = [
    {
        "id": 1,
        "rol": "Estudiante",
        "datos_personales": {
            "doc_identidad": {
                "tipo": "DNI",
                "numero": random.randint(10_00_00_00, 99_99_99_99),
            },
            "nombre": "Marcelo",
            "apellido": "Garro",
            "edad": 20,
            "correo_personal": "marcelogarro137@gmail.com",
            "fecha_nacimiento": "2003-03-22",
            "genero": "M",
            "direccion": "Av. Avenidius 1200",
            "nacionalidad": "Peruano",
        },
        "datos_academicos": {
            "codigo": random.randint(1_000_000, 9_999_999),
            "correo_institucional": "example@mail.com",
            "universidad": "UPC",
            "ciclo": random.randint(1, 10),
            "nivel": "Pregrado",
        },
    },
    {
        "id": 2,
        "rol": "Tutor",
        "datos_personales": {
            "doc_identidad": {
                "tipo": "DNI",
                "numero": random.randint(10_00_00_00, 99_99_99_99),
            },
            "nombre": "Felipe",
            "apellido": "Martinez",
            "edad": 24,
            "correo_personal": "martinezjuegos@gmail.com",
            "fecha_nacimiento": "1999-09-23",
            "genero": "M",
            "direccion": "Av. Jiron los jazminez 435",
            "nacionalidad": "Peruano",
        },
        "datos_academicos": {
            "codigo": random.randint(1_000_000, 9_999_999),
            "correo_institucional": "example@mail.com",
            "universidad": "UPC",
            "ciclo": random.randint(1, 10),
            "nivel": "Pregrado",
        },
    },
    {
        "id": 3,
        "rol": "Tutor",
        "datos_personales": {
            "doc_identidad": {
                "tipo": "DNI",
                "numero": random.randint(10_00_00_00, 99_99_99_99),
            },
            "nombre": "Marta",
            "apellido": "Diaz",
            "edad": 22,
            "correo_personal": "MartaD2001@gmail.com",
            "fecha_nacimiento": "2001-09-23",
            "genero": "F",
            "direccion": "Av. Javier Prado 1102",
            "nacionalidad": "Japones",
        },
        "datos_academicos": {
            "codigo": random.randint(1_000_000, 9_999_999),
            "correo_institucional": "example@mail.com",
            "universidad": "UPC",
            "ciclo": random.randint(1, 10),
            "nivel": "Pregrado",
        },
    },
    {
        "id": 4,
        "rol": "Estudiante",
        "datos_personales": {
            "doc_identidad": {
                "tipo": "DNI",
                "numero": random.randint(10_00_00_00, 99_99_99_99),
            },
            "nombre": "Jorge",
            "apellido": "Luna",
            "edad": 23,
            "correo_personal": "jorge@gmail.com",
            "fecha_nacimiento": "1993-09-23",
            "genero": "M",
            "direccion": "Av. illinois 1102",
            "nacionalidad": "Peruano",
        },
        "datos_academicos": {
            "codigo": random.randint(1_000_000, 9_999_999),
            "correo_institucional": "example@mail.com",
            "universidad": "UPC",
            "ciclo": random.randint(1, 10),
            "nivel": "Pregrado",
        },
    },
    {
        "id": 5,
        "rol": "Estudiante",
        "datos_personales": {
            "doc_identidad": {"tipo": "Pasaporte", "numero": 98765432},
            "nombre": "Ana",
            "apellido": "García",
            "edad": 22,
            "correo_personal": "anagarcia@example.com",
            "fecha_nacimiento": "2001-05-10",
            "genero": "F",
            "direccion": "Calle 4, Avenida 5",
            "nacionalidad": "Española",
        },
        "datos_academicos": {
            "codigo": random.randint(1_000_000, 9_999_999),
            "correo_institucional": "example@mail.com",
            "universidad": "UPC",
            "ciclo": random.randint(1, 10),
            "nivel": "Pregrado",
        },
    },
]


@app.get("/api/v1/tutorias")
def get_tutorias():
    return jsonify(tutorias)


@app.get("/api/v1/tutorias/<int:id>")
def get_tutoria(id: int):
    for tutoria in tutorias:
        if tutoria["id"] == id:
            return jsonify(tutoria)


# Tutores
@app.get("/api/v1/tutores")
def get_tutores():
    results = [usuario for usuario in usuarios if usuario["rol"] == "Tutor"]
    return jsonify(results)


@app.get("/api/v1/tutores/<int:id>")
def get_tutor(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            if usuario["rol"] != "Tutor":
                return "<h1>Este usuario no es un tutor</h1>"

            return jsonify(usuario)

    return "<h1>No existe el tutor</h1>"


# Estudiante
@app.get("/api/v1/estudiantes")
def get_estudiantes():
    results = [usuario for usuario in usuarios if usuario["rol"] == "Estudiante"]
    return jsonify(results)


@app.get("/api/v1/estudiantes/<int:id>")
def get_estudiante(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            if usuario["rol"] != "Estudiante":
                return "<h1>Este usuario no es un estudiante</h1>"

            return jsonify(usuario)

    return "<h1>No existe el estudiante</h1>"


app.run(host="0.0.0.0", port=82)
