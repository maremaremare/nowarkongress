from moderation import moderation
from moderation.moderator import GenericModerator
from .models import ContentItem, OuterParticipant
from threadedcomments.models import ThreadedComment
from moderation.message_backends import StandartMessageBackend


class ContentModerator(GenericModerator):
    manager_names = ['objects', 'itms', 'items']
    notify_user = False
    auto_approve_for_superusers = True
    auto_approve_for_staff = True
    message_backend_class = StandartMessageBackend
    notify_moderator = False
    auto_approve_for_authenticated = False
    bypass_moderation_after_approval = True
    #bypass_moderation_after_approval = True
    #visibility_column = 'visible'

class CommentModerator(GenericModerator):
    notify_user = False
    auto_approve_for_superusers = True
    auto_approve_for_authenticated = True


class SignatureModerator(GenericModerator):
    notify_user = False
    auto_approve_for_superusers = True
    auto_approve_for_authenticated = True
   

moderation.register(ContentItem, ContentModerator)
moderation.register(ThreadedComment, CommentModerator)
#moderation.register(OuterParticipant, SignatureModerator)

