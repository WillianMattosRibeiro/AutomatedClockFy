def check_value(string):
    if string == 'description':
        return "Atividades de Projeto e Reunião"
    if string == 'project':
        return "Desenvolvimento de Conteúdo"
    if string == 'tags':
        return "Reunião"
    if string == 'billable':
        return "false"
    if string == 'start_hour':
        return f"09:00:00"
    if string == 'end_hour':
        return f"13:00:00"
    if string == 'date':
        from datetime import datetime
        import pytz
        tz = pytz.timezone("America/Sao_Paulo")
        return datetime.now(tz=tz).strftime("%Y-%m-%d")
