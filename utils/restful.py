from flask import jsonify

import json
from flask import jsonify  # 假设使用Flask框架，根据实际情况调整


class HttpStatusCode:
    """HTTP状态码常量类，定义API接口常用的响应状态码"""
    OK = 200  # 响应正常
    UNLOGIN_ERROR = 401  # 未登录错误
    PERMISSION_ERROR = 403  # 权限不足错误
    PARAM_ERROR = 400  # 客户端参数错误
    SERVER_ERROR = 500  # 服务器内部错误

    def _restful_response(self, code, message, data):
        """
        :param code: HTTP状态码
        :param message: 响应消息
        :param data: 响应数据
        :return: 包含响应内容和状态码的元组
        """
        return jsonify({
            "message": message or "",
            "data": data or {}
        }), code

    def success(self, message=None, data=None):
        """返回成功响应（200）"""
        return self._restful_response(code=self.OK, message=message, data=data)

    def unlogin_error(self, message="没有登入!"):
        """返回未登录错误响应（401）"""
        return self._restful_response(code=self.UNLOGIN_ERROR, message=message, data=None)

    def permission_error(self, message="没有权限访问!"):
        """返回权限不足错误响应（403）"""
        return self._restful_response(code=self.PERMISSION_ERROR, message=message, data=None)

    def param_error(self, message="参数错误!"):
        """返回参数错误响应（400）"""
        return self._restful_response(code=self.PARAM_ERROR, message=message, data=None)

    def server_error(self, message="服务器开小差!"):
        """返回服务器错误响应（500）"""
        return self._restful_response(code=self.SERVER_ERROR, message=message or "服务器内部错误", data=None)


response = HttpStatusCode()
