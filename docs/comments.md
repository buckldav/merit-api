```bash
python manage.py createapikey Blog --email=<email>
```

```bash
# CREATE
curl -X POST http://localhost:8000/api/comments/ -d '{content: "Test Comment"}' -H 'Authorization: Api-Key <api-key>' -H 'Content-Type: application/json'
# RETRIEVE
curl http://localhost:8000/api/comments/ -H 'Authorization: Api-Key <api-key>' -H 'Content-Type: application/json'
```
