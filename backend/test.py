import dns.rdatatype,dns.resolver
answers = []
for query_type in dns.rdatatype.RdataType:
    try:
        answers.extend(list(dns.resolver.resolve('google.com', query_type)))
    except dns.exception.DNSException:
        continue
for i in answers:
    print(i)