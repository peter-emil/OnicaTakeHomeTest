import dataclasses
import typing


class UserId(str):
    pass


class Name(str):
    pass


@dataclasses.dataclass
class UserDetails:
    firstName: typing.Optional[Name]
    lastName: typing.Optional[Name]


@dataclasses.dataclass
class User:
    id: UserId
    details: UserDetails


def user_factory(
        id: typing.Union[UserId, str],
        firstName: typing.Union[Name, str, None] = None,
        lastName: typing.Union[Name, str, None] = None,
        *args, **kwargs
):
    return User(
        id=id,
        details=UserDetails(
            firstName=firstName,
            lastName=lastName
        )
    )