import anybadge
import coverage
import unittest

import test

tresholds = {
    40: 'red',
    60: 'orange',
    80: 'yellow',
    100: 'green',
}


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    unittest.main(module='test', exit=False)

    cov.stop()
    value = round(cov.report(morfs='to_be_tested.py'), 2)

    badge = anybadge.Badge("Coverage", value, thresholds=tresholds, value_suffix='%')

    badge.write_badge("Coverage.svg", overwrite=True)