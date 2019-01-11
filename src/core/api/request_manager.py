from src.core.api.request_handler import RequestHandler
from src.utils.config_handler import ConfigHandler


class RequestManager:
    __instance = None

    @staticmethod
    def get_instance():
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestHandler()
            RequestManager.__instance.session.headers.update(
                {"X-Requested-With": "XMLHttpRequest",
                 "Content-Type": "application/json",
                 "Cookie" : ConfigHandler.get_config().get_cookie(),
                 "X-CSRF-Token" : ConfigHandler.get_config().get_XCSRFToken()
                 })




        return RequestManager.__instance
