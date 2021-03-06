def get_targets(pattern, urls, plugins=None, wordlist=None):
    """Generate scan targets"""

    targets = []
    
    if pattern == 'vuln':
        for url in urls:
            for plugin in plugins:
                targets.append({'url': url, 'plugin': plugin})
    else:
        with open(wordlist, 'r') as f:
            for sens in f:
                for url in urls:
                    targets.append({'url': url, 'sens': sens.strip()})
    
    return targets
