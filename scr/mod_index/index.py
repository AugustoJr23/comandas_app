from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/index", template_folder='templates')

''' rotas dos index '''
@bp_index.route('/')
def formindex():
    return render_template('formIndex.html'), 200