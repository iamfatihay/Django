# Django Session Class-notes
# bir app olusturunca/ekleyince
    - installed app lere ekle
    -url de path ekle

# Token Authentication icin
    - Setting.py a ekle
    
        REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ]
    }
    