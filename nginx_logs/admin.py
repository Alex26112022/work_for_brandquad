from django.contrib import admin

from nginx_logs.models import ParseLogs


@admin.register(ParseLogs)
class ParseLogsAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address', 'date_log', 'method', 'uri', 'status_code', 'size')
    list_filter = ('method', 'status_code')
    search_fields = ('ip_address', 'method', 'status_code')
    list_display_links = (
        'ip_address', 'date_log', 'method', 'uri', 'status_code', 'size')
    fields = ('ip_address', 'date_log', 'method', 'uri', 'status_code', 'size')
