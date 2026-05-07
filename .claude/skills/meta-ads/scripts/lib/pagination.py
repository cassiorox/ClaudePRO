#!/usr/bin/env python3
"""
Helpers de paginacao para a Meta Ads API.
"""

import json
import sys


def collect_cursor(cursor, limit=None):
    """
    Coleta resultados de um Cursor do SDK, respeitando o limite.
    O Cursor do SDK faz auto-paginacao quando iterado.

    Args:
        cursor: Cursor do SDK (retornado por get_xxx() methods)
        limit: Numero maximo de resultados (None = todos)

    Returns:
        Lista de dicts serializados
    """
    results = []
    count = 0
    for item in cursor:
        if hasattr(item, 'export_all_data'):
            results.append(item.export_all_data())
        else:
            results.append(item)
        count += 1
        if limit and count >= limit:
            break
    return results


def paginate_edge(parent_obj, edge_method, fields=None, params=None, limit=25):
    """
    Busca resultados de uma edge do SDK com paginacao.

    Args:
        parent_obj: Objeto pai (ex: AdAccount, Campaign)
        edge_method: Nome do metodo de edge (ex: 'get_campaigns')
        fields: Lista de campos
        params: Dict de parametros extras

    Returns:
        Dict com 'data' e 'paging' (cursors)
    """
    method = getattr(parent_obj, edge_method)

    call_params = params or {}
    if limit:
        call_params['limit'] = limit

    call_fields = fields or []

    cursor = method(fields=call_fields, params=call_params)

    results = []
    for item in cursor:
        if hasattr(item, 'export_all_data'):
            results.append(item.export_all_data())
        else:
            results.append(item)
        if len(results) >= limit:
            break

    # Build response with paging info
    response = {"data": results}

    # Extract paging cursors if available
    if hasattr(cursor, 'paging') and cursor.paging:
        response["paging"] = cursor.paging
    elif hasattr(cursor, '_paging'):
        response["paging"] = cursor._paging

    return response


def fetch_url(url):
    """
    Busca uma URL de paginacao diretamente (next/previous page).
    Util quando o usuario tem a URL completa de paginacao.
    """
    import requests
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"ERRO ao buscar URL de paginacao: {e}", file=sys.stderr)
        sys.exit(1)
