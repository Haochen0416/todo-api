# test_todos.py - Tests for /todos endpoints


class TestCreateTodo:
    def test_create_todo_success(self, client, auth_headers):
        """Authenticated user can create a todo."""
        response = client.post("/todos", json={
            "title": "Buy groceries", "description": "Milk, eggs, bread"
        }, headers=auth_headers)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Buy groceries"
        assert data["description"] == "Milk, eggs, bread"
        assert data["completed"] is False

    def test_create_todo_unauthenticated(self, client):
        """Unauthenticated request to create todo returns 401."""
        response = client.post("/todos", json={"title": "Test"})
        assert response.status_code == 401

    def test_create_todo_no_description(self, client, auth_headers):
        """Todo can be created with title only (description optional)."""
        response = client.post("/todos", json={"title": "Minimal todo"}, headers=auth_headers)
        assert response.status_code == 201
        assert response.json()["title"] == "Minimal todo"


class TestGetTodos:
    def test_get_todos_empty(self, client, auth_headers):
        """New user has no todos."""
        response = client.get("/todos", headers=auth_headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_todos_returns_own_todos_only(self, client, auth_headers):
        """User can only see their own todos."""
        client.post("/todos", json={"title": "My todo"}, headers=auth_headers)

        # Register and log in a second user
        client.post("/auth/register", json={
            "username": "user2", "email": "user2@example.com", "password": "pass123"
        })
        login = client.post("/auth/login", data={"username": "user2", "password": "pass123"})
        headers2 = {"Authorization": f"Bearer {login.json()['access_token']}"}

        response = client.get("/todos", headers=headers2)
        assert response.json() == []  # user2 sees no todos

    def test_get_todos_unauthenticated(self, client):
        """Unauthenticated request returns 401."""
        response = client.get("/todos")
        assert response.status_code == 401


class TestUpdateTodo:
    def test_update_todo_title(self, client, auth_headers):
        """User can update a todo's title."""
        todo_id = client.post("/todos", json={"title": "Old title"}, headers=auth_headers).json()["id"]
        response = client.put(f"/todos/{todo_id}", json={"title": "New title"}, headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["title"] == "New title"

    def test_mark_todo_completed(self, client, auth_headers):
        """User can mark a todo as completed."""
        todo_id = client.post("/todos", json={"title": "Task"}, headers=auth_headers).json()["id"]
        response = client.put(f"/todos/{todo_id}", json={"completed": True}, headers=auth_headers)
        assert response.status_code == 200
        assert response.json()["completed"] is True

    def test_update_nonexistent_todo(self, client, auth_headers):
        """Updating a non-existent todo returns 404."""
        response = client.put("/todos/9999", json={"title": "Ghost"}, headers=auth_headers)
        assert response.status_code == 404

    def test_cannot_update_others_todo(self, client, auth_headers):
        """User cannot update another user's todo."""
        todo_id = client.post("/todos", json={"title": "Private"}, headers=auth_headers).json()["id"]

        client.post("/auth/register", json={
            "username": "attacker", "email": "attacker@example.com", "password": "pass123"
        })
        login = client.post("/auth/login", data={"username": "attacker", "password": "pass123"})
        headers2 = {"Authorization": f"Bearer {login.json()['access_token']}"}

        response = client.put(f"/todos/{todo_id}", json={"title": "Hacked"}, headers=headers2)
        assert response.status_code == 404


class TestDeleteTodo:
    def test_delete_todo_success(self, client, auth_headers):
        """User can delete their own todo."""
        todo_id = client.post("/todos", json={"title": "To delete"}, headers=auth_headers).json()["id"]
        response = client.delete(f"/todos/{todo_id}", headers=auth_headers)
        assert response.status_code == 200
        assert str(todo_id) in response.json()["message"]

    def test_delete_nonexistent_todo(self, client, auth_headers):
        """Deleting a non-existent todo returns 404."""
        response = client.delete("/todos/9999", headers=auth_headers)
        assert response.status_code == 404

    def test_cannot_delete_others_todo(self, client, auth_headers):
        """User cannot delete another user's todo."""
        todo_id = client.post("/todos", json={"title": "Protected"}, headers=auth_headers).json()["id"]

        client.post("/auth/register", json={
            "username": "intruder", "email": "intruder@example.com", "password": "pass123"
        })
        login = client.post("/auth/login", data={"username": "intruder", "password": "pass123"})
        headers2 = {"Authorization": f"Bearer {login.json()['access_token']}"}

        response = client.delete(f"/todos/{todo_id}", headers=headers2)
        assert response.status_code == 404
