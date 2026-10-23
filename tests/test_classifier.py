from src.services.rule_classifier import RuleClassifier
from src.services.keyword_classifier import KeywordClassifier

def test_password_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I forgot my password")

    assert result == "account"


def test_fee_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I have a fee problem")

    assert result == "finance"


def test_technical_classification():
    classifier = RuleClassifier()

    result = classifier.classify("The server is down")

    assert result == "technical"


def test_unknown_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"

def test_keyword_login_classification():
    classifier = KeywordClassifier()
    result = classifier.classify("I cannot LOGIN to my account")
    assert result == "account"


def test_keyword_password_classification_is_not_finance():
    classifier = KeywordClassifier()
    result = classifier.classify("I forgot my password")
    # False 
    assert result == "account"


def test_keyword_voucher_classification():
    classifier = KeywordClassifier()
    result = classifier.classify("Where is my VOUCHER")
    assert result == "finance"


def test_keyword_payment_classification():
    classifier = KeywordClassifier()
    result = classifier.classify("The payment failed")
    assert result == "finance"




def test_keyword_server_classification():
    classifier = KeywordClassifier()
    result = classifier.classify("The server is down")
    # False
    assert result != "account"


def test_keyword_unknown_classification_is_not_technical():
    classifier = KeywordClassifier()
    result = classifier.classify("I want some information")
    # False
    assert result != "technical"