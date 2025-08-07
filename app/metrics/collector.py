"""
Prometheus metrics collector for 2048 game.

This module defines and manages Prometheus metrics for tracking
game statistics including moves and game starts.
"""

from prometheus_client import Counter, start_http_server
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Prometheus metrics
moves_total = Counter(
    'game_moves_total',
    'Total number of moves made in the 2048 game'
)

games_started_total = Counter(
    'games_started_total',
    'Total number of games started in the 2048 game'
)


def start_metrics_server(port: int = 8000) -> None:
    """
    Start the Prometheus metrics HTTP server.
    
    Args:
        port (int): Port number for the metrics server. Defaults to 8000.
    """
    try:
        start_http_server(port)
        logger.info(f"Prometheus metrics server started on port {port}")
    except Exception as e:
        logger.error(f"Failed to start metrics server: {e}")
        raise


def increment_moves() -> None:
    """Increment the total moves counter."""
    moves_total.inc()
    logger.debug("Incremented moves counter")


def increment_games_started() -> None:
    """Increment the games started counter."""
    games_started_total.inc()
    logger.debug("Incremented games started counter")
