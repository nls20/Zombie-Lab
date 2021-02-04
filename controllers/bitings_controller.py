from flask import Blueprint, Flask, redirect, render_template, request
from models.biting import Biting
import repositories.biting_repository as biting_repository
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings=bitings)

# NEW
@bitings_blueprint.route("/bitings/new", methods=['GET'])
def new_biting():
    humans = human_repository.select(all)
    zombies = zombie_repository.select(all)
    return render_template("/bitings/new.html", humans = humans, zombies = zombies)


# CREATE

# EDIT

# UPDATE

# DELETE
