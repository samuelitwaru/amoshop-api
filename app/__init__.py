from flask import Flask, request
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api



app = Flask(__name__)


app.config.from_object(config.ProductionConfig)
app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


# load database models
from app.models import models

# load setup
from app.setup import *


# load api resources
from app.API.resources.product import ProductAPI, ProductListAPI, ProductQuantityAPI
from app.API.resources.sale import SaleAPI, SaleListAPI, SaleCheckoutAPI
from app.API.resources.stock import StockAPI, StockListAPI
from app.API.resources.user import UserAPI, UserListAPI, UserAuthAPI, UserUpdateAPI
from app.API.resources.sale_group import SaleGroupAPI, SaleGroupListAPI


api.add_resource(ProductListAPI, '/shop/api/v1.0/products', endpoint="products")
api.add_resource(ProductAPI, '/shop/api/v1.0/products/<int:id>', endpoint="product")
api.add_resource(ProductQuantityAPI, '/shop/api/v1.0/products/<int:id>/quantity', endpoint="product_quantity")

api.add_resource(SaleListAPI, '/shop/api/v1.0/sales', endpoint="sales")
api.add_resource(SaleAPI, '/shop/api/v1.0/sales/<int:id>', endpoint="sale")
api.add_resource(SaleCheckoutAPI, '/shop/api/v1.0/sales/checkout', endpoint="sale_checkout")

api.add_resource(StockListAPI, '/shop/api/v1.0/stock', endpoint="stock-list")
api.add_resource(StockAPI, '/shop/api/v1.0/stock/<int:id>', endpoint="stock")

api.add_resource(UserListAPI, '/shop/api/v1.0/users', endpoint="users")
api.add_resource(UserAPI, '/shop/api/v1.0/users/<int:id>', endpoint="user")
api.add_resource(UserAuthAPI, '/shop/api/v1.0/users/auth', endpoint="user_auth")
api.add_resource(UserUpdateAPI, '/shop/api/v1.0/users/<int:id>/update', endpoint="user_update")

api.add_resource(SaleGroupListAPI, '/shop/api/v1.0/sale-groups', endpoint="sale-groups")
api.add_resource(SaleGroupAPI, '/shop/api/v1.0/sale-groups/<int:id>', endpoint="sale-group")
