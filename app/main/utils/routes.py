from django.urls import get_resolver


def getRoutes():
    urlconf = get_resolver()
    routes = extractRoutes(urlconf.url_patterns)

    return routes

    

def extractRoutes(url_patterns, prefix=""):
    routes = []
    for pattern in url_patterns:
        if hasattr(pattern, "url_patterns"):
            routes += extractRoutes(pattern.url_patterns, prefix + str(pattern.pattern))
        else:
            routes.append({
                "pattern": prefix + str(pattern.pattern),
                "name": pattern.name
            })
    return routes