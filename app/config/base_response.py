from apiflask import Schema
from apiflask.fields import String, Integer, Field


class BaseResponse(Schema):
    data = Field()
    message = String()
    code = Integer()
