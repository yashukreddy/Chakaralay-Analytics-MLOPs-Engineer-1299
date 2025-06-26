# MLOPs Engineer Role Challenge by Chakaralaya Analytics

## My Info:
- **Name**: Yashwanth Reddy  
- **Reg no**: 22BAI1299  
- **VIT Email ID**: yashwanth.reddy2022@vitstudent.ac.in  
- **GitHub**: [https://github.com/yashukreddy/](https://github.com/yashukreddy/)  
- **LinkedIn**: [https://www.linkedin.com/in/yashwanthreddykuchipudi](https://www.linkedin.com/in/yashwanthreddykuchipudi)

---

## ML Application:

I chose an animal identification ml project which detects which animal image is uploaded. I chose this project because it was done by me previously and I have a proper knowledge about it and another reason is it can get some meaningful metrics to track from the predictions apart from only API requests. In the training I used a transfer learning model.

> **Disclaimer**:  
> I couldn't build a docker image and load it into the minikube kubernetes because its huge size around 4GB. So I assume if everything was gone accordingly and the below steps I would have done since I previously have experience in working around dockers, minikube, helm, Prometheus and Grafana. I urged the same in my briefing video as well. Hope you understand.

---

## Containerization:

Docker was used for containerization with only the relevant resources which are necessary for the application to run on any platform. Its good practice to use .dockerignore file in which all the files and folder can be mentioned which are not necessary to build a docker image for a particular application, which make our image light and more convenient to access.

---

## Deployment in Kubernetes:

Kubernetes is a open source platform for distributed computing. It offers a powerful, scalable, and flexible platform to automate and manage the entire ML lifecycle — from development to deployment and monitoring. Namespaces are multiple virtual clusters inside the main Kubernetes cluster. I have used the default namespace to deploy this application.

---

## Monitoring:

Helm is a package manager which I used to install Prometheus and Grafana into my Kubernetes. These are the tools which helps to track the metrics and create visualization dashboards for statistical understanding of our model or application performance such are accuracy, latency, hits, etc. I assure you that I have knowledge about switching ports between the docker container and the pod and from the Kubernetes cluster to the external IP port.

Alarming is also another feature Grafana provided in which a certain threshold (set by us) is crossed or reached, it send us intimation through email service or even through other platforms or application which can be configured by us. I have used an alarm for the latest_confidence_score metric in which if the model accuracy was below 60, it fires an alarm.

---

## Deployment:

For CI-CD, GitHub Actions is opted. I have prepared an .yaml file for the continues deployment whenever a push action is done to the repository. It will automatically installs the requirements, builds the docker image, loads the image into the minikube environment and runs in the minikube pod.

Makefile is also written to automate the  building, loading, applying and more actions inside the minikube environment.

---

## NOTE:

All the relevant code used for the deployment of this application in provided in the repository. If any of the files are missing, it means I did not create or use that file for this deployment automation and is done manually by me.

The above description explains my understanding, integration thought process and my knowledge of these techniques and tools. I have not provided any code snippets as it only explains my understanding and working.
