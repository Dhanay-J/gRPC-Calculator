# gRPC-Calculator

A basic Calculator API implemented using gRPC in Python.

## Requirements

- **Operating System**: Windows 11
- **Python Version**: 3.12.0

## Installation Steps

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Dhanay-J/gRPC-Calculator.git
```

### 2. Navigate to the Project Directory

Change to the project directory:

```bash
cd gRPC-Calculator
```

### 3. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
py -m venv env
```

### 4. Activate the Virtual Environment

Activate the virtual environment:

```bash
.\env\Scripts\activate
```

### 5. Install Required Dependencies

Install the necessary dependencies from the `requirements.txt` file:

```bash
py -m pip install -r requirements.txt
```

### 6. Generate Python Code from Proto File

Use `grpc_tools.protoc` to generate the Python code from the `.proto` file:

```bash
py -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. .\calc.proto
```

### 7. Start the gRPC Server

Run the server to handle client requests:

```bash
py calc_server.py
```

### 8. Run the gRPC Client

In a separate terminal window, run the client to interact with the server:

```bash
py calc_client.py
```

---

## Notes

- Ensure that the virtual environment is activated whenever you are working on the project.
- The server and client should be running in separate terminal instances.
- If you encounter any issues, check that all dependencies are correctly installed and that the `.proto` file is properly compiled.

Feel free to modify the code to extend the functionality of the calculator API or add additional features.

```

```
