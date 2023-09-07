from datetime import datetime

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SheetReport

def convert_date(date_string, output_format='%Y-%m-%d'):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date_object.strftime(output_format)
    return formatted_date

@csrf_exempt
def save_pdf_to_model(request):
    if request.method == 'POST':
        pdf_content = request.POST.get('pdf_data')  # Assuming you send the PDF as a file.
        if pdf_content:
            recipient_list = 'srbc500@gmail.com'
            message = f"HELLO sanjay"
            subject = 'Your sheet Generated'
            from_email = 'info@sanjay.solutions'
            # Create an EmailMessage instance
            email = EmailMessage(subject, message, from_email, [recipient_list])
            email.attach("your_pdf_filename.pdf", pdf_content, 'application/pdf')  # Attach the PDF
            email.send()
            return JsonResponse({'success': True})


def get_top_bottom_sheet(request, query=''):
    if query == 'top':
        obj = SheetReport.objects.first()
    else:
        obj = SheetReport.objects.last()

    context = {
        'id': obj.id,
        'obj': obj,
    }
    return render(request, 'home_page.html', context)

def get_pre_and_next_sheet(request, id, query=''):
    if query == 'pre':
        try:
            obj = SheetReport.objects.filter(id__lt=id).order_by('-id')[0]
        except:
            obj = SheetReport.objects.get(id=id)

    else:
        try:
            obj = SheetReport.objects.filter(id__gt=id).order_by('id')[0]
        except:
            obj = SheetReport.objects.get(id=id)

    context = {
        'id': obj.id,
        'obj': obj,
    }
    return render(request, 'home_page.html', context)


def get_search_sheet(request):
    search = request.GET.get('search')
    context = {}
    try:
        obj = SheetReport.objects.get(job_no__exact=search)

        context['id'] = obj.id
        context['job_no'] = obj.job_no
        context['date'] = obj.date
        context['name'] = obj.name
        context['size'] = obj.size
        context['page'] = obj.page
        context['sheet1'] = obj.sheet1
        context['ink'] = obj.ink
        context['plates_qty'] = obj.plates_qty
        context['plates_rate'] = obj.plates_rate
        context['plates_amt'] = obj.plates_amt
        context['printing_qty'] = obj.printing_qty
        context['printing_rate'] = obj.printing_rate
        context['printing_amt'] = obj.printing_amt
        context['paper'] = obj.paper
        context['paper_amt'] = obj.paper_amt
        context['lamination'] = obj.lamination
        context['lamination_amt'] = obj.lamination_amt
        context['binding'] = obj.binding
        context['binding_amt'] = obj.binding_amt
        context['other_gst'] = obj.other_gst
        context['gst_amt'] = obj.gst_amt
        context['total_this_bill'] = obj.total_this_bill
        context['previous_bill'] = obj.previous_bill
        context['paid'] = obj.paid
        context['closing_bal'] = obj.closing_bal
        context['paper_rq_sheet'] = obj.paper_rq_sheet
        context['paper_rq_qty'] = obj.paper_rq_qty
        context['paper_rq_size'] = obj.paper_rq_size
        context['paper_rq_gsm'] = obj.paper_rq_gsm
        context['paper_rq_vendor'] = obj.paper_rq_vendor
        context['paper_rq_amt'] = obj.paper_rq_amt
        context['paper_rq_date'] = obj.paper_rq_date
        context['paper_rq_bank'] = obj.paper_rq_bank

    except Exception as e:
        print(e)

    return JsonResponse(context)


