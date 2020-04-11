'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''


from django.urls import path
from . import views


urlpatterns = [

   path('',views.Index,name='index_page'),
   path('image',views.take_images,name="images"),
   path('detect',views.Detect,name="detection"),
   path('chest_scan',views.chest_scan,name='chest_scan'),
   # path('random',views.random,name='random'),

]
