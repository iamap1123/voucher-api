from apiflask import APIFlask
from config.base_response import BaseResponse
from config.db import session
from models.voucher import Voucher
from sqlalchemy import delete
from schemas.voucher_schema import (
    VoucherCreateSchema,
    VoucherOutputSchema,
    VoucherUpdateSchema,
    VoucherSearchSchema,
)

app = APIFlask(__name__)

app.config["BASE_RESPONSE_SCHEMA"] = BaseResponse
app.config["JSON_SORT_KEYS"] = False


@app.get("/")
def index():
    return "<h2>Welcom to APIFlask assignment, please find more detail in <a href='/docs'>/docs</a><h2>"


@app.get("/vouchers")
@app.output(VoucherOutputSchema(many=True))
def get_all_vouchers():
    vouchers = session.query(Voucher).all()

    return {"data": vouchers, "message": "Query successfully!", "code": 200}


@app.post("/vouchers")
@app.input(VoucherCreateSchema(many=True))
@app.output(VoucherOutputSchema(many=True))
def create_new_voucher(json_data):
    vouchers = []
    for data in json_data:
        new_voucher = Voucher(**data)
        session.add(new_voucher)
        vouchers.append(new_voucher)

    session.commit()

    return {
        "data": vouchers,
        "message": "Create new vouchers successfully!",
        "code": 201,
    }


@app.patch("/voucher/<int:voucher_id>")
@app.input(VoucherUpdateSchema)
@app.output(VoucherOutputSchema)
def update_voucher(voucher_id, json_data):
    voucher = session.query(Voucher).filter(Voucher.id == voucher_id)
    count = voucher.count()
    code = 200
    message = "Update voucher Successfully!"

    if count > 0:
        voucher.update(json_data)
        session.commit()
    else:
        code = 404
        message = "No voucher found."

    return {"data": voucher.first(), "message": message, "code": code}


@app.delete("/voucher/<int:voucher_id>")
def delete_voucher(voucher_id):
    voucher = session.query(Voucher).filter(Voucher.id == voucher_id)
    count = voucher.count()
    code = 204
    message = "Delete voucher successfully!"

    if count > 0:
        session.execute(delete(Voucher).where(Voucher.id == voucher_id))
        session.commit()
    else:
        code = 404
        message = "No voucher found."

    return {"message": message, "code": code}


@app.post("/vouchers/search")
@app.input(VoucherSearchSchema)
@app.output(VoucherOutputSchema(many=True))
def search_voucher(json_data):
    query = session.query(Voucher)
    if "name_like" in json_data:
        name = "%{}%".format(json_data.pop("name_like"))
        query = query.filter(Voucher.name.like(name))

    vouchers = query.filter_by(**json_data).all()

    return {"data": vouchers, "code": 200}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
