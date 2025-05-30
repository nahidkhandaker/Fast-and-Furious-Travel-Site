from .models import AppDetail, SocialMedia



def app_detail(request):
	this_app = AppDetail.objects.get(developed_by='Durjoy Acharya')
	socialmedias = SocialMedia.objects.filter(socialmedia_is_active='yes')

	context = {
		'this_app': this_app,
		'socialmedias': socialmedias
	}
	return context