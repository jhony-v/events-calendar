from flask import jsonify


def Response(status: bool, restProps):
    if type(restProps) is list or type(restProps) is dict:
        return jsonify({
            'status': status,
            'data': restProps
        })
    else:
        return jsonify({
            'status': status,
            'message': restProps
        })
