import flask



# 1. O usuário acessa uma página web.
# 2. Faz upload de uma imagem.
# 3. O Flask recebe essa imagem.
# 4. O Python analisa os pixels utilizando NumPy e processamento de imagem.
# 5. O sistema identifica as 10 cores mais frequentes.
# 6. O resultado aparece na página, com as cores e seus respectivos códigos HEX.



app = flask.Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
