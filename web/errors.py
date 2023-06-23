from model.dto.error import Error


not_found_err = Error(code=400, name='Error',
                      description='Bad Request')

internal_err = Error(code=500, name='Error',
                     description='Internal Server Error')
