from flask import render_template
from . import notes_bp

@notes_bp.route('/')
def notes_list():
    return render_template('notes/list.html')

@notes_bp.route('/<int:note_id>')
def note_view(note_id: int):
    return render_template('notes/view.html', note_id=note_id)

@notes_bp.route('/create', methods=['GET', 'POST'])
def note_create():
    return render_template('notes/edit.html', note=None)

@notes_bp.route('/<int:note_id>/edit', methods=['GET', 'POST'])
def note_edit(note_id: int):
    return render_template('notes/edit.html', note_id=note_id)

@notes_bp.route('/<int:note_id>/export')
def note_export(note_id: int):
    return render_template('notes/export.html', note_id=note_id) 