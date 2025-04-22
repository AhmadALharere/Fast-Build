from django.db import models

# Create your models here.
#app name: noticeBoard
notice_type = (
    
    ("perment","perment"),
    ("descount","descount"),
    ("offer","offer"),
    ("update annuncement","update annuncement")
    )


class Notice(models.Model):
    
    id = models.AutoField(primary_key=True)
    type = models.CharField(default="perment",choices=notice_type, max_length=50)
    title = models.CharField(default="perment!!!", max_length=50)
    description = models.TextField()
    descount = models.ForeignKey("home.Descount", on_delete=models.CASCADE,null=True,blank=True) 
    #should return error wherever user enter the type "descount" and this field is null
    
    offer = models.ForeignKey("home.Offer", on_delete=models.CASCADE,null=True,blank=True)
    #should return error wherever user enter the type "offer" and this field is null
    
    def __str__(self):
        return self.title
    
    
    