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
        }
    
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