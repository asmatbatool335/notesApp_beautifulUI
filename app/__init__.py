from flask import Flask, render_template
from .extensions import db, migrate, login_manager

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .auth import auth_bp
    from .notes import notes_bp
    from .folders import folders_bp
    from .main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp, url_prefix='/notes')
    app.register_blueprint(folders_bp, url_prefix='/folders')
    app.register_blueprint(main_bp)

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html'), 403

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error.html'), 500

    return app 