import anybadge
import coverage
import unittest


tresholds = {
    40: 'red',
    60: 'orange',
    80: 'yellow',
    100: 'green',
}


if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    
    from tests import test       # Needs to be after cov.start to count lines with function definition
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=2).run(suite)

    cov.stop()
    value = round(cov.report(morfs='src/to_be_tested.py'), 2)

    badge = anybadge.Badge("Coverage", value, thresholds=tresholds, value_suffix='%')

    try:
        badge.write_badge("docs/img/Coverage.svg")
    except:
        badge.write_badge("docs/img/Coverage.svg", overwrite=True)