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

        # By default next_page_path and previous_page_path are none
        next_page_path = None
        previous_page_path = None
        base_path = request.base_url + "?page="
        end_path = "&number" + str(number)

        # updating the next_page_path and previous_page_path if the is
        # data on either next or previous page from the pagination

        if len(list) == number:
            next_page_path = base_path + str(page + 1) + end_path
        if page > 1:
            previous_page_path = base_path + str(page - 1) + end_path

        data = [dict(data=list)]
        data.append(dict(paging=dict(next=next_page_path,
                                     previous=previous_page_path)))

        return data
