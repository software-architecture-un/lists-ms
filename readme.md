# lists_ms 

Microservicio encargado del manejo de listas para los lugares a visitar . .

Se usa como lenguaje base **Python 3**, con el framework Django REST.

Como base de datos se usa PostgreSQL.

### Ejecución

En la carpeta del archivo ejecutar las siguientes instucciones:

1. Añadir ip del nodo al archivo lists_ms/setting.py , en el arreglo ALLOWED_HOSTS.
2. Ejecutar `docker-compose build`
3. Ejecutar `docker-compose up`.

####ENDPOINTS Y RETORNO

-     POST /lists-ms/list
      -     Body (cURL)
~~~
-F id_user=1 \
-F 'name=Lista 1' \
-F comment=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOOOOOOOOOOOOOOOXXXX \
-F estimatedDate=2019-05-05
~~~
      -   Response       
~~~
{
    "content": {
        "id": 1,
        "id_user": 1,
        "name": "Lista 1",
        "comment": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOOOOOOOOOOOOOOOXXXX",
        "estimatedDate": "2019-05-05"
    },
    "message": "List was created"
}
~~~
        - Sin id_user:
          - Response:
~~~
{
    "content": {},
    "message": {
        "id_user": [
            "This field is required."
        ]
    }
}
~~~

