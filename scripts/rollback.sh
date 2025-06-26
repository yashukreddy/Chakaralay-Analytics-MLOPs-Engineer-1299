DEPLOYMENT_NAME="animal-identification-app"
NAMESPACE="default"

kubectl rollout undo deployment/$DEPLOYMENT_NAME --namespace=$NAMESPACE