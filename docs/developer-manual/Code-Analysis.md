The purpose of this page is to provide some cursory documentation and overview as to the purpose of the various sections of the codebase to both speed up development and provide a better way for us to potentially facilitate migration to newer frameworks etc.

It will be incomplete for a time but will provide a way for us to increase documentation on the existing codebase.

**application** is where the majority of the code lives

- **auth** contains the FreeIPA adapter which allows sharing authentication with a LDAP server
- **cloud_storage** contains code used with the S3 hosting that was configured for the saas-dev branch

Analytics
**ListenerstatController.php** -
pulls in getDataAction which pulls the getDataPointsWithinRange

- **services**
  - CalendarService.php
    1. makeContextMenu - builds the menu for when you right click on a show in the calendar
    2.
