from flask import Flask, render_template
import random
import requests



app = Flask(__name__)

@app.route("/test/")
def test():
    return f'<p style="color:green">¡¡Estoy vivo!!</p>'

@app.route("/")
def inicio():

    variable1 = 46

    return render_template('home.html')

@app.route("/acerca/")
def about():

    template_name = 'about.html'

    lista_links = ['www.google.com','www.duckduckgo.com','www.python.org','www.mercadolibre.com.ar']

    numero = random.randint(1,6)

    return render_template(template_name, links=lista_links, numero=numero)

@app.route("/prueba/")
def prueba():

    template_name = 'index.html'

    return render_template(template_name)

@app.route("/cotizacion-dolar/")
def get_dolar():
    template_name = 'dolar.html'


    url = "https://www.dolarsi.com/api/api.php"

    querystring = {"type":"valoresprincipales"}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)

    ctx = response.json()


    return render_template(template_name, context=ctx)

@app.route("/noticias/")
def noticias():
    template_name = 'noticias.html'


    articulos = [
        {
            'titulo':'La NASA reveló nuevas fotos en alta resolución tomadas por el Telescopio James Webb',
            'texto': 'Las imágenes del Universo incluyen detalles sobre la atmósfera de un lejano planeta gaseoso, una "guardería estelar" donde se forman estrellas, un "quinteto" de galaxias enfrascadas en una danza de encuentros cercanos y la nube de gas alrededor de una moribunda estrella.',
            'fecha':'12 de Julio, 2022',
            'imagen':'https://www.diarionorte.com/content/bucket/5/294705w750h348c.jpg.webp',
            'autor':'German Correa'
        },
        {
            'titulo':'Duele ver que un diputado hable de la compra venta de órganos',
            'texto': 'El referente local acaba de asumir en el centro de ablaciones. Describe el esfuerzo cotidiano para crear conciencia sobre un tema sensible.',
            'fecha':'14 de Mayo, 2022',
            'imagen':'https://www.diarionorte.com/content/bucket/7/294727w750h540c.jpg.webp',
            'autor':'Oscar Martinez'
        },
        {
            'titulo':'El inquietante thriller que es un furor en Netflix y no para de sumar reproducciones',
            'texto': 'Se trata de una serie de seis episodios que cuenta cómo se lleva a cabo el rescate de un asesino en serie de una cárcel psiquiátrica durante la noche del 24 de diciembre.',
            'fecha':'01 de Enero, 2021',
            'imagen':'https://www.diarionorte.com/content/bucket/9/294729w750h500c.jpg.webp',
            'autor':'Daniel Insaurralde'
        },
        {
            'titulo':'El inquietante thriller que es un furor en Netflix y no para de sumar reproducciones',
            'texto': 'Se trata de una serie de seis episodios que cuenta cómo se lleva a cabo el rescate de un asesino en serie de una cárcel psiquiátrica durante la noche del 24 de diciembre.',
            'fecha':'04 de Enero, 2021',
            'imagen':'https://www.diarionorte.com/content/bucket/9/294729w750h500c.jpg.webp',
            'autor':'Mariela Quintana'
        }
    ]


    return render_template(template_name, contenido=articulos)