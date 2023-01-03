import motor.motor_asyncio

conn_str = "mongodb://mongo-0.mongo.mongo.svc.cluster.local:27017,mongo-1.mongo.mongo.svc.cluster.local:27017," \
           "mongo-2.mongo.mongo.svc.cluster.local:27017/?replicaSet=rs0&authSource=db01&tls=true" \
           "&tlsCertificateKeyFile=/rs0-client/dbuser01.pem&tlsCAFile=/rs0-ca/rs0-ca.pem "
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)

db = client.db01

collections = db.users
