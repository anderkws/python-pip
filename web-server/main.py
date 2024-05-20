import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,]

@app.get('/respuestaHTML',response_class=HTMLResponse)
def get_ls():
    return '''
        <h1>Hola soy una cabecera</h1>
        <p>soy un parrafo</p>
    '''

@app.get('/contact')
def get_list():
    return {"name": 'Platzi'}


def run():
    store.get_categories()

if __name__=='__main__':
    run()