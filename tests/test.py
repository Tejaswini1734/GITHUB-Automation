def test_all_cases():
    passed_count = [0]
    total = [0]

    # ✅ Basic Cases
    run_test_case([1, 2, 3, 4, 5], False, passed_count, total)
    run_test_case([1, 2, 3, 1], True, passed_count, total)
    run_test_case([], False, passed_count, total)
    run_test_case([42], False, passed_count, total)
    run_test_case([5, 5, 5, 5, 5], True, passed_count, total)

    # ✅ Edge Cases
    run_test_case([2**31 - 1, -2**31, 0, -1, 1], False, passed_count, total)
    run_test_case([-1000000, 1000000, 0, -1000000, 5000], True, passed_count, total)
    run_test_case([999999999, -999999999, 0], False, passed_count, total)
    run_test_case([1] * 1000000, True, passed_count, total)
    run_test_case(list(range(1000000)), False, passed_count, total)

    print(f"\nPassed {passed_count[0]} / {total[0]} test cases!")
    assert passed_count[0] == total[0]
