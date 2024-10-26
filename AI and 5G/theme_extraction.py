# Define keywords for each document
documents_keywords = {
    "GPAI.txt": [
        'global', 'partnership', 'artificial', 'intelligence', 'gpai', 'multilateral', 
        'initiative', 'aimed', 'supporting', 'responsible', 'development', 'adoption', 
        'use', 'ai', 'technologies', 'grounded', 'human', 'rights', 'inclusion', 'diversity', 
        'innovation', 'economic', 'growth', 'launched', 'june', '2020', 'provides', 
        'platform', 'governments', 'international', 'organizations', 'industry', 'experts', 
        'civil', 'society', 'academia', 'collaborate', 'issues', 'address', 'complex', 
        'challenges', 'opportunities', 'posed', 'rapid', 'adoption', 'technologies', 'globally'
    ],
    "National Innovation Plan.txt": [
        'kingdom', 'saudi', 'arabia', 'national', 'science', 'technology', 'innovation', 
        'plan', 'introduction', 'developed', 'long', 'term', 'vision', 'sti', 'create', 
        'knowledgebased', 'economy', 'society', 'globally', 'competitive', 'ecosystem', 
        'achieving', 'strategic', 'goal', 'becoming', 'advanced', 'countries', '1445h', 
        '2025', 'factors', 'hopefully', 'ensuring'
    ],
    "National Water Strategy 2030.txt": [
        'national', 'water', 'strategy', '2030', 'definition', 'key', 'terms', 'demand', 
        'irrigation', 'requirements', 'animal', 'husbandry', 'biological', 'aquaculture', 
        'sector', 'volume', 'stored', 'reservoirs', 'municipal', 'supply', 'system', 
        'production', 'storage', 'days', 'transport', 'distribution', 'average', 'demand'
    ],
    "Paris Agreement.txt": [
        'paris', 'agreement', 'united', 'nations', '2015', 'framework', 'climate', 
        'change', 'parties', 'convention', 'objective', 'equity', 'responsibilities', 
        'capabilities', 'national', 'circumstances'
    ],
    "Saudi Arabia's drought management strategy.txt": [
        'saudi', 'arabias', 'drought', 'management', 'strategy', 'integrates', 'efforts', 
        'national', 'water', 'strategy', 'nws', 'vision', '2030', 'renewable', 'energy', 
        'program', 'goal', 'secure', 'sustainable', 'resources', 'ensure', 'efficient', 
        'energy', 'use', 'enhance', 'resilience', 'climate', 'challenges', 'droughts', 
        'emerging', 'technologies', 'ai', '5g', 'optimizing', 'resource', 'management'
    ],
    "SDG 13.txt": [
        'sdg', '13', 'climate', 'action', 'urgent', 'combat', 'impacts', 'global', 
        'challenges', 'affecting', 'country', 'region', 'weather', 'events', 'rising', 
        'sea', 'levels', 'disruptions', 'food', 'water', 'supply', 'consequences', 
        'ecosystems', 'targets', 'strengthen', 'resilience'
    ],
    "SDG 6.txt": [
        'sdg', '6', 'clean', 'water', 'sanitation', 'availability', 'sustainable', 
        'management', 'access', 'fundamental', 'human', 'right', 'health', 'dignity', 
        'development', 'aspects', 'wastewater', 'treatment', 'ecosystems', 'wateruse', 
        'efficiency', 'targets'
    ],
    "SDG 9.txt": [
        'sdg', '9', 'industry', 'innovation', 'infrastructure', 'resilient', 
        'industrialization', 'sustainable', 'economic', 'growth', 'job', 'creation', 
        'development', 'solutions', 'challenges', 'targets'
    ],
    "UN Convention for Combatting Desertification.txt": [
        'united', 'nations', 'convention', 'combat', 'desertification', 'unccd', 'overview', 
        'adopted', '1994', 'binding', 'international', 'agreement', 'environment', 
        'development', 'sustainable', 'land', 'management', 'mitigate', 'effects', 
        'drought', 'regions', 'degradation', 'africa', 'asia', 'latin', 'america', 
        'climate', 'change', 'biodiversity'
    ],
    "Vision 2030.txt": [
        'mission', '2030', 'drought', 'management', 'strategy', 'saudi', 'arabia', 
        'introduction', 'part', 'vision', 'comprehensive', 'strategies', 'sustainable', 
        'development', 'effective', 'management', 'natural', 'resources', 'arid', 
        'climate', 'challenges', 'cuttingedge', 'technologies', 'including', 'ai', '5g', 
        'enhance', 'effectiveness'
    ]
}

# Define possible themes based on a comprehensive list of keywords
themes = {
    "Innovation & Technology": [
        'innovation', 'technology', 'ai', '5g', 'economic', 'growth', 'technologies', 
        'cuttingedge', 'digital', 'development'
    ],
    "Water Management": [
        'water', 'management', 'supply', 'reservoirs', 'sanitation', 'demand', 
        'irrigation', 'aquaculture', 'distribution', 'storage', 'resources'
    ],
    "Climate Change & Action": [
        'climate', 'change', 'action', 'drought', 'resilience', 'global', 'impacts', 
        'challenges', 'weather', 'events', 'sea', 'levels', 'disruptions', 'biodiversity'
    ],
    "Sustainable Development": [
        'sustainable', 'development', 'resources', 'effective', 'management', 'ecosystems', 
        'governance', 'resilience', 'environment', 'land'
    ],
    "Global Collaboration": [
        'global', 'partnership', 'international', 'organizations', 'collaboration', 
        'civil', 'society', 'academia', 'expert', 'platform'
    ]
}

# Function to extract themes from keywords
def extract_themes(keywords, themes):
    found_themes = []
    for theme, keywords_list in themes.items():
        if any(keyword in keywords for keyword in keywords_list):
            found_themes.append(theme)
    return found_themes

# Analyze each document and extract themes
for doc, keywords in documents_keywords.items():
    document_themes = extract_themes(keywords, themes)
    print(f"\nThemes for {doc}:")
    print(", ".join(document_themes))
