import redis

conexion = redis.StrictRedis(host = '127.0.0.1', port ='6379')
cadena = "{palabra:ahuevao, significado:idiota}"

conexion.incr('slam:key', 1)
conexion.hset("slam", 1  )



datos = conexion.hgetall("slam")
for dato in  datos:
    print(datos)


conexion.hdel('slam', 2)






