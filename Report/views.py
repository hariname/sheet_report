import io
from datetime import datetime
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SheetReport, LookUp
import io
from django.http import HttpResponse
from django.db.models import Q
from xlsxwriter.workbook import Workbook

@csrf_exempt
def save_pdf_to_model(request):
    if request.method == 'POST':
        pdf_content = request.FILES.get('pdf_file')
        if pdf_content:
            recipient_list = ['srbc500@gmail.com']  # Use a list for recipient emails
            message = "HELLO sanjay"
            subject = 'Your sheet Generated'
            from_email = 'info@sanjay.solutions'

            # Create an EmailMessage instance
            email = EmailMessage(subject, message, from_email, recipient_list)

            # Attach the PDF
            email.attach("your_pdf_filename.pdf", pdf_content.read(), 'application/pdf')

            try:
                email.send()
                return JsonResponse({'success': True})
            except Exception as e:
                # Handle any exceptions that may occur during email sending
                return JsonResponse({'success': False, 'error_message': str(e)})
        else:
            return JsonResponse({'success': False, 'error_message': 'PDF data not provided in the request.'})


def get_top_bottom_sheet(request, query=''):
    obj = ''
    id = 0
    try:
        if query == 'top':
            obj = SheetReport.objects.first()
            id = obj.id
        else:
            obj = SheetReport.objects.last()
            id = obj.id
    except:
        pass

    context = {
        'id': id,
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
        header_date = obj.header_date
        header_date = datetime.strftime(header_date, '%d/%m/%Y')

        paper_rq_date = obj.paper_rq_date
        paper_rq_date = datetime.strftime(paper_rq_date, '%d/%m/%Y')

        context['id'] = obj.id
        context['job_no'] = obj.job_no
        context['date'] = header_date
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
        context['paper_rq_date'] = paper_rq_date
        context['paper_rq_bank'] = obj.paper_rq_bank

    except Exception as e:
        print(e)

    return JsonResponse(context)


# Create your views here.
def home_page(request, id=0):
    try:
        obj_count = SheetReport.objects.last()
        job_no = int(obj_count.job_no) + 1
    except:
        job_no = ''

    if request.method == 'POST':
        form = request.POST
        head_job_no = form.get('job_no')
        header_date = form.get('date')
        header_date = datetime.strptime(header_date, '%d/%m/%Y')
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
        paper_rq_date = datetime.strptime(paper_rq_date, '%d/%m/%Y')
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

        if paper_rq_bank:
            paper_rq_bank = paper_rq_bank
        else:
            paper_rq_bank = ''

        if id == 0:
            job_no = int(head_job_no)

            sheet_obj = SheetReport.objects.create(job_no=job_no,
                                                   header_date=header_date,
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
                                                   closing_bal=int(previous_bill)+int(total_this_bill)-int(paid),
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
            msg = 'Sheet Created'
        else:
            sheet_obj = SheetReport.objects.filter(id=id).update(header_date=header_date,
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
                                                                 closing_bal=int(previous_bill)+int(total_this_bill)-int(paid),
                                                                 paper_rq_sheet=paper_rq_sheet,
                                                                 paper_rq_qty=paper_rq_qty,
                                                                 paper_rq_size=paper_rq_size,
                                                                 paper_rq_gsm=paper_rq_gsm,
                                                                 paper_rq_vendor=paper_rq_vendor,
                                                                 paper_rq_amt=paper_rq_amt,
                                                                 paper_rq_date=paper_rq_date,
                                                                 paper_rq_bank=paper_rq_bank,
                                                                 )
            msg = 'Sheet Updated'

        if sheet_obj:
            context = {
                'id': id,
                'msg': msg,
            }
            return JsonResponse(context)
    else:
        try:
            loader = LookUp.objects.get(title='loader')
        except:
            loader = ''

        closing = ''
        obj = ''
        try:
            if id != 0:
                obj = SheetReport.objects.get(id=id)
        except:
            obj = ''
        try:
            closing = SheetReport.objects.last()
            closing = closing.closing_bal
        except:
            closing = ''
        context = {
            'id': id,
            'obj': obj,
            'closing': closing,
            'job_no': job_no,
            'loader': loader,
        }
        return render(request, 'home_page.html', context)


def report(request):
    obj = SheetReport.objects.all().order_by('-id')
    context = {
        'obj': obj,
    }
    return render(request, 'reports.html', context)


def export_history(request, fromD, toD, search):
    output = io.BytesIO()
    workbook = Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet('sheet')

    header_format = workbook.add_format({
        'border': 1,
        'bg_color': '#C6EFCE',
        'bold': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'indent': 1,
    })

    headings = ['Job No', 'Date', 'Name', 'Plates', 'Printing', 'Paper', 'Lamination', 'Binding', 'Other / Gst', 'Total', 'Paid', 'Closing']
    for col_num, heading in enumerate(headings):
        worksheet.write(0, col_num, heading, header_format)

    unlocked_format = workbook.add_format({'locked': False})
    worksheet.set_column('A:A', 15, unlocked_format)
    worksheet.set_column('B:B', 15, unlocked_format)
    worksheet.set_column('C:C', 25, unlocked_format)
    worksheet.set_column('D:D', 25, unlocked_format)
    worksheet.set_column('E:E', 25, unlocked_format)
    worksheet.set_column('F:F', 25, unlocked_format)
    worksheet.set_column('G:G', 25, unlocked_format)
    worksheet.set_column('H:H', 25, unlocked_format)
    worksheet.set_column('I:I', 25, unlocked_format)

    pro_data = SheetReport.objects.all()  # Default queryset

    # if fromD != 'None':
    #     pro_data = pro_data.filter(header_date=fromD)

    if fromD != 'None' and toD != 'None':
        pro_data = pro_data.filter(Q(header_date__gte=toD) & Q(header_date__lte=toD))

    if search != 'None':
        pro_data = pro_data.filter(Q(job_no__iexact=search) | Q(name__iexact=search))

    rows = []
    for obj in pro_data:
        job_no = obj.job_no
        header_date = obj.header_date.strftime("%Y-%m-%d")
        name = obj.name
        plates_amt = obj.plates_amt
        printing_amt = obj.printing_amt
        paper_amt = obj.paper_amt
        lamination_amt = obj.lamination_amt
        binding_amt = obj.binding_amt
        gst_amt = obj.gst_amt
        total_this_bill = obj.total_this_bill
        paid = obj.paid
        closing_bal = obj.closing_bal

        rows.append([job_no, header_date, name, plates_amt, printing_amt, paper_amt, lamination_amt, binding_amt, gst_amt, total_this_bill, paid, closing_bal])

    for row_num, row_data in enumerate(rows, start=1):
        for col_num, cell_data in enumerate(row_data):
            worksheet.write(row_num, col_num, cell_data, unlocked_format)

    workbook.close()

    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = "attachment; filename=Sheet_Report.xlsx"

    return response
