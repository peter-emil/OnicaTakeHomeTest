import typing
from src.app import entities
from src.app.repository import get_user_repository


repository = get_user_repository()


def get_list_of_users() -> typing.List[entities.UserId]:
    users = repository.get_user_list()
    return users


def get_user(user_id: entities.UserId) -> typing.Optional[entities.User]:
    if not user_id:
        return None
    user = repository.get_user(
        user_id=entities.UserId(user_id)
    )
    return user
