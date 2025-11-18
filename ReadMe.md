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

### Docker Build Success
![Build Success](screenshots/docker_build_success.png)

### Docker Run
![Build Success 2](screenshots/docker_run_output.png)


### Files Inside Container
![Inside Container](screenshots/inside_container_files.png)


⸻

Summary

This lab demonstrates how to:
    •   Containerize a machine learning script with Docker
    •   Install and manage ML dependencies inside the image
    •   Run a modified Python ML workflow in isolation
    •   Produce reproducible and consistent training results


⸻
