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

Get HTML from url
```
http://localhost:8001/?url=URL_TO_SCRAP
```

Get HTML from url + xpath
```
http://localhost:8001/url=URL_TO_SCRAP&xpath=XPATH_SELECTOR
```
