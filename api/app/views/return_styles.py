from flask import jsonify


class ListStyle():
    @staticmethod
    def list(select, request):
        list = []
        for items in select:
            list.append(items.to_dict())
        return {'data': list}
