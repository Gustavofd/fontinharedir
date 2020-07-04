from flask import Flask, jsonify, redirect, request, url_for

app = Flask(__name__)

@app.route('/<name>/<int:age>', methods=['POST'])
def main(name, age):
    return 'OK %s - %s' % (name, age), 200

@app.route('/request', methods=['POST'])
def handle_post_request():
    #person = request.args.get('person')
    #print request.form
    return 'Recebida a solicitacao via (%s chave %s) de %s que possui %s anos de idade' % (request.method, request.headers['apikey'], request.form['name'], request.form['age']), 200

@app.route('/redir/v0/<servico>/<valor>', methods=['GET'])
def redir_v1_handle(servico, valor):
    # sufixo e prefixo padrao, serao usados caso o servico nao seja localizado
    prefixo = 'https://www.uol.com.br' 
    sufixo = ''
    prefixo_e_sufixo = ''
    # dicionario contendo os servicos, no futuro poderá estar hospedado em um banco nosql
    servicos = {
        "google": ['https://www.google.com/search?q=', ''],
        "yahoo": ['https://br.search.yahoo.com/search?p=', '&fr=yfp-search-sb'],
        "bing": ['https://www.bing.com/search?q=', ''],
        "busca": ['https://www.google.com/search?q=', ''],
        "livro": ['https://www.saraiva.com.br/', ''],
        "filme": ['https://www.omelete.com.br/busca?q=', ''],
        "vinho": ['https://www.wine.com.br/search.ep?keyWords=','']
    }
    if servico in servicos:
        prefixo_e_sufixo = servicos.get(servico)
        prefixo = prefixo_e_sufixo[0]
        sufixo = prefixo_e_sufixo[1]
    if (prefixo_e_sufixo == ''):
        url_para_redirecionamento = prefixo + sufixo    
    else:
        url_para_redirecionamento = prefixo + valor + sufixo
    return redirect(url_para_redirecionamento)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
