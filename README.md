<div align="center">
	<img src="https://raw.githubusercontent.com/edynsoncoronado/learn_odoo/master/src/images/edyodoo.jpg" alt="drawing" width="300"/>
	<img src="https://raw.githubusercontent.com/edynsoncoronado/learn_odoo/master/src/images/odoo.png"  alt="drawing" width="400"/><br>
</div
-----------------

# Learn Odoo

Course odoo by Edynson Coronado Icochea

* **Buenas prácticas**
* **Cambios**
* **Novedades**

## Buenas prácticas

**1. Actualización de módulos**
```bash
$ odoo -c odoo-server-comunity.conf -d <db_name> -u all
```

**2. Estructura del módulo**
- https://www.odoo.com/documentation/13.0/reference/guidelines.html#module-structure
```
my_module
├── __init__.py
├── __manifest__.py
├── controllers
│   ├── __init__.py
│   └── <module_name>.py
|   └── <inherited_module_name>.py
├── models
│   ├── __init__.py
│   └── first_main_model.py
│   └── another_main_model.py
│   └── inherit_model.py
├── report
│   ├── __init__.py
│   └── <model>_report.py            (statistics reports with python)
│   └── <model>_views.xml            (statistics reports SQL views)
│   └── <model>_reports.xml          (printable reports: report actions, paperformat, ...)
│   └── <model>_templates.xml        (printable reports: xml report templates)
├── data
│   ├── __init__.py
│   └── <model>_data.xml
│   └── <model>_demo.xml
├── views
│   ├── __init__.py
│   └── <module_name>_menus.xml     (optional definition of main menus)
│   └── <model>_templates.xml       (import of JS / CSS)
│   └── <model>_views.xml           (backend views)
│   └── assets.xml                  (portal templates)
├── security
│   └── ir.model.access.csv
│   └── <model>_security.xml
```
