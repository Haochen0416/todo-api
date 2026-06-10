# test_auth.py - Tests for /auth endpoints
import pytest


class TestRegister:
    def test_register_success(self, client):
        """New user registers successfully."""
        response = client.post("/auth/register", json={
            "username": "alice", "email": "alice@example.com", "password": "pass123"
        })
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "alice"
        assert data["email"] == "alice@example.com"
        assert data["is_active"] is True
        assert "password" not in data  # password must never be returned

    def test_register_duplicate_username(self, client):
        """Registering with an existing username returns 400."""
        payload = {"username": "bob", "email": "bob@example.com", "password": "pass123"}
        client.post("/auth/register", json=payload)
        response = client.post("/auth/register", json={
            "username": "bob", "email": "different@example.com", "password": "pass123"
        })
        assert response.status_code == 400
        assert "Username already registered" in response.json()["detail"]

    def test_register_duplicate_email(self, client):
        """Registering with an existing email returns 400."""
        client.post("/auth/register", json={
            "username": "carol", "email": "carol@example.com", "password": "pass123"
        })
        response = client.post("/auth/register", json={
            "username": "carol2", "email": "carol@example.com", "password": "pass123"
        })
        assert response.status_code == 400
        assert "Email already registered" in response.json()["detail"]


class TestLogin:
    def test_login_success(self, client, registered_user):
        """Valid credentials return a JWT token."""
        response = client.post("/auth/login", data={
            "username": registered_user["username"],
            "password": registered_user["password"],
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_wrong_password(self, client, registered_user):
        """Wrong password returns 401."""
        response = client.post("/auth/login", data={
            "username": registered_user["username"],
            "password": "wrongpassword",
        })
        assert response.status_code == 401

    def test_login_nonexistent_user(self, client):
        """Non-existent user returns 401."""
        response = client.post("/auth/login", data={
            "username": "ghost", "password": "pass123"
        })
        assert response.status_code == 401


class TestGetMe:
    def test_get_me_authenticated(self, client, registered_user, auth_headers):
        """Authenticated user can retrieve their own profile."""
        response = client.get("/auth/me", headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["username"] == registered_user["username"]

    def test_get_me_unauthenticated(self, client):
        """Unauthenticated request returns 401."""
        response = client.get("/auth/me")
        assert response.status_code == 401
