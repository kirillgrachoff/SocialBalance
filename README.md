# Social Balance Service

I think, it is very useful

## How to use
I hope, I'll develop it using docker...

# Docker usage
```
docker build -t <container-name> -f docker/Dockerfile .
docker run --rm -p 5000:5000 -v "$PWD":/data <container-name>
```
`-v "$PWD":/data` - to specify place, where database.db is placed