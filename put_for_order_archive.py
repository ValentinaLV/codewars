# def put(self, uuid):
#     json_data = request.json
#     order_archive = OrderArchive.query.filter_by(uuid=uuid).first()
#     if not order_archive:
#         return {'message': 'No such Order in Archive'}, 404
#     try:
#         updated_order_archive = order_archive_schema.load(json_data, session=db.session)
#         order_archive.id_user = updated_order_archive.id_user
#         order_archive.id_order = updated_order_archive.id_order
#         order_archive.id_product = updated_order_archive.id_product
#         order_archive.price = updated_order_archive.price
#         db.session.commit()
#     except ValidationError as e:
#         return {"message": str(e)}, 422
#     return order_archive_schema.dump(order_archive)

a = 5
b = a
print(id(a), id(b))
print(a == b)
b = 7
print(id(a), id(b))
print(a == b)
print(hash(a), hash(b))
