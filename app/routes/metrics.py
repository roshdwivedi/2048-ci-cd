"""
Flask routes for handling metrics and game endpoints.

This module contains routes for serving Prometheus metrics
and handling game-related API calls.
"""

from flask import Blueprint, jsonify, request
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from metrics import increment_moves, increment_games_started
import logging

logger = logging.getLogger(__name__)

# Create Blueprint for metrics routes
metrics_bp = Blueprint('metrics', __name__)


@metrics_bp.route('/metrics')
def prometheus_metrics():
    """
    Expose Prometheus metrics endpoint.
    
    Returns:
        Response: Prometheus metrics in the expected format.
    """
    try:
        metrics_data = generate_latest()
        response = metrics_data, 200, {'Content-Type': CONTENT_TYPE_LATEST}
        logger.debug("Served Prometheus metrics")
        return response
    except Exception as e:
        logger.error(f"Error generating metrics: {e}")
        return jsonify({'error': 'Failed to generate metrics'}), 500


@metrics_bp.route('/move', methods=['POST'])
def record_move():
    """
    Record a player move in the game.
    
    This endpoint is called whenever a player makes a move
    and increments the moves counter.
    
    Returns:
        JSON response confirming the move was recorded.
    """
    try:
        increment_moves()
        logger.info("Player move recorded")
        return jsonify({
            'status': 'success',
            'message': 'Move recorded'
        }), 200
    except Exception as e:
        logger.error(f"Error recording move: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to record move'
        }), 500


@metrics_bp.route('/start', methods=['POST'])
def record_game_start():
    """
    Record a new game start.
    
    This endpoint is called when a new game is started
    and increments the games started counter.
    
    Returns:
        JSON response confirming the game start was recorded.
    """
    try:
        increment_games_started()
        logger.info("New game started")
        return jsonify({
            'status': 'success',
            'message': 'Game start recorded'
        }), 200
    except Exception as e:
        logger.error(f"Error recording game start: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to record game start'
        }), 500


@metrics_bp.route('/health')
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        JSON response indicating service health.
    """
    return jsonify({
        'status': 'healthy',
        'service': '2048-game'
    }), 200
