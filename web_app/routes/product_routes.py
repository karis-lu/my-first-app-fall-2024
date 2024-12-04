# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash
from app.product import fetch_product_json

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products")
def products_list():
    print("PRODUCTS...")

    try:
        products = fetch_product_json()

        flash("Fetched Latest Product Data!", "success")
        
        return render_template("products.html", products=products)
    except Exception as err:
        print('OOPS', err)

        flash("Product Data Error. Please try again!", "danger")
        return redirect("/")
    

#
# API ROUTES
#

@product_routes.route("/api/product.json")
def unemployment_api():
    print("DRINK DATA (API)...")

    try:
        data = fetch_product_json()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Unemployment Data Error. Please try again."}, 404