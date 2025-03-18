from . import blueprint


@blueprint.route("/route1")
def route1():
    return "This is route 1"
