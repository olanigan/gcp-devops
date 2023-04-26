## GKE config 

### CloudShell Access
```
gcloud container clusters get-credentials [GKE_NAME] --zone [ZONE] --project [PROJECT_NAME]
```

### Workstation Access

- Install GKE Auth plugin for local Kubectl access
`gcloud components install gke-gcloud-auth-plugin`

```
gcloud container clusters get-credentials [GKE_NAME] --zone [ZONE] --project [PROJECT_NAME] >>> gke_kubeconfig.yaml
```