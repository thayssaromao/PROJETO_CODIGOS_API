status_map = {
    200: "Autenticação bem-sucedida!",
    201: "Recurso criado com sucesso!",
    204: "Nenhum conteúdo retornado (requisição bem-sucedida).",
    400: "Requisição inválida! Verifique os dados enviados.",
    401: "Token inválido ou expirado!",
    403: "Sem permissão para acessar este recurso!",
    404: "Recurso não encontrado! Verifique a URL ou os parâmetros.",
    405: "Método não permitido! Verifique o método HTTP usado.",
    408: "Tempo de requisição esgotado (timeout).",
    429: "Muitas requisições! Aguarde antes de tentar novamente.",
    500: "Erro interno do servidor! Tente novamente mais tarde.",
    502: "Bad Gateway! Problema na comunicação entre servidores.",
    503: "Serviço indisponível! O servidor pode estar sobrecarregado.",
    504: "Gateway Timeout! O servidor não respondeu a tempo."
}