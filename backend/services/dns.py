from dns import rdatatype,resolver

def get_dns_records(domain):
    answers = []
    query_types = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT",
        "CNAME",
        "CAA",
        "SOA"
    ]
    for query_type in query_types:
        try:
            answers.extend(list(dns.resolver.resolve(domain, query_type)))
        except dns.exception.DNSException:
            continue
