```shell
 curl -d '{"num1" : [1, 2, 3], "num2":[4, 5, 6]}' -H "Content-Type: application/json" -X POST http://localhost:8080/process
```

```shell
docker run -p 8080:8080 python-ws
```