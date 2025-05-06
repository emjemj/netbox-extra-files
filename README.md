# Extra Files

This plugin adds a general purpose file area to the Circuits view.

## Set up for local development
Use this docker-compose stack:
https://github.com/netbox-community/netbox-docker

Map development tree into netbox and netbox-housekeeping container via Docker volume in docker-compose.override:
```
services:
  netbox:
    ports:
      - 8000:8080
    volumes:
      - ../netbox-extra-files:/netbox-extra-files:z
  netbox-worker:
    volumes:
      - ../netbox-extra-files:/netbox-extra-files:z
  netbox-housekeeping:
    volumes:
      - ../netbox-extra-files:/netbox-extra-files:z
```

### Install plugin in development/editable mode
```
docker compose up
docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
docker compose exec -u root netbox /usr/local/bin/uv pip install -e /netbox-extra-files
docker compose exec -u root netbox-worker /usr/local/bin/uv pip install -e /netbox-extra-files
docker compose exec -u root netbox-housekeeping /usr/local/bin/uv pip install -e /netbox-extra-files
```

### Enable Plugin
```
vi ./configuration/configuration.py
```

Add this line:
```
PLUGINS = [ 'extra_files' ]
```

### Restart docker compose
```
^C
docker compose up
```
