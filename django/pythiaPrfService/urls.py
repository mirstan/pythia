"""
URLs for interacting with the Pythia PRF service.
"""

from django.conf.urls import include, url
import views

urlpatterns = [
	url(r'^eval$', views.eval),

	# Client key rotation
	# url(r'^update-request$', views.updateRequest),
	# url(r'^update-begin$', views.updateBegin),
	# url(r'^update-complete$', views.updateComplete),
]