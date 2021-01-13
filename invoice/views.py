from django.shortcuts import render

from django.views.generic import View


# dependies for render_to_pdf function


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

# writing render_to_pdf function


def render_to_pdf(template_source, context_dict={}):

    template = get_template(template_source)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Create your views here.


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):

        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 2725,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:

            return pdf

        # return HttpResponse(pdf, content_type='application/pdf') or
        return HttpResponse("Not Found")


def print(request):
    return render(request, 'invoice.html', {})
