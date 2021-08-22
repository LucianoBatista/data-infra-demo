# Data Infra on K8s

## Pre-Requisites

You'll need to have the following tools installed to run this example.

- docker
- kinD
- helm
- kubectl
- kubens and kubectx CLI


## Creating the environment

### Create the cluster

As we'll be setting up a lot of big data tools, I'll not restrict the resources of the cluster.

Go to the folder `00_cluster` and run:

```bash
$ kind create cluster --name big-data-infra --config $ kind-cluster.yaml
```

If you look at the cluster resources, you'll see that your whole machine will be available for the cluster.

```bash
$ kubectl describe nodes
```

### Mysql 

Now, we'll be setting up a MySQL database and put some data to work with.

At this point, we'll be using mostly helm charts to install all the tools that we need. But before that we'll create a namespace specific to the mysql.

```bash
$ kubectl create namespace mysql-app-storage
$ kubens mysql-app-storage
```

Installing mysql...

```bash
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm install mysql bitnami/mysql --namespace mysql-app-storage
```

Exposing the port.

```bash
$ kubectl port-forward mysql-0 3306:3306
```


### Data Lake

Building a Data Lake with MinIO.


### Spark

Configuring a Spark On K8s Operator to run.


### Pinot

Building an OLAP datastore.


### Superset

Building a data viz tool.


## Airflow

Creating an orquestration with Airflow to move the data between those steps.