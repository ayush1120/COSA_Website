# Documentation 





## Backend 

Basic Knowledge about Django Framework and Python is required.

Also I have used the following
* Django Class Based Views

Other than that following dependencies are utilized for the Project :
*  Croppie - Django  : A django extension to crop image on upload form according to
                                              required size.
                                                                * Docs - Croppie : [Croppie](https://foliotek.github.io/Croppie/)
                                                                * Docs - django-croppie : [Django Croppie](https://github.com/dima-kov/django-croppie) - You Can See Example Django Project



* **Libraries** : Make sure you have installed *pillow, argon2, bcrypt* libraries in order for project to run. Or install djangoEnv environment from djangoEnv.yml it has all the dependencies needed.

___



#### Django Apps List : 

* **first_app** :  As the name suggest its the first app contains models as Events, UserProfile, Announcement and other homepage related database tables.

  It has views for add events,  login, register, and to be continued.

* **Other Apps in this are gonna be on the name of club.**

___

#### Templates 

Templates will follow the following 

____
#### Plans

* CKEditor  : Going to use CK Editor To have RichTextField
    * Docs : [Django CKEditor](http://django-ckeditor.readthedocs.io/en/latest/)
    * Tutorial : [Django - CKEditor Tutorial](https://www.youtube.com/watch?v=L6y6cn1XUfw)

____
#### Notes / Later To-do

###### To do

1. Media files are not deleting even when a model instance is deleted. Fix It.
2. Search option for serving media and static files  as current method is not suited for deployment I guess.

###### Notes

* See backerr.md to know about errors and problems faced during development.