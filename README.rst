|BuildStatus|

Small Django APP for managing Bitbucket or Github webhooks

Tested on Python 2.7 and 3.4, with Django 1.7 and 1.8. The minimum
version of Django that covers this APP is 1.7, there began the
maintenance of ``JsonResponse``

How to Install
--------------

1. ``pip install django-bitbucket-hook``
2. Add ``django_bitbucket_hook`` to ``INSTALLED_APPS`` in your
   ``settings.py``
3. Run ``./manage.py migrate``
4. Add ``url(r'^hook/', include('django_bitbucket_hook.urls'))``
5. In the admin panel you will find fields for Hook
6. Fields

-  Name - The name of the hook
-  User - User created repository ( Example:
   https://github.com/Kras4ooo/django-bitbucket-hook/ -> ``Kras4ooo`` )
-  Repo - The name of the repo ( Example:
   https://github.com/Kras4ooo/django-bitbucket-hook/ ->
   ``django-bitbucket-hook`` )
-  Path - Full path to the script to be executed ( Example:
   ``/home/test/test-repo/execute-script.sh`` )
-  Branch - Which branch to be monitored ( Example: ``dev``, ``master``,
   ``test``, ``stage`` ...etc )

7. Go to set up your Webhook
8. If everything is okay you will get the following response in Webhook
   (``{'success': True}``)
9. Examples URLS

-  http[s]://domain/hook -> Gets the Hook that corresponds to the user
   name, and repo name
-  http[s]://domain/hook/name -> Gets the hook that fits the following
   name
-  http[s]://domain/hook/name/branch -> Gets the Hook which has the same
   name and branch of the repository

.. |BuildStatus| image:: https://travis-ci.org/Kras4ooo/django-bitbucket-hook.svg?branch=master
   :target: https://travis-ci.org/Kras4ooo/django-bitbucket-hook
