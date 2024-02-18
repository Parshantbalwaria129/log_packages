import logging
import traceback
import sys


@staticmethod
def wrap_method_with_error_handling(method):
    def wrapper(*args, **kwargs):
        try:
            result = method(*args, **kwargs)
            # logging.info(
            #     f"Method '{method.__name__}' executed successfully")
            return result
        except Exception as e:
            _, _, tb = sys.exc_info()
            tb_info = traceback.extract_tb(tb)
            user_traceback = '\n'.join(traceback.format_list(tb_info[1:]))
            # user_traceback = traceback.format_exc()
            logging.error(
                f"An exception occurred in method '{method.__name__}': {e}\n {user_traceback}")
            print("==========================================================================")
            return type(e)
    return wrapper
    
def log_error(target):
    # Check if the target is a class and enable error logging for its methods
    if isinstance(target, type):
            for name, method in vars(target).items():
                if callable(method):
                    if not hasattr(method, '_wrap_method_with_error_handling'):
                        setattr(target, name, wrap_method_with_error_handling(method))
                        method._wrap_method_with_error_handling = True
            return target
    elif callable(target):
        # check if target is a callable method
        if not hasattr(target, '_wrap_method_with_error_handling'):
            setattr(target, target.__name__, wrap_method_with_error_handling(target))
            target._wrap_method_with_error_handling = True
        return target
    else:
        return target

