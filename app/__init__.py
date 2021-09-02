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


# load template filters
from app import template_filters


# load api resources
from app.API.resources.product import ProductAPI, ProductListAPI, ProductQuantityAPI
from app.API.resources.sale import SaleAPI, SaleListAPI, SaleCheckoutAPI
from app.API.resources.stock import StockAPI, StockListAPI
from app.API.resources.category import CategoryAPI, CategoryListAPI
from app.API.resources.user import UserAPI, UserListAPI, UserAuthAPI, UserUpdateAPI
from app.API.resources.sale_group import SaleGroupAPI, SaleGroupListAPI

api_url = '/shop/api/v1.0'

api.add_resource(ProductListAPI, f'{api_url}/products', endpoint="products")
api.add_resource(ProductAPI, f'{api_url}/products/<int:id>', endpoint="product")
api.add_resource(ProductQuantityAPI, f'{api_url}/products/<int:id>/quantity', endpoint="product_quantity")

api.add_resource(SaleListAPI, f'{api_url}/sales', endpoint="sales")
api.add_resource(SaleAPI, f'{api_url}/sales/<int:id>', endpoint="sale")
api.add_resource(SaleCheckoutAPI, f'{api_url}/sales/checkout', endpoint="sale_checkout")

api.add_resource(StockListAPI, f'{api_url}/stock', endpoint="stock-list")
api.add_resource(StockAPI, f'{api_url}/stock/<int:id>', endpoint="stock")

api.add_resource(CategoryListAPI, f'{api_url}/categories', endpoint="category-list")
api.add_resource(CategoryAPI, f'{api_url}/categories/<int:id>', endpoint="category")

api.add_resource(UserListAPI, f'{api_url}/users', endpoint="users")
api.add_resource(UserAPI, f'{api_url}/users/<int:id>', endpoint="user")
api.add_resource(UserAuthAPI, f'{api_url}/users/auth', endpoint="user_auth")
api.add_resource(UserUpdateAPI, f'{api_url}/users/<int:id>/update', endpoint="user_update")

api.add_resource(SaleGroupListAPI, f'{api_url}/sale-groups', endpoint="sale-groups")
api.add_resource(SaleGroupAPI, f'{api_url}/sale-groups/<int:id>', endpoint="sale-group")


from app.routes.index import index_bp

app.register_blueprint(index_bp)
