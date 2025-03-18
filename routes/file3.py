from . import blueprint


@blueprint.route("/route3")
def route3():
    return "This is route 3"
