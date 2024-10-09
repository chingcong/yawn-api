# yawn-tornado

A lightweight web application boilerplate built using Tornado, designed for high-performance, non-blocking network applications. This project aims to provide a robust foundation for developing RESTful APIs and handling real-time web features with ease.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [License](#license)
- [Contributing](#contributing)

## Features

- **Asynchronous Processing**: built on the Tornado framework, allowing for non-blocking requests and efficient handling of concurrent connections.
- **Custom Error Handling**: utilizes Pydantic models for structured error responses.
- **Health Check**: built-in health check endpoints to monitor the status of the application and its dependencies.
- **Configuration Management**: easy configuration using environment variables and a dedicated configuration class.

## Installation

To set up yawn-tornado on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/chingcong/yawn-tornado.git
   cd yawn-tornado
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:

   ```bash
   pytohn3 -m pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root with your environment variables (e.g., database URL, secret keys).

## Usage

To start the server, use the following command:

```bash
python3 server.py
```

This will start the Tornado web server on the specified host and port (default: `localhost:8888`).

You can access the API at `http://localhost:8888`.

### Example API Call

To make a GET request to the health check endpoint, you can use `curl`:

```bash
curl http://localhost:8888/health
```

This will return a JSON response with the health status of the application.

## Configuration

Configuration options are managed via a `configs` folder. You can modify the `Config` class to adjust settings such as:

- **Server Settings**: number of workers, timeout settings.
- **Database Configuration**: connection strings and options.
- **Logging Level**: set the logging level for the application.

### Example `.env` File

```env
APP_ENV=dev
APP_VERSION=1.0.0
APP_SERVER_HOST=localhost
APP_SERVER_PORT=8000
```

## Endpoints

The following endpoints are available:

### Health Check

- **GET /healthcheck**
  - Description: check the health of the application and its dependencies.
  - Response: JSON object with health status.

#### Sample Response

```json
{
  "redis": "OK",
  "database": "OK",
  "application": {
    "name": "YAWN"
  },
  "version": "1.0.0",
  "env": "development"
}
```

## Error Handling

yawn-tornado uses Pydantic models to handle errors gracefully. The response format is consistent across different types of errors, ensuring easy integration for clients.

### Example Error Responses

1. **Internal Server Error**

   ```json
   {
     "code": "INTERNAL_SERVER_ERROR",
     "status": 500,
     "message": "Internal server error"
   }
   ```

2. **Database Connection Error**

   ```json
   {
     "code": "DATABASE_CONNECTION_ERROR",
     "status": 500,
     "message": "Database connection error"
   }
   ```

## Logging

Logging is configured using Python's built-in logging module. The default logging level is set to `INFO`. You can customize the logging configuration in the `configs` module. Logs are written to the console and can be redirected to a file if needed.

### Example Log Output

```
INFO:__main__:Application started on http://localhost:8888
INFO:__main__:Health check passed: Redis and database are reachable.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a pull request.

For any issues or feature requests, please open an issue in the GitHub repository.

---

Thank you for using yawn-tornado! I hope it meets your needs for building fast and scalable web applications.

```

### Additional Considerations

- **Add More Endpoints**: if your application has additional endpoints, describe them in the "Endpoints" section.
- **Usage Examples**: provide examples of how to use your endpoints with sample requests and responses.
- **Detailed Configuration Options**: if your application has many configurable options, consider adding a detailed explanation of each one.

Feel free to adjust any parts of this template to better fit your project’s needs! If you have more specific content or sections you want to add, let me know!
```
