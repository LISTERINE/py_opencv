from flask_assets import Bundle

common_css = Bundle(
        'css/thirdparty/bootstrap.min.css',
        output='bundle/css/common.css'
)

common_js = Bundle(
        'js/thirdparty/jquery-2.1.1.min.js',
        'js/thirdparty/bootstrap.min.js',
        'js/thirdparty/socket.io-1.4.5.js',
        output='bundle/js/common.js'
)

index_js = Bundle(
        'js/socket.js',
        output='bundle/js/index.js'
)
