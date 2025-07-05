# Unfollow User

This document provides an overview of the project structure, design patterns, communication architecture, and API endpoint instructions.

## Folder Structure

The project is organized into the following main folders:

*   **`.github/`**: Contains GitHub Actions workflow files.
    *   **`workflows/`**: Houses YAML files for CI/CD pipelines, such as `docker-publish.yml` which likely handles building and publishing Docker images.
*   **`conections/`**: This folder is responsible for managing database connections.
    *   `mysql.py`: Contains the logic to establish a connection to a MySQL database using SQLAlchemy, retrieving database credentials from environment variables.
*   **`models/`**: Defines the data models or schema for the application.
    *   `models.py`: Uses SQLAlchemy to define database tables as Python classes (e.g., `Profile`, `Followers`). These models represent the structure of the data.
*   **`services/`**: Contains the business logic of the application.
    *   `functions.py`: Implements the core functionalities, such as `unfollow_user`, which interacts with the database models and connection layer to perform actions.
*   **`tests/`**: Includes test files for the application.
    *   `reoute_test.py`: Appears to be an integration test script that makes HTTP requests to the live API endpoints (e.g., `/login`, `/unfollow`) to verify their functionality.
    *   `test_unfollow.py`: Likely contains unit tests specifically for the `unfollow_user` functionality (though its content was not provided in the initial exploration).

Other notable files:

*   **`main.py`**: The main entry point of the Flask application. It defines API routes (e.g., `/unfollow`), handles incoming requests, and uses services to process them. It also manages JWT-based authentication.
*   **`dockerfile`**: Instructions for building a Docker image for the application, enabling containerization.
*   **`requirements.txt`**: Lists the Python dependencies required for the project.
*   **`.gitignore`**: Specifies intentionally untracked files that Git should ignore (e.g., `__pycache__/`).

## Backend Design Pattern

The backend appears to follow a **Layered Architecture** pattern, with elements of a **Service Layer**.

*   **Presentation Layer (API Endpoints)**: `main.py` defines the API endpoints, receives HTTP requests, and returns responses. It handles request validation and authentication.
*   **Service Layer (Business Logic)**: `services/functions.py` encapsulates the business logic. For example, `unfollow_user` contains the rules and steps for a user to unfollow another.
*   **Data Access Layer (Database Interaction)**:
    *   `conections/mysql.py` manages the database connection.
    *   `models/models.py` defines the ORM (Object-Relational Mapping) models that interact with the database.

This separation of concerns helps in maintaining a modular and testable codebase.

## Communication Architecture

The application uses a **RESTful API** architecture for communication.

*   Clients (e.g., frontend applications, mobile apps, or test scripts like `tests/reoute_test.py`) interact with the server by sending HTTP requests to specific endpoints.
*   Data is exchanged in JSON format.
*   **Authentication**: The `/unfollow` endpoint (and likely others) uses **JWT (JSON Web Token)** for authentication.
    *   A client first authenticates (e.g., via a `/login` endpoint, as suggested by `tests/reoute_test.py`).
    *   Upon successful authentication, the server issues a JWT.
    *   The client must include this JWT in the `Authorization` header (as a Bearer token) for subsequent requests to protected endpoints.

## Folder Pattern

The folder pattern is primarily **Layer-based**. The top-level directories (`conections`, `models`, `services`) clearly delineate different layers of the application (data access, data definition, business logic).

## Endpoint Instructions

### Unfollow User

This endpoint allows a logged-in user to unfollow another user.

*   **HTTP Method**: `POST`
*   **URL**: `/unfollow`
*   **Headers**:
    *   `Authorization`: `Bearer <YOUR_JWT_TOKEN>` (Replace `<YOUR_JWT_TOKEN>` with the actual JSON Web Token obtained after logging in).
    *   `Content-Type`: `application/json`
*   **Request Body** (JSON):
    ```json
    {
        "id_following": <USER_ID_TO_UNFOLLOW>
    }
    ```
    *   `id_following` (integer, required): The ID of the user that the authenticated user wishes to unfollow.

*   **Responses**:

    *   **Success (200 OK)**:
        ```json
        {
            "message": "Unfollowed successfully"
        }
        ```
    *   **Error - Missing `id_following` (400 Bad Request)**:
        ```json
        {
            "error": "Missing id_following"
        }
        ```
    *   **Error - Cannot unfollow oneself (400 Bad Request)**:
        ```json
        {
            "error": "You cannot unfollow yourself"
        }
        ```
    *   **Error - Token missing or invalid (401 Unauthorized)**:
        ```json
        {
            "error": "Token missing or invalid"
        }
        ```
    *   **Error - Token expired (401 Unauthorized)**:
        ```json
        {
            "error": "Token expired"
        }
        ```
    *   **Error - Invalid token (401 Unauthorized)**:
        ```json
        {
            "error": "Invalid token"
        }
        ```
    *   **Error - Follow relationship not found (404 Not Found)**:
        ```json
        {
            "error": "Follow relationship not found or already inactive"
        }
        ```

---

This README should provide a good starting point for understanding the project.
