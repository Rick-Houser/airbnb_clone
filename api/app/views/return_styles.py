from flask import request


class ListStyle():
    @staticmethod
    def list(select, request):

        # Assigning a default values to page an number
        number = 10
        page = 1

        # Traversing the parameters and checking if number and page
        # exist in the URL of the request
        for value in request.args:
            if value == 'number':
                number = int(request.values.get('number'))
            elif value == 'page':
                page = int(request.values.get('page'))

        # creating a list for pagination
        list = []
        for items in select.paginate(page, number):
            list.append(items.to_dict())
        return {'data': list}
