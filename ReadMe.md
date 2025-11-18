# Docker Lab
```bash
    •   Added StandardScaler for feature normalization
    •   Replaced RandomForest with LogisticRegression (max_iter=500)
    •   Modified train-test split with a new random_state=123
    •   Printed model accuracy score for evaluation
    •   Saved model as iris_logistic_model.pkl and scaler.pkl
    •   Updated Dockerfile to use Python 3.11-slim
    •   Created custom requirements.txt for dependency control
    •   Executed the full ML pipeline inside Docker

```
⸻

Files in This Repository
```bash
Dockerfile          # Docker build instructions for Python 3.11 environment
main.py             # Customized ML training script (Logistic Regression)
requirements.txt    # Dependencies used inside the Docker container
screenshots/        # Build & run screenshots for lab submission

```
⸻

How to Build the Docker Image
```bash
docker build -t meenu-lab1 .
```

⸻

How to Run the Docker Container
```bash
docker run meenu-lab1
```
Expected output:
```bash
Model Accuracy: 0.97xx
Training completed — Logistic Regression model saved! by Meena

```
⸻

### Screenshots


Docker Build Success

Shows the complete Docker image build process, including dependency installation and successful tagging of the image.

screenshots/docker_build_success.png



Docker Run Output

Displays the model accuracy and the confirmation message after training is completed inside the Docker container.

screenshots/docker_run_output.png


Files Inside Container

Screenshot taken after entering the container with docker run -it meenu-lab1 sh
Shows that the model file and script files exist inside the /app directory.

screenshots/inside_container_files.png



GitHub Repository Directory View

Shows the final project structure on GitHub including Dockerfile, main.py, requirements.txt, README.md, and screenshots folder.

screenshots/github_repo_view.png


⸻

Summary

This lab demonstrates how to:
    •   Containerize a machine learning script with Docker
    •   Install and manage ML dependencies inside the image
    •   Run a modified Python ML workflow in isolation
    •   Produce reproducible and consistent training results


⸻
