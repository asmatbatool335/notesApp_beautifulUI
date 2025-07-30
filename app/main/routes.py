from flask import render_template
from . import main_bp

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/search')
def search_notes():
    from flask import request
    query = request.args.get('q', '')
    # Placeholder: list of matching notes
    notes = [
        {'id': 1, 'title': 'Sample Note Title', 'snippet': 'This is a preview of the note content...'}
    ] if query else []
    return render_template('main/search_results.html', query=query, notes=notes) 