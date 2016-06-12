Installing OLiMS with Odoo v9 on Windows

For those new to Odoo like myself I wanted to share how to install this module on Windows Odoo v9

After installing Odoo and logging in. Top right where it says Administrator, select the dropdown and click About. On About click 'Activate the Developer Mode'.

Under settings, give user Administrator Access Rights and Technical Features Permissions. Depending on your setup like if you had demo info installed you may need to set your group rights to inherit some features.

Rename olims-master to olims and place in C:\Program Files (x86)\Odoo9.0-version you installed\server\openerp\addons

Restart Odoo server 

Click Update Apps List on the left (ensure you are still in developer mode). OLiMS should appear. If not refresh your browser.
