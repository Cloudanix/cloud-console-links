.PHONY: test coverage test-arn test-aws-links check

PYTEST = pytest

test:
	$(PYTEST) tests -q

coverage:
	$(PYTEST) tests --cov=cloudconsolelink --cov-report=term-missing -q

test-arn:
	$(PYTEST) tests/test_provider_coverage.py -k 'raw_arn_templates or helper_based_arn_templates or helper_functions_cover_all_arn_shapes' -q

test-aws-links:
	$(PYTEST) tests/test_aws.py -k 'cloudtrail or cloudwatch_loggroup or sns_topic' -q

check:
	$(MAKE) test
	$(MAKE) coverage
