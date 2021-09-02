from app import app, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask_login import UserMixin, current_user
from flask_sqlalchemy import Model
from sqlalchemy import Column, DateTime, desc


class TimestampedModel(Model):
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime)


product_categories = db.Table('product_categories',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)


class Product(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    barcode = db.Column(db.String, unique=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    units = db.Column(db.String, nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    stock = db.relationship("Stock", backref="product")
    sales = db.relationship("Sale", backref="product")
    categories = db.relationship('Category', cascade="all,delete", secondary=product_categories, lazy='subquery', backref=db.backref('products', lazy=True))

	
class Category(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)


class Stock(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))


class Sale(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    sale_group_id = db.Column(db.Integer, db.ForeignKey("sale_group.id"))


class SaleGroup(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    sales = db.relationship("Sale", backref="sale")


user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    recovery_password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=False)
    token = db.Column(db.String)
    profile = db.relationship('Profile', backref='user', uselist=False, foreign_keys="[Profile.user_id]", cascade="all,delete")
    roles = db.relationship('Role', secondary=user_roles, lazy='subquery', backref=db.backref('users', lazy=True))
    sale_groups = db.relationship("SaleGroup", backref="user", lazy='dynamic')

    def __init__(self, *args, **kwargs):
        self.email = kwargs.get("email")
        self.username = kwargs.get("username")
        self.is_active = kwargs.get("is_active")
        password = kwargs.get("password")
        if password:
            self.set_password(password)

    def __str__(self):
        return self.profile.name

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data["id"])
        return user

    @property
    def role_names(self):
        return [role.name for role in self.roles]

    def set_roles(self, roles):
        for name in roles:
            role = Role.query.filter_by(name=name).first()
            if role:
                self.roles.append(role)
        db.session.commit()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(64), nullable=False, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Profile(db.Model, TimestampedModel):
    id = db.Column(db.Integer, primary_key=True)     
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    telephone = db.Column(db.String(16))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))

    def __str__(self):
        return self.name