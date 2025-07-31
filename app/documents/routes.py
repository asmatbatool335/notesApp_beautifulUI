from flask import render_template
from . import documents_bp

@documents_bp.route('/')
def documents_list():
    return render_template('documents/list.html')

@documents_bp.route('/<int:document_id>')
def document_view(document_id: int):
    return render_template('documents/view.html', document_id=document_id)

@documents_bp.route('/create', methods=['GET', 'POST'])
def document_create():
    return render_template('documents/edit.html', document=None)

@documents_bp.route('/<int:document_id>/edit', methods=['GET', 'POST'])
def document_edit(document_id: int):
    return render_template('documents/edit.html', document_id=document_id)

@documents_bp.route('/<int:document_id>/export')
def document_export(document_id: int):
    return render_template('documents/export.html', document_id=document_id) 