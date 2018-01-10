def calc_add(x,y):
	pass
	# return x+y








def test_calculator_add_returns_correct_result():
	result = calc_add(2,2)
	assert result == 4


def test_calculator_returns_error_message_if_both_args_not_numbers():
	try:
            calc_add("two", "three")

        except ValueError:
            print("Exception caught")
            assert True, "Fail: ValueError exception not caught"

        except:
            assert False, "Fail: Exception other than ValueError caught"

        else: 
            assert False, "Fail: No exception caught"
