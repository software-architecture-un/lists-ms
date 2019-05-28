# lists_ms 

Microservicio encargado del manejo de listas para los lugares a visitar . .

Se usa como lenguaje base **Python 3**, con el framework Django REST.

Como base de datos se usa PostgreSQL.

### Ejecución

En la carpeta del archivo ejecutar las siguientes instucciones:

1. Añadir ip del nodo al archivo lists_ms/setting.py , en el arreglo ALLOWED_HOSTS.
2. Ejecutar `docker-compose build`
3. Ejecutar `docker-compose run lists-ms python3 manage.py migrate`.
4. Ejecutar `docker-compose run lists-ms python3 manage.py makemigrations `.
5. Ejecutar `docker-compose up`.
