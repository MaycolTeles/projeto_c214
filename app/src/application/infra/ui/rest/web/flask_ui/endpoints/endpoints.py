"""
Module containing all the endpoints for the Flask application.
"""

from typing import Optional

from src.application.adapters.controllers.rest.web import WebController

from flask import Response, jsonify, request


def index():
    """
    Function to render the index page.
    """
    return Response("Hello, World!")


def comprovante_residencia(comprovante_residencia_id: Optional[int] = None):
    """
    Function to return the network traffic data.
    """
    params = {"id": comprovante_residencia_id-1 if comprovante_residencia_id else None}
    controller = WebController()

    if request.method == "POST":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        params["comprovante_type"] = request.form["comprovante_type"]
        response = controller.create_comprovante_residencia(params)

    elif request.method == "GET":
        if comprovante_residencia_id:
            response = controller.read_comprovante_residencia(params)

        else:
            response = controller.read_all_comprovante_residencia(params)

    elif request.method == "PUT":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        params["comprovante_type"] = request.form["comprovante_type"]
        response = controller.update_comprovante_residencia(params)

    elif request.method == "DELETE":
        response = controller.delete_comprovante_residencia(params)

    return jsonify(response)


def rg(rg_id: Optional[int] = None):
    """
    TODO
    """
    params = {"id": rg_id-1 if rg_id else None}
    controller = WebController()

    if request.method == "POST":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        response = controller.create_rg(params)

    elif request.method == "GET":        
        if rg_id:
            response = controller.read_rg(params)

        else:
            response = controller.read_all_rg(params)

    elif request.method == "PUT":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        response = controller.update_rg(params)

    elif request.method == "DELETE":
        response = controller.delete_rg(params)

    return jsonify(response)


def cpf(cpf_id: Optional[int] = None):
    """
    TODO
    """
    params = {"id": cpf_id-1 if cpf_id else None}
    controller = WebController()

    if request.method == "POST":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        response = controller.create_cpf(params)

    elif request.method == "GET":
        if cpf_id:
            response = controller.read_cpf(params)

        else:
            response = controller.read_all_cpf(params)

    elif request.method == "PUT":
        params["value"] = request.form["value"]
        params["date"] = request.form["date"]
        response = controller.update_cpf(params)

    elif request.method == "DELETE":
        response = controller.delete_cpf(params)

    return jsonify(response)