# Import required libraries
import subprocess

# Define your deployment function
def deploy():
    # Clone the Git repository
    subprocess.run(['git', 'clone', 'https://github.com/apargc61/Quadratic-Equation-Solver.git'])

    # Build the Docker image
    subprocess.run(['docker', 'build', '-t', 'your-image-name', '.'])

    # Push the Docker image to Docker Hub (or another container registry)
    subprocess.run(['docker', 'push', 'your-image-name'])

    # Deploy the Docker image to your Kubernetes cluster
    subprocess.run(['kubectl', 'apply', '-f', 'your-deployment.yaml'])

# Call your deployment function
deploy()
