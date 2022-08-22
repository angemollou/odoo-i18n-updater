#!/usr/bin/bash

docker exec -t devcontainer_web_1 bash -c '/usr/bin/odoo --db_host ${DB_HOST} --database odoo --db_user ${DB_USER} --db_password ${DB_PASSWORD} --update ${MODULE_NAME} --stop-after-init' && \
docker container restart devcontainer_web_1
