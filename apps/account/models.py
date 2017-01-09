from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    first_name = models.CharField(default='',blank=True,null=True,max_length=100)
    last_name = models.CharField(blank=True,null=True,max_length=100)
    email = models.EmailField(blank=True,null=True,max_length=100)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    about_me = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    # the user being followed
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # db_index will create a db index for the 'created_at' field
    # following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)
    # have to specify symmetrical=False, bc it is 'True' by default for M2MFields
    # manytomany from user to itself

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

# Add following field to User dynamically
# done to avoid altering 'User'
User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
