# url2dom

## Chrome Browser as a Service in Docker Container
## for SPAs scrapping

### Build
```
make build 
```

### Run
```
make run 
```

### Use

Obtain HTML from url
```
POST http://localhost:8001/
BODY {
  "url": "URL_TO_SCRAP"
}
```

Obtain values from url + [ xpath ]
```
POST http://localhost:8001/
BODY {
  "url": "URL_TO_SCRAP",
  "xpath": [ "xpath1", "xpath2", ..., "xpathN"
}
```
