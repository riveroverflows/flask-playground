from . import blueprint


@blueprint.route("/route2")
def route2():
    return "This is route 2"
