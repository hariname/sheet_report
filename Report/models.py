from django.db import models


class SheetReport(models.Model):
    job_no = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

    size = models.CharField(max_length=50)
    page = models.CharField(max_length=50)
    sheet1 = models.CharField(max_length=50)
    ink = models.CharField(max_length=50)

    plates_qty = models.IntegerField(default=0, null=True, blank=True)
    plates_rate = models.IntegerField(default=0, null=True, blank=True)
    plates_amt = models.IntegerField(default=0, null=True, blank=True)

    printing_qty = models.IntegerField(default=0, null=True, blank=True)
    printing_rate = models.IntegerField(default=0, null=True, blank=True)
    printing_amt = models.IntegerField(default=0, null=True, blank=True)

    paper = models.CharField(max_length=50)
    paper_amt = models.IntegerField(default=0, null=True, blank=True)

    lamination = models.CharField(max_length=50)
    lamination_amt = models.IntegerField(default=0, null=True, blank=True)

    binding = models.CharField(max_length=50)
    binding_amt = models.IntegerField(default=0, null=True, blank=True)

    other_gst = models.CharField(max_length=50)
    gst_amt = models.IntegerField(default=0, null=True, blank=True)

    total_this_bill = models.BigIntegerField(default=0, null=True, blank=True)
    previous_bill = models.BigIntegerField(default=0, null=True, blank=True)
    paid = models.BigIntegerField(default=0, null=True, blank=True)
    closing_bal = models.BigIntegerField(default=0, null=True, blank=True)

    paper_rq_sheet = models.CharField(max_length=50, null=True, blank=True)
    paper_rq_qty = models.IntegerField(null=True, default=0, blank=True)
    paper_rq_size = models.CharField(max_length=50, null=True, blank=True)
    paper_rq_gsm = models.CharField(max_length=50, null=True, blank=True)
    paper_rq_vendor = models.CharField(max_length=50, null=True, blank=True)
    paper_rq_amt = models.IntegerField(default=0, null=True, blank=True)
    paper_rq_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    paper_rq_bank = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.job_no

    class Meta:
        db_table = 'sheet_report'
