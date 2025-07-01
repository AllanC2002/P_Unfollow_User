import pytest
from unittest.mock import patch, MagicMock
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

@patch("services.functions.conection_userprofile")
@patch("main.jwt.decode")
def test_unfollow_success(mock_jwt_decode, mock_conection, client):
    # Mockear the JWT decode function to return a valid user ID
    mock_jwt_decode.return_value = {"user_id": 1}

    # Simulate a database session
    mock_session = MagicMock()
    mock_conection.return_value = mock_session

    # Simulate a follow relationship in the database
    mock_follow = MagicMock()
    mock_follow.Status = 1
    mock_session.query().filter_by().first.return_value = mock_follow

    # Send a POST request to the /unfollow endpoint
    response = client.post(
        "/unfollow",
        headers={"Authorization": "Bearer fake-token"},
        json={"id_following": 2}
    )

    assert response.status_code == 200
    assert response.json["message"] == "Unfollowed successfully"
