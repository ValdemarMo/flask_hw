import hashlib
from typing import Type

import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from auth import hash_password
from models import Session, Ad

# from schema import CreateUser, UpdateUser, CreateAd

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: str | dict | list):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    response = jsonify({"status": "error", "message": er.message})
    response.status_code = er.status_code
    return response


def get_ad(session: Session, ad_id: int):
    ad = session.get(Ad, ad_id)
    print(ad)
    if ad is None:
        raise HttpError(404, "ad not found")
    return ad


class AdViews(MethodView):
    def get(self, ad_id: int):
        with Session() as session:
            ad = get_ad(session, ad_id)
            return jsonify(
                {
                    "id": ad.id,
                    "owner": ad.owner,
                    "title": ad.title,
                    "description": ad.description,
                    "creation_time": ad.creation_time.isoformat(),
                }
            )
        pass

    def post(self):
        with Session() as session:
            new_ad = Ad(**request.json)
            session.add(new_ad)
            session.commit()
            return jsonify({"id": new_ad.id})

    def delete(self, ad_id: int):
        with Session() as session:
            ad = get_ad(session, ad_id)
            session.delete(ad)
            session.commit()
            return jsonify({"status": "deleted"})


ad_view = AdViews.as_view("ad")

app.add_url_rule(
    "/ad/<int:ad_id>",
    view_func=ad_view,
    methods=["GET", "DELETE"],
)
app.add_url_rule("/ad", view_func=ad_view, methods=["POST"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
