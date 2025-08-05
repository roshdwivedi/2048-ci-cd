"""Metrics package for 2048 game Prometheus monitoring."""

from .collector import (
    increment_moves,
    increment_games_started,
    start_metrics_server
)

__all__ = [
    'increment_moves',
    'increment_games_started', 
    'start_metrics_server'
]
