# edx-custom-registration-form
This custom registration form extension for Open edX adds two input fields to
the User Registration form: Phone Number and Country Code. Both fields are
required inputs.

## Installation
1. Install the module in the edx platform virtualenv: `pip install -e .`
2. Edit lms.env.json:
    1. Add a new line containing: `"REGISTRATION_EXTENSION_FORM": "reg_form_ext.forms.PhoneInfoForm",`
    2. Add a new line containing: `"ADDL_INSTALLED_APPS": ["reg_form_ext"],`
    3. Ensure combined login registration is set: `"ENABLE_COMBINED_LOGIN_REGISTRATION": true,`
    4. Save and exit editor.
3. Run migrations with `paver update_db`
4. Restart the LMS.


## Testing
Once installed, the tests can be run from the edx-platform directory with the
paver command:  
`paver test_system -s lms -t /edx/src/edx-custom-registration-form`


## Required Settings
```yaml
EDXAPP_FEATURES:
  ENABLE_COMBINED_LOGIN_REGISTRATION: true
EDXAPP_EXTRA_REQUIREMENTS:
  - name: edx-custom-registration-form
    version: 1.0
  - name: git+https://github.com/open-craft/edx-custom-registration-form.git
EDXAPP_ENV_EXTRA:
  REGISTRATION_EXTENSION_FORM: "reg_form_ext.forms.PhoneInfoForm"
EDXAPP_ENV_EXTRA:
  ADDL_INSTALLED_APPS:
    - reg_form_ext
```
