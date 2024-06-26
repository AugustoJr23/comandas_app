from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from funcoes import Funcoes
from settings import getHeadersAPI, ENDPOINT_CLIENTE
from mod_login.login import validaToken

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos clientes '''

@bp_cliente.route('/formCliente/', methods=['GET'])
@validaToken
def formCliente():
    return render_template('formCliente.html')

@bp_cliente.route('/', methods=['GET', 'POST'])
@validaToken
def formListaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers=getHeadersAPI())
        result = response.json()

        print(result) # para teste
        print(response.status_code) # para teste

        if (response.status_code != 200):
            raise Exception(result)
        
        return render_template('formListaCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        logradouro = request.form['logradouro']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']

        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'logradouro': logradouro, 'numero': numero, 'complemento': complemento, 'bairro':   bairro, 'cidade': cidade, 'estado': estado, 'cep': cep}
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_CLIENTE, headers=getHeadersAPI(), json=payload)
        result = response.json()

        print(result) # [{'msg': 'Cadastrado com sucesso!', 'id': 13}, 200]
        print(response.status_code) # 200

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result)

        return redirect(url_for('cliente.formListaCliente', msg=result[0]))
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
    
@bp_cliente.route("/formEditCliente", methods=['POST'])
def formEditCliente():
    try:
        # ID enviado via FORM
        id_cliente = request.form['id']

        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(ENDPOINT_CLIENTE + id_cliente, headers=getHeadersAPI())
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result)
        
        # renderiza o form passando os dados retornados
        return render_template('formCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/edit', methods=['POST'])
def edit():
    try:

        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        logradouro = request.form['logradouro']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']

        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'logradouro': logradouro, 'numero': numero, 'complemento': complemento, 'bairro':   bairro, 'cidade': cidade, 'estado': estado, 'cep': cep}
        
        # executa o verbo PUT da API e armazena seu retorno
        response = requests.put(ENDPOINT_CLIENTE + id_cliente, headers=getHeadersAPI(), json=payload)
        result = response.json()

        print(result[0])

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result)
        
        return redirect(url_for('cliente.formListaCliente', msg=result[0]))
    
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
    
@bp_cliente.route('/delete', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']

        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(ENDPOINT_CLIENTE + id_cliente, headers=getHeadersAPI())
        result = response.json()

        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result)
    
        return jsonify(erro=False, msg=result[0])
    
    except Exception as e:
        return jsonify(erro=True, msgErro=e.args[0])