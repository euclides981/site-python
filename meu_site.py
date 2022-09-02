from flask import Flask, render_template

app = Flask(__name__)

# Criar a primeira página do site
# route é o "diretório" -> site.com/"diretorio"
# função é o que vai ser exibido neste diretório
# template


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)


# Colocar site no ar


if __name__ == '__main__':
    app.run(debug=True)
