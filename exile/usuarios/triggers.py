from trigger import default
from smtp.plugins import TriggerSMTPPlugin
import models


class T1(default.Trigger):
    events = {'save': 'all'}
    model = models.Empleado

# end class

class SMTP1(TriggerSMTPPlugin):
    emails = ['luismiguel.mopa@gmail.com']
    messages = {
        'save': {
            'html': ''
        }
    }

    def get_subject(self, event, instance):
         return "instance.subject"
    # end def

    def get_html(self, html, instance):
        return "instance.message"
    # end def

    def get_emails(self, event, instance):
         return [self.emails, instance.email]
    # end def
# end class


default.triggers.register(T1, [SMTP1])