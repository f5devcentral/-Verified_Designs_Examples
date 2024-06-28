def extract_service_http_node_name(data):
    def find_service_http_node(node, parent_key=None):
        if isinstance(node, dict):
            if node.get('class') == 'Service_HTTP':
                return parent_key
            for key, value in node.items():
                result = find_service_http_node(value, key)
                if result:
                    return result
        elif isinstance(node, list):
            for item in node:
                result = find_service_http_node(item, parent_key)
                if result:
                    return result
        return None

    return find_service_http_node(data)

class FilterModule(object):
    def filters(self):
        return {
            'get_document_ids_map': self.get_document_ids_map
        }

    def get_document_ids_map(self, data, migrate_app_prefix):
        print(data)
        rValue = {}
        for request in data:
            migrate_vs_name = extract_service_http_node_name(request.item.json)
            document_id = request.json.id
            rValue[migrate_vs_name] = document_id

        return rValue
