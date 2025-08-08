"""
Flask application for 2048 game with Prometheus metrics.

This application serves the 2048 game frontend and provides
API endpoints for tracking game metrics.
"""

from flask import Flask, render_template
from routes import metrics_bp
from metrics import start_metrics_server
import logging
import threading

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_app():
    """
    Application factory pattern for creating Flask app.
    
    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(metrics_bp)
    
    @app.route('/')
    def home():
        """Serve the main game page."""
        logger.info("Serving main game page")
        return render_template('index.html')
    @app.route("/health")
    def health():
        return "OK", 200
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        logger.warning(f"404 error: {error}")
        return render_template('index.html'), 404

    @app.errorhandler(400)
    def bad_request(error):
        """Handle 400 errors."""
        logger.warning(f"400 error: {error}")
        return {'error': 'Bad request'}, 400

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        logger.error(f"500 error: {error}")
        return {'error': 'Internal server error'}, 500
    
    return app


def start_metrics_server_async():
    """Start Prometheus metrics server in a separate thread."""
    try:
        start_metrics_server(port=8000)
    except Exception as e:
        logger.error(f"Failed to start metrics server: {e}")


if __name__ == '__main__':
    # Start metrics server in background thread
    metrics_thread = threading.Thread(
        target=start_metrics_server_async,
        daemon=True
    )
    metrics_thread.start()
    
    # Create and run Flask app
    app = create_app()
    logger.info("Starting Flask application on http://localhost:5000")
    logger.info("Prometheus metrics available at http://localhost:5000/metrics")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
