"""
This module contains unit tests for the Flask application.
"""

import pytest
from app import app

class TestApp:
    """Test suite for Flask app."""

    @pytest.fixture
    def client(self):
        """Create a test client."""
        with app.test_client() as client:
            yield client

    def test_home(self, client):
        """Test the home route."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Hello, Flask!"
