from flask import jsonify


def Response(status: bool, restProps):
    if type(restProps) is list:
        return jsonify({
            'status': status,
            **restProps
        })
    else:
        return jsonify({
            'status': status,
            'message': restProps
        })
