from fastapi import FastAPI
from fastapi.responses  import HTMLResponse
app =FastAPI()
app.title ="Mi aplicacion con fastapi m"
app.version = "0.0.1"
movies_list =[
    {
        "id":1,
         "title":" la caida del tercer  Reich",
         "overview":" cuenta la caida de la alemania nazi ",
         "yield":"2007",
         "rating":10.0
    },
    
        {
        "id":2,
        "title":"  EL Exorcista 3",
        "overview":" cuenta de una pecados de una mujer poseida ",
        "yield":"2008",
        "rating":10.0
        },
        
    {
        "id": 3,
        "title": "El Legado del Dragón",
        "overview": "Una antigua orden secreta resurge para proteger al mundo de una amenaza mística.",
        "yield": "2023",
        "rating": 8.5
    },
    {
        "id": 4,
        "title": "Horizonte Perdido",
        "overview": "Una nave espacial se desvía de su curso, llevándola a un planeta desconocido y lleno de peligros.",
        "yield": "2024",
        "rating": 9.0
    },
    {
        "id": 5,
        "title": "La Guerra de los Clones",
        "overview": "En un futuro cercano, los clones humanos luchan por sus derechos y su libertad.",
        "yield": "2023",
        "rating": 8.0
    },
    {
        "id": 6,
        "title": "Bajo las Sombras",
        "overview": "Un grupo de amigos se enfrenta a sus peores miedos tras encontrar una casa maldita.",
        "yield": "2023",
        "rating": 7.5
    },
    {
        "id": 7,
        "title": "El Último Asalto",
        "overview": "Un boxeador retirado vuelve al ring para una última pelea que lo cambiará todo.",
        "yield": "2023",
        "rating": 8.8
    },
    {
        "id": 8,
        "title": "Ecos del Pasado",
        "overview": "Una periodista descubre secretos familiares ocultos mientras investiga un caso de asesinato.",
        "yield": "2024",
        "rating": 9.2
    },
    {
        "id": 9,
        "title": "El Renacer del Imperio",
        "overview": "Un imperio olvidado surge de las cenizas, y sus enemigos deben unir fuerzas para detenerlo.",
        "yield": "2024",
        "rating": 8.7
    },
    {
        "id": 10,
        "title": "La Ciudad de Cristal",
        "overview": "En una metrópolis futurista, un detective sigue las pistas de un misterio que podría cambiarlo todo.",
        "yield": "2024",
        "rating": 9.5
    },
]

     

@app.get('/', tags=["Home"] )
def message ():
   # return {"Hello":"World"}
   return HTMLResponse('<h1> Hello World</h1>')
@app.get('/movies', tags=["Movies"])
def movies():
    return movies_list


@app.get('/movies/{id}', tags=["Movies"])
def get_movies(id:int):
    for item in movies_list:
        if item["id"]==id:    
            return item 
    return[]    