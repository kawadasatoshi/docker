from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'design', 'short_tips.urls', name='design'),
    host(r'shortcutkey', 'short_tips.urls', name='shortcutkey'),
    host(r'dialogue', 'short_tips.urls', name='dialogue'),
    host(r'wordeffect', 'short_tips.urls', name='wordeffect'),
    host(r'stock', 'short_tips.urls', name='stock'),
    host(r'shogi', 'short_tips.urls', name='shogi'),
    host(r'psy', 'short_tips.urls', name='psy'),
    host(r'examengcloud', "examengcloud.urls", name="examengcloud"),
    host(r'apologagent', "apologagent.urls", name="apologagent"),
    host(r'fanstatic', "fanstatic.urls", name="fanstatic"),
    host(r"techtweetrank", "engineer_rank.urls", name="engineer_rank"),
    host(r"techblog", "techblog.urls", name="techblog"),
    host(r"oversea-it", "oversea_it.urls", name="oversea-it"),
    host(r"question", "question.urls", name="question"),
    host(r"oreilly", "oreilly.urls", name="oreilly"),
    host(r'.*', 'short_tips.urls', name='else'),

)