# Create your views here.
def home_page(request, id=0):
    if request.method == 'POST':
        form = request.POST
        job_no = form.get('job_no')
        date = form.get('date')
        date = convert_date(date)
        print(date,'===========================date')
        name = form.get('name')
        size = form.get('size')
        page = form.get('page')
        sheet1 = form.get('sheet1')
        ink = form.get('ink')
        plates_qty = form.get('plates_qty')
        plates_rate = form.get('plates_rate')
        plates_amt = form.get('plates_amt')
        printing_qty = form.get('printing_qty')
        printing_rate = form.get('printing_rate')
        printing_amt = form.get('printing_amt')
        paper = form.get('paper')
        paper_amt = form.get('paper_amt')
        lamination = form.get('lamination')
        lamination_amt = form.get('lamination_amt')
        binding = form.get('binding')
        binding_amt = form.get('binding_amt')
        other_gst = form.get('other_gst')
        gst_amt = form.get('gst_amt')
        total_this_bill = form.get('total_this_bill')
        previous_bill = form.get('previous_bill')
        paid = form.get('paid')
        closing_bal = form.get('closing_bal')

        paper_rq_sheet = form.get('paper_rq_sheet')
        paper_rq_qty = form.get('paper_rq_qty')
        paper_rq_size = form.get('paper_rq_size')
        paper_rq_gsm = form.get('paper_rq_gsm')
        paper_rq_vendor = form.get('paper_rq_vendor')
        paper_rq_amt = form.get('paper_rq_amt')
        paper_rq_date = form.get('paper_rq_date')
        paper_rq_bank = form.get('paper_rq_bank')

        if plates_qty:
            plates_qty = plates_qty
        else:
            plates_qty = 0
        if plates_rate:
            plates_rate = plates_rate
        else:
            plates_rate = 0
        if plates_amt:
            plates_amt = plates_amt
        else:
            plates_amt = 0
        if printing_qty:
            printing_qty = printing_qty
        else:
            printing_qty = 0
        if printing_rate:
            printing_rate = printing_rate
        else:
            printing_rate = 0
        if printing_amt:
            printing_amt = printing_amt
        else:
            printing_amt = 0
        if paper_amt:
            paper_amt = paper_amt
        else:
            paper_amt = 0
        if lamination_amt:
            lamination_amt = lamination_amt
        else:
            lamination_amt = 0
        if binding_amt:
            binding_amt = binding_amt
        else:
            binding_amt = 0
        if gst_amt:
            gst_amt = gst_amt
        else:
            gst_amt = 0
        if total_this_bill:
            total_this_bill = total_this_bill
        else:
            total_this_bill = 0
        if previous_bill:
            previous_bill = previous_bill
        else:
            previous_bill = 0
        if paid:
            paid = paid
        else:
            paid = 0
        if closing_bal:
            closing_bal = closing_bal
        else:
            closing_bal = 0

        if paper_rq_sheet:
            paper_rq_sheet = paper_rq_sheet
        else:
            paper_rq_sheet = ''
        if paper_rq_qty:
            paper_rq_qty = paper_rq_qty
        else:
            paper_rq_qty = 0
        if paper_rq_size:
            paper_rq_size = paper_rq_size
        else:
            paper_rq_size = ''
        if paper_rq_gsm:
            paper_rq_gsm = paper_rq_gsm
        else:
            paper_rq_gsm = ''
        if paper_rq_vendor:
            paper_rq_vendor = paper_rq_vendor
        else:
            paper_rq_vendor = ''
        if paper_rq_amt:
            paper_rq_amt = paper_rq_amt
        else:
            paper_rq_amt = 0
        if paper_rq_date:
            paper_rq_date = paper_rq_date
        else:
            paper_rq_date = ''
        if paper_rq_bank:
            paper_rq_bank = paper_rq_bank
        else:
            paper_rq_bank = ''

        if id == 0:
            sheet_obj = SheetReport.objects.create(job_no=datetime.now().strftime('%H%M%S'),
                                                   date=date,
                                                   name=name,
                                                   size=size,
                                                   page=page,
                                                   sheet1=sheet1,
                                                   ink=ink,
                                                   plates_qty=plates_qty,
                                                   plates_rate=plates_rate,
                                                   plates_amt=plates_amt,
                                                   printing_qty=printing_qty,
                                                   printing_rate=printing_rate,
                                                   printing_amt=printing_amt,
                                                   paper=paper,
                                                   paper_amt=paper_amt,
                                                   lamination=lamination,
                                                   lamination_amt=lamination_amt,
                                                   binding=binding,
                                                   binding_amt=binding_amt,
                                                   other_gst=other_gst,
                                                   gst_amt=gst_amt,
                                                   total_this_bill=total_this_bill,
                                                   previous_bill=previous_bill,
                                                   paid=paid,
                                                   closing_bal=closing_bal,

                                                   paper_rq_sheet=paper_rq_sheet,
                                                   paper_rq_qty=paper_rq_qty,
                                                   paper_rq_size=paper_rq_size,
                                                   paper_rq_gsm=paper_rq_gsm,
                                                   paper_rq_vendor=paper_rq_vendor,
                                                   paper_rq_amt=paper_rq_amt,
                                                   paper_rq_date=paper_rq_date,
                                                   paper_rq_bank=paper_rq_bank,
                                                   )
            id = sheet_obj.id
        else:
            sheet_obj = SheetReport.objects.filter(id=id).update(job_no=job_no,
                                                                 date=date,
                                                                 name=name,
                                                                 size=size,
                                                                 page=page,
                                                                 sheet1=sheet1,
                                                                 ink=ink,
                                                                 plates_qty=plates_qty,
                                                                 plates_rate=plates_rate,
                                                                 plates_amt=plates_amt,
                                                                 printing_qty=printing_qty,
                                                                 printing_rate=printing_rate,
                                                                 printing_amt=printing_amt,
                                                                 paper=paper,
                                                                 paper_amt=paper_amt,
                                                                 lamination=lamination,
                                                                 lamination_amt=lamination_amt,
                                                                 binding=binding,
                                                                 binding_amt=binding_amt,
                                                                 other_gst=other_gst,
                                                                 gst_amt=gst_amt,
                                                                 total_this_bill=total_this_bill,
                                                                 previous_bill=previous_bill,
                                                                 paid=paid,
                                                                 closing_bal=closing_bal,

                                                                 paper_rq_sheet=paper_rq_sheet,
                                                                 paper_rq_qty=paper_rq_qty,
                                                                 paper_rq_size=paper_rq_size,
                                                                 paper_rq_gsm=paper_rq_gsm,
                                                                 paper_rq_vendor=paper_rq_vendor,
                                                                 paper_rq_amt=paper_rq_amt,
                                                                 paper_rq_date=paper_rq_date,
                                                                 paper_rq_bank=paper_rq_bank,
                                                                 )

        if sheet_obj:
            context = {
                'id': id,
            }
            return JsonResponse(context)
    else:
        obj = ''
        if id != 0:
            obj = SheetReport.objects.get(id=id)
        context = {
            'id': id,
            'obj': obj,
        }
        return render(request, 'home_page.html', context)


def report(request):
    obj = SheetReport.objects.all()
    context = {
        'obj': obj,
    }
    return render(request, 'reports.html', context)
