from django.utils.translation import ugettext_lazy as _

# Choices used in `market_state` field to inform
# about user's transaction type
MARKET_OPTIONS = {
    ('B', _('buy')),
    ('S', _('sell')),
}
