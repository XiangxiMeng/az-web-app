# az-web-app

```ps1
docker build . --tag <image>:<version>
```

For local running

```ps1
docker run -p 8000:8000 <image>:<version>
```

Visit

http://localhost:8000/sleep/<secs>
http://localhost:8000/sleep1/<secs>
http://localhost:8000/sleep2/<secs>
http://localhost:8000/sleep3/<secs>
http://localhost:8000/sleep4/<secs>

http://localhost:8000/asleep/<secs>
http://localhost:8000/asleep1/<secs>
http://localhost:8000/asleep2/<secs>
http://localhost:8000/asleep3/<secs>
http://localhost:8000/asleep4/<secs>

asleep uses gevent for async sleep

Don't visit the same url at the same time in the same browser, because the browser will automatically put these requests in one queue.

In Azure Web App set WEBSITES_PORT=8000
