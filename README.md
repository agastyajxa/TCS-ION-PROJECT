# TCS iON Internship Project

A fully containerized Jenkins CI/CD pipeline deployed on AWS. This project integrates Docker, Jenkins, and AWS services to automate software delivery, ensuring scalability, efficiency, and reliability for modern DevOps workflows.

## 🚀 Features
- **Containerized Jenkins Setup** – Runs Jenkins inside a Docker container for a portable CI/CD environment.
- **Automated CI/CD Pipeline** – Streamlines build, test, and deployment processes.
- **AWS Deployment** – Leverages AWS EC2 for Jenkins and manages infrastructure efficiently.
- **Scalability** – Designed to scale with cloud-based deployments.
- **Security Best Practices** – Uses SSH key authentication and secure credentials management.

## 🛠️ Technologies Used
- **Jenkins** – Automates CI/CD workflows
- **Docker** – Containers for Jenkins and application services
- **AWS EC2** – Cloud hosting for Jenkins and supporting services
- **GitHub** – Version control and integration with Jenkins

## 📌 Prerequisites
Ensure you have the following installed/configured:
- AWS Account & EC2 instance
- Docker & Docker Compose
- SSH Key Pair for EC2 access
- Jenkins installed inside a Docker container
- Proper security group rules for Jenkins (port 8080)

## 📖 Setup & Installation

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/agastyajxa/TCS-ION-PROJECT.git
 cd TCS-ION-PROJECT
```

### 2️⃣ Configure AWS EC2 & Security Groups
- Launch an EC2 instance
- Allow inbound traffic on port `8080` (Jenkins), `22` (SSH)
- SSH into the instance:
  ```sh
  ssh -i your-key.pem ubuntu@your-ec2-instance-ip
  ```

### 3️⃣ Run Jenkins in Docker
```sh
docker-compose up -d
```

### 4️⃣ Access Jenkins
- Open a browser and go to:
  ```
  http://your-ec2-instance-ip:8080
  ```
- Retrieve the initial admin password:
  ```sh
  docker exec -it jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword
  ```
- Complete the setup and install required plugins.

### 5️⃣ Configure Jenkins Pipeline
- Connect Jenkins to your GitHub repository
- Create a new pipeline and configure it to use the `Jenkinsfile` from the repository.



## ✅ CI/CD Workflow
1. **Code Push** – Developers push code to GitHub.
2. **Jenkins Trigger** – Jenkins pulls the latest code.
3. **Build & Test** – Jenkins builds and tests the application inside containers.

## 📌 Future Improvements
- Integrate Kubernetes for orchestration
- Integrate Monitoring Tools
- Automate infrastructure setup using Terraform
- Implement Blue-Green Deployment Strategy

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

🎯 **Contributions are welcome!** Feel free to fork the repository and submit pull requests.

💬 Need help? Open an [issue](https://github.com/agastyajxa/TCS-ION-PROJECT/issues) or reach out!

