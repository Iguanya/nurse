app_name = "nurses"
app_title = "Nurses"
app_publisher = "George Mwangi"
app_description = "nurses"
app_email = "georgemwangim254@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nurses/css/nurses.css"
# app_include_js = "/assets/nurses/js/nurses.js"

# include js, css files in header of web template
web_include_css = [
    "/assets/nurses/css/style.css",
    "/assets/nurses/vendor/bootstrap/css/bootstrap.min.css",
    "/assets/nurses/vendor/bootstrap-icons/bootstrap-icons.css",
    "/assets/nurses/vendor/boxicons/css/boxicons.min.css",
    "/assets/nurses/vendor/glightbox/css/glightbox.min.css",
    "/assets/nurses/vendor/swiper/swiper-bundle.min.css",
]
web_include_js = [
    "/assets/nurses/js/main.js"
    "/assets/nurses/vendor/purecounter/purecounter_vanilla.js",
  	"/assets/nurses/vendor/bootstrap/js/bootstrap.bundle.min.js",
	"/assets/nurses/vendor/glightbox/js/glightbox.min.js",
 	"/assets/nurses/vendor/isotope-layout/isotope.pkgd.min.js",
  	"/assets/nurses/vendor/swiper/swiper-bundle.min.js",
  	"/assets/nurses/vendor/waypoints/noframework.waypoints.js",
  	"/assets/nurses/vendor/php-email-form/validate.js",

]
web_include_img = [
    "assets/nurses/img/about.jpg",
	"assets/nurses/img/hero-bg.png",
	"assets/nurses/img/team.jpg",
    "assets/nurses/img/testimonials/testimonials-1.jpg",
	"assets/nurses/img/testimonials/testimonials-2.jpg",
	"assets/nurses/img/testimonials/testimonials-3.jpg",
	"assets/nurses/img/testimonials/testimonials-4.jpg",
	"assets/nurses/img/testimonials/testimonials-5.jpg",
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nurses/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "nurses/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "nurses.utils.jinja_methods",
# 	"filters": "nurses.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "nurses.install.before_install"
# after_install = "nurses.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "nurses.uninstall.before_uninstall"
# after_uninstall = "nurses.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "nurses.utils.before_app_install"
# after_app_install = "nurses.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "nurses.utils.before_app_uninstall"
# after_app_uninstall = "nurses.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nurses.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nurses.tasks.all"
# 	],
# 	"daily": [
# 		"nurses.tasks.daily"
# 	],
# 	"hourly": [
# 		"nurses.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nurses.tasks.weekly"
# 	],
# 	"monthly": [
# 		"nurses.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "nurses.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nurses.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nurses.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["nurses.utils.before_request"]
# after_request = ["nurses.utils.after_request"]

# Job Events
# ----------
# before_job = ["nurses.utils.before_job"]
# after_job = ["nurses.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"nurses.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

