import sys


def error_message_details(error,error_detail:sys):
    # Whenever we execute a python code and if it fails. The Sys module will push the error message to this function
    _, _, exc_tb = error_detail.exc_info() 

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Occured python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class AppException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message









