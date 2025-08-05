# 2048 DevOps-Friendly Web Application

A Flask-based web application serving the classic 2048 game with built-in Prometheus metrics for monitoring and observability.

## 🎮 Features

- **Classic 2048 Gameplay**: Full-featured 2048 game with keyboard, mouse, and touch controls
- **Flask Backend**: Clean, modular Flask application with application factory pattern
- **Prometheus Metrics**: Built-in metrics collection for monitoring game usage
- **DevOps Ready**: Structured for easy deployment and monitoring

## 📊 Metrics

The application exposes the following Prometheus metrics:

- `game_moves_total`: Counter tracking total number of moves made
- `games_started_total`: Counter tracking total number of games started

## 🏗️ Architecture

The application follows clean code principles with a modular structure:

```
2048-devops-app/
├── app.py                 # Main Flask application
├── metrics/               # Prometheus metrics module
│   ├── __init__.py
│   └── collector.py       # Metrics definitions and collection
├── routes/                # Flask routes module  
│   ├── __init__.py
│   └── metrics.py         # API endpoints for metrics and game tracking
├── templates/             # Jinja2 templates
│   └── index.html         # Main game template
├── static/                # Static assets
│   ├── script.js          # Game logic and API integration
│   └── style.css          # Game styling
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd 2048-game
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   - Game: http://localhost:5000
   - Metrics: http://localhost:5000/metrics
   - Health Check: http://localhost:5000/health

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve the main game page |
| `/metrics` | GET | Prometheus metrics endpoint |
| `/move` | POST | Record a player move |
| `/start` | POST | Record a new game start |
| `/health` | GET | Health check endpoint |

## 📈 Monitoring

### Prometheus Configuration

Add the following job to your `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: '2048-game'
    static_configs:
      - targets: ['localhost:5000']
    metrics_path: '/metrics'
    scrape_interval: 15s
```

### Example Metrics Output

```
# HELP game_moves_total Total number of moves made in the 2048 game
# TYPE game_moves_total counter
game_moves_total 42.0

# HELP games_started_total Total number of games started in the 2048 game  
# TYPE games_started_total counter
games_started_total 3.0
```

## 🐳 Docker Support

The application includes a Dockerfile for containerized deployment:

```bash
# Build the image
docker build -t 2048-game .

# Run the container
docker run -p 5000:5000 -p 8000:8000 2048-game
```

## 🎯 Game Controls

- **Keyboard**: Use arrow keys (↑ ↓ ← →)
- **Mouse**: Click and drag to move tiles
- **Touch**: Swipe gestures on touch devices
- **Reset**: Click the "Reset Game" button

## 🧪 Development

The application is structured with clean code principles:

- **Separation of Concerns**: Metrics, routes, and application logic are separated
- **Application Factory**: Flask app creation follows the factory pattern
- **Error Handling**: Comprehensive error handling with logging
- **Type Hints**: Python functions include type annotations
- **Documentation**: All modules and functions are documented

### Code Structure

- `app.py`: Main application entry point with factory pattern
- `metrics/collector.py`: Prometheus metrics definitions and helpers
- `routes/metrics.py`: Flask Blueprint with API endpoints
- `static/script.js`: Frontend JavaScript with API integration

## 🔍 Logging

The application uses Python's built-in logging with structured format:

```
2025-01-05 18:30:15,123 - app - INFO - Starting Flask application on http://localhost:5000
2025-01-05 18:30:15,125 - metrics.collector - INFO - Prometheus metrics server started on port 8000
```

## 🚦 Production Deployment

For production deployment, consider:

1. **Use Gunicorn**: The application includes gunicorn in requirements
2. **Environment Variables**: Configure logging levels and ports via environment
3. **Reverse Proxy**: Use nginx or similar for static file serving
4. **Monitoring**: Set up Prometheus and Grafana for metrics visualization

### Example Production Command

```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:create_app()
```

## 📝 License

This project is open source. Feel free to use, modify, and distribute.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing code style
4. Add tests if applicable
5. Submit a pull request

## 🐛 Issues

If you encounter any issues, please check:

1. All dependencies are installed: `pip install -r requirements.txt`
2. No port conflicts on 5000 (Flask) or 8000 (metrics)
3. Check the application logs for specific error messages
