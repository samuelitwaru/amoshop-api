from flask_login import LoginManager, current_user
# from flask_apscheduler import APScheduler
from app import app
from app.models import User


login_manager = LoginManager(app)
# scheduler = APScheduler()

login_manager.login_view = "index.login"
login_manager.login_message = "Login here."
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id, is_active=True).first()


# scheduler.add_job(id='Time sheet reminder', func=send_time_sheet_reminders, trigger="cron", day='25-31', hour=7, minute=0, second=0)
# scheduler.add_job(id='Scheduler task', func=send_action_mails, trigger='interval', seconds=60)
# scheduler.start()