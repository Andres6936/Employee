import json
import os

from azure.cosmos import CosmosClient, DatabaseProxy, ContainerProxy


class Connector:
    def __init__(self):
        self.client = CosmosClient(os.environ["ACCOUNT_URI"], os.environ["ACCOUNT_KEY"])

    def getDatabase(self) -> DatabaseProxy:
        return self.client.get_database_client("SampleDB")

    def getContainer(self, database: DatabaseProxy) -> ContainerProxy:
        return database.get_container_client("SampleContainer")

    def getUser(self):
        database: DatabaseProxy = self.getDatabase()
        container: ContainerProxy = self.getContainer(database)
        items = container.query_items(
            query="SELECT * FROM SampleContainer S WHERE S.id = '027D0B9A-F9D9-4C96-8213-C8546C4AAE71'")
        for item in items:
            print(json.dumps(item, indent=True))

    def saveUser(self):
        pass

    def removeUser(self):
        pass

    def updateUser(self):
        pass
