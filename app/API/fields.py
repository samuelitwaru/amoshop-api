from flask_restful import fields


class Fields:

	def timestampedmodel_fields(self):
		return { 
		}

	def timestampedmodel_fields_min(self):
		return { 
		}

	def product_fields(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
			"brand": fields.String,
			"description": fields.String,
			"barcode": fields.String,
			"quantity": fields.Integer,
			"units": fields.String,
			"buying_price": fields.Integer,
			"selling_price": fields.Integer,
			"stock": fields.Nested(self.stock_fields_min()),
			"sales": fields.Nested(self.sale_fields_min()),
			"categories": fields.Nested(self.category_fields_min())
		}

	def product_fields_min(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
			"brand": fields.String,
			"description": fields.String,
			"barcode": fields.String,
			"quantity": fields.Integer,
			"units": fields.String,
			"buying_price": fields.Integer,
			"selling_price": fields.Integer,
		}

	def category_fields(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
		}

	def category_fields_min(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
		}

	def stock_fields(self):
		return { 
			"id": fields.Integer,
			"quantity": fields.Integer,
			"product": fields.Nested(self.product_fields_min()),
		}

	def stock_fields_min(self):
		return { 
			"id": fields.Integer,
			"quantity": fields.Integer,
		}

	def sale_fields(self):
		return { 
			"id": fields.Integer,
			"created_at": fields.String,
			"quantity": fields.Integer,
			"buying_price": fields.Integer,
			"selling_price": fields.Integer,
			"product": fields.Nested(self.product_fields_min()),
			"sale_group": fields.Nested(self.sale_group_fields_min()),
			"session": fields.Nested(self.session_fields_min()),
		}

	def sale_fields_min(self):
		return {
			"id": fields.Integer,
			"created_at": fields.String,
			"quantity": fields.Integer,
			"buying_price": fields.Integer,
			"selling_price": fields.Integer,
		    "product": fields.Nested(self.product_fields_min()),
		}

	def sale_group_fields(self):
		return { 
			"id": fields.Integer,
			"created_at": fields.String,
			"amount": fields.Integer,
		    "paid": fields.Integer,
			"user": fields.Nested(self.user_fields()),
		    "sales": fields.Nested(self.sale_fields_min()),
		}

	def sale_group_fields_min(self):
		return { 
			"id": fields.Integer,
			"amount": fields.Integer,
		    "paid": fields.Integer,
		}

	def session_fields(self):
		return {
			"id": fields.Integer,
		    "start_time": fields.String,
		    "stop_time": fields.String,
		    "user": fields.Nested(self.user_fields_min()),
		    "sales": fields.Nested(self.sale_fields_min()),
		}

	def session_fields_min(self):
		return {
			"id": fields.Integer,
		    "start_time": fields.String,
		    "stop_time": fields.String,
		}

	def user_fields(self):
		return { 
			"id": fields.Integer,
			"username": fields.String,
			# "password": fields.String,
			# "recovery_password": fields.String,
			"is_active": fields.Boolean,
			"token": fields.String,
			"profile": fields.Nested(self.profile_fields_min()),
			"sessions": fields.Nested(self.session_fields_min()),
			"roles": fields.List(fields.String),
		}

	def user_fields_min(self):
		return { 
			"id": fields.Integer,
			# "username": fields.String,
			# "password": fields.String,
			"recovery_password": fields.String,
			"is_active": fields.Boolean,
		}



	def profile_fields(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
			"email": fields.String,
			"telephone": fields.String,
			"user": fields.Nested(self.user_fields_min()),
		}

	def profile_fields_min(self):
		return { 
			"id": fields.Integer,
			"name": fields.String,
			"email": fields.String,
			"telephone": fields.String,
		}


