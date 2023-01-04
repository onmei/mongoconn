import asyncio
import motor.motor_asyncio


async def get_server_info() -> object:

    conn_str = "mongodb://mongo-0.mongo.mongo.svc.cluster.local:27017,mongo-1.mongo.mongo.svc.cluster.local:27017," \
               "mongo-2.mongo.mongo.svc.cluster.local:27017/?replicaSet=rs0&authSource=db01&tls=true" \
               "&tlsCertificateKeyFile=/rs0-client/dbuser01.pem&tlsCAFile=/rs0-ca/rs0-ca.pem "
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")

loop = asyncio.get_event_loop()

loop.run_until_complete(get_server_info())
# db = client.db01

# collections = db.users
