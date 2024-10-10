# MicroTimeServer

A container that listens on port 54321 and responds to a GET /time HTTP request with the current time in JSON format.

## Use case

I have several Raspberry Pi Picos that run simple MicroPython scripts that need to know the current time. I can't use NTP because they are not connected to the internet, so I wrote this container to provide the time in a format that is easy to parse by MicroPython.

This way I don´t have to use the ntptime package, which is very dependend on the internet connection and can fail if there is no internet connection.

## Example Usage

```bash
curl http://localhost:54321/time
```

```json
{
    "current_time": "2024-10-10T14:03:44.544950+02:00", 
    "date": "2024-10-10", 
    "time": "14:03:44", 
    "offset": "+0200", 
    "timezone": "CEST", 
    "timestamp": 1728561824.54495
}
```

## Build

```bash
git clone https://github.com/varkenvarken/MicroTimeServer.git
cd MicroTimeServer
docker compose build
```

