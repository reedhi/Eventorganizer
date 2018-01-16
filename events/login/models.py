from django.db import models

class User (models.Model):
    password=models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    email=models.CharField(max_length=1000)
    contact_no = models.IntegerField()


    def __str__(self):
        return 'name : ' +str(self.name) + 'email :' + str(self.email) + 'contact_no :' + str(self.contact_no)

class Event(models.Model):
    event_name= models.CharField(max_length=300)
    admin= models.BooleanField(max_length=250)
    event_details=models.CharField(max_length=500)
    user_id=models.ForeignKey(User)
    createdDate = models.DateField()
    lastUpdetedDate = models.DateField()

    def __str__(self):
        return 'event_name : '+str(self.event_name) + 'admin : ' +str(self.admin) + 'event_details' + str(self.event_details) +'user_id : ' + str(self.user_id) + 'createDate : ' + str(self.createdDate) + ' lastUpdetedDate : ' + str(self.lastUpdetedDate)