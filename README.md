# May I take your /order?

Pizza-server app. Flask with Dockerfile, CI with Jenkinsfile, deploy with helm
The server will take orders in the form of json loads:
```jsonc
{
"pizza-type": "<margherita|pugliese|marinara>"
"size": "<personal|family>"
"amount": <int>
}
```

You can clone and test the app with:
```
docker build -t my-flask-app .
docker run -p 8080:8080 my-flask-app
```

A basic CI solution exists in the Jenkinsfile (get a Jenkins server up and running, add a pipeline or multi-branch pipeline)

To deploy on a k8s cluster please see the helm chart in the pizzaapp folder.
To deploy run:
```
helm upgrade --install pizza-app ./helm -f values.yaml
```

A sanity check is be available at https://<host url or LB that should redirect to port 8080>/health
(Or http://localhost:8080//health if running locally)


Check by posting e.g:
```jsonc
curl -X POST -H "Content-Type: application/json" -d '{
  "pizza-type": "margherita", //or other
  "size": "personal", //or family
  "amount": 2
}' https://<host url or LB that should redirect to port 8080>/order

#(Or http://localhost:8080/order if running locally)
```

