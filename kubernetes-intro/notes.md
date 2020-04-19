### kubernetes installers
 - minikube
 - kind

### Vanila Dashboard
 - https://github.com/kubernetes/dashboard


### k9s 
 -  terminal UI to interact with your Kubernetes clusters


12. Создать Dockerfile в котором будет описан образ:

1. Запускающий web-сервер на порту 8000
2. Отдающий содержимое директории /app
3. Работающий с UID 1001

13. Dockerfile:

1. разместить в kubernetes-intro/web 
2. Собрать образ и разместить его в DockerHub

14. Написать манифест web-pod.yaml

    apiVersion: v1      # Версия API 
    kind: Pod           # Объект, который создаем
    metadata:
        name:           # Название Pod
        labels:         # Метки в формате key: value
            key: value
    spec:               # Описание Pod
        containers:     # Описание контейнеров внутри Pod
            - name:     # Название контейнера
              image:    # Образ из которого создается контейнер
