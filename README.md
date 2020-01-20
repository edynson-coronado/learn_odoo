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
│   ├── <module_name>.py
|   └── <inherited_module_name>.py
├── models
│   ├── __init__.py
│   └── first_main_model.py
│   └── another_main_model.py
│   └── inherit_model.py
├── report
│   ├── __init__.py
│   ├── <model>_report.py            (statistics reports with python)
│   ├── <model>_views.xml            (statistics reports SQL views)
│   ├── <model>_reports.xml          (printable reports: report actions, paperformat, ...)
│   └── <model>_templates.xml        (printable reports: xml report templates)
├── data
│   ├── __init__.py
│   ├── <model>_data.xml
│   └── <model>_demo.xml
├── views
│   ├── <module_name>_menus.xml     (optional definition of main menus)
│   ├── <model>_templates.xml       (import of JS / CSS)
│   ├── <model>_views.xml           (backend views)
│   └── assets.xml                  (portal templates)
└── security
    ├── ir.model.access.csv
    └── <model>_security.xml
```
**3. Scaffolding**

**4. Manifest**

**5. Models**

**6. Compute fields**

**7. Inheritance**

**8. Onchange**

**9. Constrains**

**10. Actions**

**11. Menus**

**12. Tree views**

**13. Form views**

**14. Search views**

**15. Calendar**

**16. Graph**

**17. Report**

**18. Controllers**

**19. Security**

**20. Tests**

## Cambios
**1. Modo desarrollador permanente**

**2. Bye api.one, api.multi**

**3. Bye account.invoice**

**4. View_type -> view_mode**

**5. Ocultar y mostrar campos en vista tree**

**6. Campos booleanos: “customer” y “supplier” quitados, reemplazados por campos ranqueados.**

**7. Campo “image” reemplazado por “image_1920”**

## Novedades
**1. Website_forum - perfil de usuario**

**2. Agregar videos al ecomerce - carrusel**

**3. Vista mapa en res.partner**

**4. Carga de js con lazy loading**

**5. jQuery v3**
