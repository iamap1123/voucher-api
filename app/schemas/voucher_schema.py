from apiflask.schemas import Schema
from apiflask.fields import Integer, String, DateTime, Boolean, Float, Date
from marshmallow import validates_schema, ValidationError
from marshmallow.validate import Range, Length, OneOf
from .date_validator import wrong_date_range


class VoucherOutputSchema(Schema):
    id = Integer()
    name = String()
    discount_amount = Integer()
    discount_percentage = Float()
    effective_date_from = Date()
    effective_date_end = Date()
    status = String()
    valid = Boolean()
    created_at = DateTime()
    updated_at = DateTime()


class VoucherCreateSchema(Schema):
    name = String(required=True, validate=[Length(min=1, max=50)])
    discount_amount = Integer(
        required=True,
        validate=[Range(min=1, error="Discount amount must be greater than 0")],
    )
    discount_percentage = Float(
        required=True,
        validate=[
            Range(min=0.01, error="Discount percentage must be greater than 0.01"),
            Range(max=1, error="Discount percentage must be less than 1"),
        ],
    )
    effective_date_from = Date(required=True)
    effective_date_end = Date(required=True)
    status = String(required=True, validate=OneOf(["unused", "used", "expired"]))
    valid = Boolean(validate=OneOf([True, False]))

    @validates_schema
    def validate_effective_date(self, data, **kwargs):
        if wrong_date_range(data):
            raise ValidationError("Effective end should be later than effective from.")


class VoucherUpdateSchema(Schema):
    name = String(required=True, validate=[Length(min=1, max=50)])
    discount_amount = Integer(
        validate=[Range(min=1, error="Discount amount must be greater than 0")]
    )
    discount_percentage = Float(
        validate=[
            Range(min=0.01, error="Discount percentage must be greater than 0.01"),
            Range(max=1, error="Discount percentage must be less than 1"),
        ]
    )
    effective_date_from = Date()
    effective_date_end = Date()
    status = String(validate=OneOf(["unused", "used", "expired"]))
    valid = Boolean(required=True, validate=OneOf([True, False]))

    @validates_schema
    def validate_effective_date(self, data, **kwargs):
        if wrong_date_range(data):
            raise ValidationError("Effective end should be later than effective from.")


class VoucherSearchSchema(Schema):
    name_like = String()
    discount_amount = Integer(
        validate=[Range(min=1, error="Discount amount must be greater than 0")]
    )
    discount_percentage = Float(
        validate=[
            Range(min=0.01, error="Discount percentage must be greater than 0.01"),
            Range(max=1, error="Discount percentage must be less than 1"),
        ]
    )
    effective_date_from = Date()
    effective_date_end = Date()
    status = String(validate=OneOf(["unused", "used", "expired"]))
    valid = Boolean(validate=OneOf([True, False]))
    created_at = Date()
    updated_at = Date()
