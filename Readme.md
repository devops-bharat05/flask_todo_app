# 📝 To-Do List Application

![Alt text](./imgs/to-do-list-word-concepts-banner.jpg)

A simple, clean, and efficient To-Do List web application built with Flask, designed to help you keep track of tasks and manage your daily to-do items effectively. This app also includes a CI/CD pipeline setup using GitHub Actions for automated testing and deployment.

---

## 🌟 Features

- 🗓️ **Date-Based Task Management**: Organize tasks with the current date.
- 🆕 **Add New Tasks**: Add items to your to-do list quickly.
- 🧹 **Clear Task List**: Remove all tasks with a single click.
- ❌ **Delete Specific Tasks**: Remove individual tasks after completion.
- 🕒 **Live Clock**: Display the current time for convenience.
- 🚀 **CI/CD Pipeline**: Automated testing and deployment using GitHub Actions.

---

### Project Structure

Folder structure for the project:

```
to-do-list-flask-app/
├── app.py                    # Main Flask application
├── requirements.txt          # Dependencies for the app
├── templates/
│   └── home.html             # HTML template for the app
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # GitHub Actions workflow file
├── tests/
    └── test_app.py           # Unit tests for the app

```

---

## 🖼️ Screenshots

### Homepage
![Homepage](https://user-images.githubusercontent.com/xyz/your-homepage-image-path.png)

### Task List
![Task List](https://user-images.githubusercontent.com/xyz/your-tasklist-image-path.png)

---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **CI/CD**: GitHub Actions

---

## 🚀 Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- Flask and other dependencies in `requirements.txt`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the app**: Open `http://127.0.0.1:5000` in your web browser.

---

## ⚙️ CI/CD Pipeline with GitHub Actions

This project uses GitHub Actions to automate testing and deployment for the To-Do List app.

### 🛠️ Workflow Configuration

The GitHub Actions workflow file is located at `.github/workflows/ci-cd.yml`. The pipeline performs the following steps:

- **Install Dependencies**: Installs the required Python packages.
- **Run Tests**: Executes the test suite using `pytest`.
- **Deploy to Staging**: Deploys to a staging environment when changes are pushed to the `staging` branch.
- **Deploy to Production**: Deploys to production when a release is tagged.

### 🔒 Environment Secrets

To deploy successfully, add the following secrets to your GitHub repository:

- `STAGING_ENV_VAR`
- `PRODUCTION_ENV_VAR`

For more information on managing secrets, refer to [GitHub's documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

---

## 🧪 Running Tests

To run tests locally:

1. Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests using `pytest`:
   ```bash
   pytest tests/
   ```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🖊️ Author

👤 **Your Name**

- GitHub: [@devops-bharat05](https://github.com/devops-bharat05)
- LinkedIn: [@Bharat Bhushan](https://www.linkedin.com/in/bharat-bhushan-devops)

---

## 📣 Acknowledgments

Special thanks to the open-source community and Flask for making web development easy and enjoyable.

---

**Enjoy managing your tasks! 🗒️✨**
