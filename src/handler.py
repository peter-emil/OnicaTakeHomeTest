import json
import dataclasses
import logging
from src.app import main


def get_user_id_from_event(event):
    chain = ['requestContext', 'path']
    current = event
    for next in chain:
        current = current.get(next)
        if current is None:
            break
    else:
        current = str(current)
        candidate_id = current.split('/')[-1]
        if not candidate_id.isnumeric():
            return None
        return candidate_id
    return current


class DataclassJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            return super().default(o)
        except TypeError:
            if not dataclasses.is_dataclass(o):
                raise
            return dataclasses.asdict(o)


def get_user_list_handler(event, context):
    try:
        body = main.get_list_of_users()
        return {
            'statusCode': 200,
            'body': json.dumps(
                body,
                cls=DataclassJsonEncoder
            )
        }
    except Exception as e:
        logging.fatal(e)
        raise


def get_user_handler(event, context):
    try:
        user_id = get_user_id_from_event(event=event)
        body = main.get_user(user_id=user_id)
        if body is not None:
            return {
                'statusCode': 200,
                'body': json.dumps(
                    body,
                    cls=DataclassJsonEncoder
                )
            }
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }
    except Exception as e:
        logging.fatal(e)
        raise
