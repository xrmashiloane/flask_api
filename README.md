
# Flask API App 

Use Flask to expose API endpoint


## Deployment

To deploy this project run


```bash
  docker build --tag flask_api .
```

```bash
  docker run -p 5001:4000 -d flask_api
```


## Lessons Learned

  1. Started with running flask app locally to ensure endpoints were working
  2. Once completed moved app onto docker
  3. Files are handled different on write, had to change from native Flask method to Python one. 
  


## Authors

- [@xrmashiloane](https://www.github.com/xrmashiloane)

