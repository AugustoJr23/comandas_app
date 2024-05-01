from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos produtos '''
@bp_produto.route('/')
def formListaProduto():
    return render_template('formListaProduto.html'), 200

@bp_produto.route('/formProduto/', methods=['GET'])
def formProduto():
    return render_template('formProduto.html')