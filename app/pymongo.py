import pymongo
conn_str = "mongodb://mongo-0.mongo.mongo.svc.cluster.local:27017,mongo-1.mongo.mongo.svc.cluster.local:27017," \
           "mongo-2.mongo.mongo.svc.cluster.local:27017/?replicaSet=rs0&authSource=db01&tls=true" \
           "&tlsCertificateKeyFile=/rs0-client/dbuser01.pem&tlsCAFile=/rs0-ca/rs0-ca.pem "

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")