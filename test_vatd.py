import pytest
import vatd


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 100}, 83.33),
                          ({'rate': 1.2, 'total': 1}, 0.83)])
def test_calculate_net_handles_integers(options, expected):
    assert expected == vatd.calculate_net(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 0.5}, 0.42),
                          ({'rate': 1.2, 'total': 0.99}, 0.83)])
def test_calculate_net_handles_values_less_than_one(options, expected):
    assert expected == vatd.calculate_net(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 1.999999}, 1.67),
                          ({'rate': 1.2, 'total': 1000.00000000001}, 833.33),
                          ({'rate': 1.2, 'total': 10.1}, 8.42)])
def test_calculate_net_rounds_floats(options, expected):
    assert expected == vatd.calculate_net(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': -10}, -8.33),
                          ({'rate': 1.2, 'total': -0.1}, -0.08),
                          ({'rate': 1.2, 'total': -100.111}, -83.43)])
def test_calculate_net_handles_negatives(options, expected):
    assert expected == vatd.calculate_net(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 100}, 16.67),
                          ({'rate': 1.2, 'total': 1}, 0.17)])
def test_calculate_refund_handles_integers(options, expected):
    assert expected == vatd.calculate_refund(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 0.5}, 0.08),
                          ({'rate': 1.2, 'total': 0.99}, 0.16)])
def test_calculate_refund_handles_values_less_than_one(options, expected):
    assert expected == vatd.calculate_refund(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': 1.999999}, 0.33),
                          ({'rate': 1.2, 'total': 1000.00000000001}, 166.67),
                          ({'rate': 1.2, 'total': 10.1}, 1.68)])
def test_calculate_refund_rounds_floats(options, expected):
    assert expected == vatd.calculate_refund(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.2, 'total': -10}, -1.67),
                          ({'rate': 1.2, 'total': -0.1}, -0.02),
                          ({'rate': 1.2, 'total': -100.110}, -16.69)])
def test_calculate_refund_handles_negatives(options, expected):
    assert expected == vatd.calculate_refund(options)


@pytest.mark.parametrize("options, expected",
                         [({'rate': 1.19, 'total': 100}, 84.03),
                          ({'rate': 1.195, 'total': 100}, 83.68),
                          ({'rate': 1.1, 'total': 100}, 90.91)])
def test_changes_in_rates(options, expected):
    assert expected == vatd.calculate_net(options)


def test_verbosity():
    options = {'rate': 1.2, 'total': 100.99}
    result = vatd.verbosity(options)
    expected = """
************************
Total Receipt:  £100.99
Net Value:      £84.16
Deductable VAT: £16.83
************************"""
    assert expected == result
