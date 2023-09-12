from .models import CompanyInfo





def get_company_info(request):
	info = CompanyInfo.objects.last()

	return {"company_info":info}



