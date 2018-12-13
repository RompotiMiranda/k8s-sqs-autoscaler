# k8s-sqs-autoscaler
Kubernetes pod autoscaler based on queue size in AWS SQS

## Usage

Parameters:

 - sqs_queue_name
 - kubernetes_deployment_selector: which deployments to scale, something like "app=pymoab" 
 - kubernetes_namespace
 - poll_period: seconds. how often to check if scaling is needed 
 - scale_up_messages/scale_down_messages: how many message have to be in the queue before we scale up/down
 - scale_down_cool_down/scale_up_cool_down: how many seconds to wait between consecutive scale up/down events. this help prevent thrashing by scaling up too fast 
 - max_pods/min_pod: how far to scale

Create a kubernetes deployment like this:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: my-k8s-autoscaler
spec:
  revisionHistoryLimit: 1
  replicas: 1
  template:
    metadata:
      labels:
        app: my-k8s-autoscaler
    spec:
      containers:
      - name: my-k8s-autoscaler
        image: sideshowbandana/k8s-sqs-autoscaler:1.0.0
        command:
          - ./k8s-sqs-autoscaler
          - --sqs-queue-url=https://sqs.$(AWS_REGION).amazonaws.com/$(AWS_ID)/$(SQS_QUEUE) # required
          - --kubernetes-deployment=$(KUBERNETES_DEPLOYMENT)
          - --kubernetes-namespace=$(K8S_NAMESPACE) # optional
          - --aws-region=us-west-2  #required
          - --poll-period=10 # optional
          - --scale-down-cool-down=30 # optional
          - --scale-up-cool-down=10 # optional
          - --scale-up-messages=20 # optional
          - --scale-down-messages=10 # optional
          - --max-pods=30 # optional
          - --min-pods=1 # optional
        env:
          - name: K8S_NAMESPACE
            valueFrom:
              fieldRef:
                fieldPath: metadata.namespace
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "1512Mi"
            cpu: "500m"
        ports:
        - containerPort: 80

```
