def check_value(string):
    if string == 'description':
        return "Atividades de Projeto e Reunião"
    if string == 'projeto':
        return "Desenvolvimento de Conteúdo"
    if string == 'tags':
        return "Reunião"
    if string == 'billable':
        return "false"
    if string == 'hora_inicio':
        return f"09:00:00"
    if string == 'hora_fim':
        return f"13:00:00"
    if string == 'data':
        from datetime import datetime
        import pytz
        tz = pytz.timezone("America/Sao_Paulo")
        return datetime.now(tz=tz).strftime("%Y-%m-%d")
