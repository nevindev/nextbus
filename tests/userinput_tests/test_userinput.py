import pytest

from userinput import userinput


valid_args = ['--route', 'a route', '--stop', 'a stop', '--direction', 'north']
invalid_args = ['--route', 'a route', '--stop', 'a stop', '--direction', 'foo']
missing_args = ['--route', 'a route', '--direction', 'north']


def test_get_user_inputs_with_valid_input_returns_values():
    route, stop, direction = userinput.get_user_input(args=valid_args)

    assert route == 'a route'
    assert stop == 'a stop'
    assert direction == 'north'


def test_get_user_inputs_with_invalid_input_exits():
    with pytest.raises(SystemExit):
        userinput.get_user_input(args=invalid_args)


def test_get_user_inputs_with_missing_input_exits():
    with pytest.raises(SystemExit):
        userinput.get_user_input(args=missing_args)
