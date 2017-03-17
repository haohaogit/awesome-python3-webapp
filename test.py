# import orm
# from models import User, Blog, Comment
#
# def test():
#     yield from orm.create_pool(loop=loop,user='www', password='www', database='awesome')
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#     yield from u.save()
#
# for x in test():
#     print("%%%%%")
import orm,sys
from models import User, Blog, Comment
import asyncio

@asyncio.coroutine
def destory_pool():

    #global __pool
    if orm.__pool is not None :
        orm.__pool.close()
        yield from orm.__pool.wait_closed()
@asyncio.coroutine
def test():
    yield from orm.create_pool(user='www-data', password='www-data', db='awesome',loop=loop,host='localhost', port=3306,)

    #u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank') #重复执行会报错，因为email 有建立unique Key 约束

    #yield from u.save()

    yield from User(id='0014881168199670ae1cd311c2c4aad9b31dbb9bcb312ae000').remove()
    r = yield from User.findAll()
    print(r)
    yield from destory_pool()
#创建异步事件的句柄
loop = asyncio.get_event_loop()
loop.run_until_complete(test())

loop.close()

if loop.is_closed():
    sys.exit(0)