def test_jenkins():
    import jenkins

    server = jenkins.Jenkins('http://182.92.129.158:8889/', username="yuruotong1", password="11a47e33c625927b4e89506110d2625ec4")
    print(server.build_job("cekai17"))