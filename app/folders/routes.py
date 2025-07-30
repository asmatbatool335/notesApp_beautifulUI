from flask import render_template
from . import folders_bp

@folders_bp.route('/')
def folders_list():
    return render_template('folders/list.html')

@folders_bp.route('/<int:folder_id>')
def folder_view(folder_id: int):
    return render_template('folders/view.html', folder_id=folder_id)

@folders_bp.route('/create', methods=['GET', 'POST'])
def folder_create():
    return render_template('folders/create.html') 