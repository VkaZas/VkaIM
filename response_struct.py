# reponseV = {
#     'message' : '',
#     'data' : {
#
#     },
#     'success' : True or False
# }


def build_resp(message, data, success):
    return {'message': message, 'data': data, 'success': success}