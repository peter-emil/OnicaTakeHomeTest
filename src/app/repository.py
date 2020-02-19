import abc
import typing
import boto3
from src import constants
from src.app import entities


class UserRepository(abc.ABC):
    def get_user_list(self) -> typing.List[entities.UserId]:  # I am pretending pagination doesn't exist
        pass

    def get_user(self, user_id: entities.UserId) -> entities.User:
        pass


class DynamoDbUserRepository(UserRepository):
    def __init__(self):
        dynamodb = boto3.resource(
            'dynamodb'
        )
        self.client = dynamodb.meta.client
        if not self.table_exists():
            raise RuntimeError("DynamoDB table does not exist")
        self.table = dynamodb.Table(constants.DYNAMODB_TABLE_NAME)

    def table_exists(self) -> bool:
        try:
            self.client.describe_table(TableName=constants.DYNAMODB_TABLE_NAME)
            return True
        except self.client.exceptions.ResourceNotFoundException:
            return False

    def get_user_list(self) -> typing.List[entities.UserId]:
        user_id_list_response = self.table.scan(
            AttributesToGet=[
                'id',
            ]
        )['Items']
        return [entities.UserId(user['id']) for user in user_id_list_response]

    def get_user(self, user_id: entities.UserId) -> typing.Optional[entities.User]:
        try:
            response = self.table.get_item(
                Key={
                    'id': user_id,
                }
            )['Item']
            return entities.user_factory(
                **response
            )
        except KeyError:
            return None


def get_user_repository() -> typing.Type[UserRepository]:
    return DynamoDbUserRepository()
