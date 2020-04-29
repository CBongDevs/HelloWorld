# We can't even declare something like this because `app` is not a global variable anywhere.
# Specifically the `app` we need is a local variable in `create_app`.

# @app.route('/bad_route')
# def bad_route():
#     return """
#     <!DOCTYPE html>
#     <head>
#     <title>Bad Route</title>
#     </head>
#     <body>
#     <h1>Bad Route</h1>
#     </body>
#     </html>
#     """