from django.db.models import signals
from django.utils.translation import ugettext_noop as _

try:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        try:
            notification.create_notice_type("friend_request", _("Friendship requested"), _("Somebody requested your friendship."), default=1)
            notification.create_notice_type("friend_request_accepted", _("Friendship accepted"), _("Somebody accepted your friendship request."), default=1)
        except:
            pass

    signals.post_syncdb.connect(create_notice_types, sender=notification)
except ImportError:
    print "Skipping creation of NoticeTypes as notification app not found"
