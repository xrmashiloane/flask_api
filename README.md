
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


## API Reference

#### Get average load, available disk on file system

```http
  GET /utilisation
```


#### Get value

```http
  GET /value
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Update value, provide JSON with key return_value

```http
  POST /value
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `return_value`      | `int` | **Required**. key to update |



## Lessons Learned

  1. Started with running flask app locally to ensure endpoints were working
  2. Once completed moved app onto docker
  3. Files are handled different on write, had to change from native Flask method to Python one. 
  


## Authors

- [@xrmashiloane](https://www.github.com/xrmashiloane)

