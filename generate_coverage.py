import anybadge
import sys

tresholds = {
    40: 'red',
    60: 'orange',
    80: 'yellow',
    100: 'green',
}

try:
    value = sys.argv[1]
except IndexError:
    print("No number given. Using value = 0")
    value = 0

if __name__ == '__main__':
    badge = anybadge.Badge("Coverage", value, thresholds=tresholds)

    badge.write_badge("Coverage.svg")