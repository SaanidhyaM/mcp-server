# mcp-server
run with 

```bash
Invoke-WebRequest -Uri "http://127.0.0.1:5050/clone" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"text": "Hello, my name is saanidhya", "voice_id": "your_voice_id", "api_key": "your_api_key"}'
```
